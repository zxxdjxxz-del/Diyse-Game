#!/usr/bin/env python3
"""Executable offline adversarial coverage for the automatic Person context boundary."""
from __future__ import annotations

import asyncio
import copy
import importlib
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import AsyncMock, patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'external-services/canary'))
sys.path.insert(0, str(ROOT / 'tools/dialogue'))
import runtime_context as runtime
import compile_scene_authority as compiler


def request(chapter=8, sequence=10, people=None, mode='all_committed_story'):
    return {
        'request_id': 'test', 'scene_id': 'CURRENT', 'story_position': f'Chapter {chapter} test',
        'canon_snapshot_id': 'test-canon', 'continuity_namespace': 'story',
        'participants': people or ['ilyra', 'seyrik'],
        'context_construction': {'schema': runtime.SCHEMA, 'chapter_id': f'chapter_{chapter:02}',
            'story_clock': {'chapter': chapter, 'sequence': sequence}, 'forward_only': True,
            'continuity_policy': {'mode': mode}, 'assertions': []},
    }


def effect(kind, key, value, **kwargs):
    return {'kind': kind, 'key': key, 'value': value, **kwargs}


def assertion(req, kind, key, value, owner='ilyra', **kwargs):
    row = effect(kind, key, value, owner_id=owner,
                 id=f'assertion-{len(req["context_construction"]["assertions"])}', **kwargs)
    req['context_construction']['assertions'].append(row)
    return row


def memory(mid='m1', chapter=7, sequence=1, owner='ilyra', effects=None, **kwargs):
    return {'memory_id': mid, 'owner_id': owner, 'source_scene_id': f'scene-{mid}',
        'source_story_clock': {'chapter': chapter, 'sequence': sequence},
        'canon_snapshot_id': 'test-canon', 'privacy_visibility_scope': 'private',
        'commit_provenance': {'canon_check_status': 'PASS', 'author_approved': True},
        'context_effects': effects or [], **kwargs}


class ContextTests(unittest.TestCase):
    def test_historical_rewrite_even_explicit_ids_cannot_allow_later_memories(self):
        req = request(3, people=['torren', 'nimera'], mode='explicit_ids')
        req['context_construction']['continuity_policy']['authorized_memory_ids'] = ['early', 'late']
        early = memory('early', 2, owner='torren')
        late = memory('late', 10, owner='torren', content_summary='FUTURE_SECRET')
        built = runtime.build_person_context(req, 'torren', [late, early])
        self.assertEqual(built['memory_authorization']['authorized_memory_ids'], ['early'])
        self.assertNotIn('FUTURE_SECRET', json.dumps(built))

    def test_private_information_is_owned_by_only_one_participant(self):
        req = request()
        secret = memory(effects=[effect('epistemic', 'private_preference', 'PRIVATE_SECRET', status='trusted_report')])
        a = runtime.build_person_context(req, 'ilyra', [secret])
        b = runtime.build_person_context(req, 'seyrik', [secret])
        self.assertEqual(a['epistemic_state']['private_preference']['status'], 'trusted_report')
        self.assertNotIn('PRIVATE_SECRET', json.dumps(b))
        secret['privacy_visibility_scope'] = {'kind': 'shared', 'allowed_character_ids': ['seyrik']}
        self.assertEqual(runtime.build_person_context(req, 'ilyra', [secret])['epistemic_state'], {})

    def test_ilyra_seyrik_safe_refusal_before_affectionate_insult(self):
        req = request()
        refusal = memory('refusal', effects=[effect('relationship', 'refusal_safety', 'established', target_id='seyrik'),
                                            effect('relationship', 'trust', 'high', target_id='seyrik')])
        affection = memory('affection', 10, effects=[effect('relationship', 'affectionate_insult_permission', 'established', target_id='seyrik')])
        built = runtime.build_person_context(req, 'ilyra', [affection, refusal])
        vector = built['relationship_runtime_state']['seyrik']
        self.assertEqual(vector['refusal_safety'], 'established')
        self.assertEqual(vector['trust'], 'high')
        self.assertEqual(vector['disclosure_comfort'], 'unknown')
        self.assertEqual(vector['affectionate_insult_permission'], 'unknown')
        self.assertEqual(runtime.build_person_context(req, 'seyrik', [refusal])['relationship_runtime_state']['ilyra']['trust'], 'unknown')

    def test_torren_nimera_familial_shorthand_does_not_leak_backward(self):
        req = request(4, people=['torren', 'nimera'])
        professional = memory('respect', 3, owner='torren', effects=[effect('relationship', 'chronology_stage', 'professional_respect', target_id='nimera')])
        familial = memory('familial', 11, owner='torren', effects=[effect('relationship', 'borrowed_language', 'late_familial_shorthand', target_id='nimera')])
        built = runtime.build_person_context(req, 'torren', [professional, familial])
        self.assertEqual(built['relationship_runtime_state']['nimera']['chronology_stage'], 'professional_respect')
        self.assertNotIn('late_familial_shorthand', json.dumps(built))

    def test_corrected_belief_keeps_historical_mistake(self):
        old = memory('mistake', 3, effects=[effect('epistemic', 'route', 'north', status='misunderstanding')])
        correction = memory('correction', 5, effects=[effect('epistemic', 'route', 'south', status='known_fact')])
        built = runtime.build_person_context(request(), 'ilyra', [correction, old])
        self.assertEqual(built['epistemic_state']['route'], {'status': 'known_fact', 'value': 'south'})
        self.assertEqual(built['belief_history']['route'][0]['status'], 'misunderstanding')
        past = runtime.build_person_context(request(4), 'ilyra', [correction, old])
        self.assertEqual(past['epistemic_state']['route']['status'], 'misunderstanding')
        self.assertNotIn('south', json.dumps(past))

    def test_all_epistemic_states_remain_distinct_and_forbidden_answers_are_redacted(self):
        req = request()
        for state in runtime.EPISTEMIC_STATES:
            assertion(req, 'epistemic', state, f'answer-{state}', status=state)
        built = runtime.build_person_context(req, 'ilyra')
        self.assertEqual({v['status'] for v in built['epistemic_state'].values()}, runtime.EPISTEMIC_STATES)
        self.assertNotIn('answer-forbidden_future', json.dumps(built))
        self.assertNotIn('answer-unknown', json.dumps(built))

    def test_no_memory_authorized_still_injects_current_authority(self):
        req = request(mode='none')
        assertion(req, 'hard', 'equipment_restrictions', 'Wardrods')
        built = runtime.build_person_context(req, 'ilyra', [memory(content_summary='not allowed')])
        self.assertEqual(built['memory_authorization'], {'mode': 'none'})
        self.assertEqual(built['hard_context']['equipment_restrictions'], 'Wardrods')
        self.assertEqual(built['epistemic_state'], {})

    def test_forward_only_requires_explicit_policy_and_still_checks_chronology(self):
        req = request()
        rows = [memory('past'), memory('later', 12)]
        self.assertEqual(runtime.build_person_context(req, 'ilyra', rows)['memory_authorization']['authorized_memory_ids'], ['past'])
        req['context_construction']['forward_only'] = False
        with self.assertRaises(runtime.ContextError):
            runtime.build_person_context(req, 'ilyra', rows)

    def test_explicit_prior_continuity_without_numeric_order(self):
        req = request(mode='scene_ids')
        req['context_construction']['story_clock'] = {}
        req['context_construction']['continuity_policy'].update(authorized_scene_ids=['scene-prior', 'scene-future'], prior_scene_ids=['scene-prior', 'scene-future'])
        row = memory('prior')
        row.pop('source_story_clock')
        built = runtime.build_person_context(req, 'ilyra', [row, memory('future', 12)])
        self.assertEqual(built['memory_authorization']['authorized_memory_ids'], ['prior'])

    def test_silent_and_nonparticipating_people(self):
        for participation in ('silent', 'nonparticipating'):
            req = request()
            assertion(req, 'local', 'participation', participation)
            local = runtime.build_person_context(req, 'ilyra')['scene_local_state']
            self.assertFalse(local['current_desire_to_speak'])
            self.assertEqual(local['spoken_expression'], 'none')

    def test_conflicting_motives_are_preserved_without_choosing_winner(self):
        req = request()
        assertion(req, 'local', 'immediate_wants', ['rest', 'finish the work'])
        assertion(req, 'local', 'immediate_avoidances', ['pressure Seyrik'])
        assertion(req, 'local', 'current_task', 'finish the work')
        local = runtime.build_person_context(req, 'ilyra')['scene_local_state']
        self.assertEqual(local['immediate_wants'], ['rest', 'finish the work'])
        self.assertEqual(local['immediate_avoidances'], ['pressure Seyrik'])
        self.assertEqual(local['motive_resolution'], 'open')
        self.assertEqual(local['motive_candidates'][0]['status'], 'inference')
        self.assertEqual(local['private_appraisal'], 'unknown')
        self.assertEqual(local['visible_behavior'], 'open')
        self.assertEqual(local['spoken_expression'], 'open')

    def test_stale_future_context_and_wrong_canon_never_override_rebuild(self):
        req = request(3)
        req['person_runtime_contexts'] = {'ilyra': {'epistemic_state': {'secret': 'STALE_FUTURE'}}}
        stale = memory('stale', 2, canon_snapshot_id='old-canon')
        built = runtime.build_person_context(req, 'ilyra', [stale])
        self.assertNotIn('STALE_FUTURE', json.dumps(built))
        self.assertEqual(built['memory_authorization']['authorized_memory_ids'], [])

    def test_authorization_before_budget_and_hard_deltas_before_salience(self):
        req = request()
        boundary = memory('boundary', 2, effects=[effect('relationship', 'refusal_safety', 'established', target_id='seyrik')])
        rows = [memory(f'noise{i}', 12, practical_salience=9999) for i in range(100)] + [boundary]
        built = runtime.build_person_context(req, 'ilyra', rows)
        self.assertEqual(built['memory_authorization']['authorized_memory_ids'], ['boundary'])
        self.assertEqual(built['relationship_runtime_state']['seyrik']['refusal_safety'], 'established')

    def test_transient_state_and_threads_have_explicit_lifetime(self):
        rows = [memory('state', effects=[effect('physical', 'fatigue', 'tired'),
                effect('emotional', 'anger', 'established', applies_to_scene_ids=['CURRENT']),
                effect('thread', 'promise', 'return the book', status='open')]),
                memory('resolved', sequence=2, effects=[effect('thread', 'promise', 'returned', status='resolved')])]
        built = runtime.build_person_context(request(), 'ilyra', rows)
        self.assertEqual(built['physical_state'], {})
        self.assertEqual(built['emotional_state'], {'anger': 'established'})
        self.assertEqual(built['open_threads'], [])

    def test_conflicting_same_position_evidence_stays_unknown(self):
        rows = [memory('a', effects=[effect('relationship', 'trust', 'high', target_id='seyrik')]),
                memory('b', effects=[effect('relationship', 'trust', 'low', target_id='seyrik')])]
        built = runtime.build_person_context(request(), 'ilyra', rows)
        self.assertEqual(built['relationship_runtime_state']['seyrik']['trust'], 'unknown')
        self.assertIn('conflicting_evidence:relationship.seyrik.trust', built['unresolved_dependencies'])

    def test_memory_cannot_override_hard_canon_and_build_does_not_mutate_inputs(self):
        req = request()
        assertion(req, 'hard', 'equipment_restrictions', 'current')
        rows = [memory(effects=[effect('hard', 'equipment_restrictions', 'retired')])]
        original = copy.deepcopy((req, rows))
        built = runtime.build_person_context(req, 'ilyra', rows)
        self.assertEqual(built['hard_context']['equipment_restrictions'], 'current')
        self.assertEqual((req, rows), original)
        self.assertEqual(built, runtime.build_person_context(req, 'ilyra', rows))

    def test_unverified_legacy_and_sandbox_memory_is_denied(self):
        row = memory()
        row.pop('commit_provenance')
        self.assertEqual(runtime.build_person_context(request(), 'ilyra', [row])['memory_authorization']['authorized_memory_ids'], [])
        req = request()
        req['continuity_namespace'] = 'sandbox'
        self.assertEqual(runtime.build_person_context(req, 'ilyra', [memory()])['memory_authorization']['authorized_memory_ids'], [])


class CompilerTests(unittest.TestCase):
    def setUp(self):
        self.spec = json.loads((ROOT / 'tests/dialogue/fixtures/authority_ch1_brackenwall_protocol.json').read_text())

    def test_source_backed_assertions_and_tamper_rejection(self):
        self.spec['context_assertions'] = [dict(id='custody', owner_id='cyanis', kind='epistemic', key='card_custody',
            value='Card stays with Cyanis', status='known_fact',
            source=self.spec['story_sources'][0], source_quote='Card stays with Cyanis; Ilyra monitors only real changes;')]
        req = compiler.compile_spec_data(self.spec)['request_seed']
        self.assertEqual(req['person_runtime_contexts']['cyanis']['epistemic_state']['card_custody']['status'], 'known_fact')
        self.assertNotIn('card_custody', req['person_runtime_contexts']['ilyra']['epistemic_state'])
        req['context_construction']['assertions'][0]['value'] = 'tampered'
        with self.assertRaises(runtime.ContextError):
            runtime.build_person_context(req, 'cyanis')
        self.spec['context_assertions'][0]['source_quote'] = 'fabricated quote'
        with self.assertRaises(compiler.CompileError):
            compiler.compile_spec_data(self.spec)

    def test_scene_identity_and_character_profile_are_fingerprinted(self):
        req = compiler.compile_spec_data(self.spec)['request_seed']
        req['story_position'] = 'a different historical scene'
        with self.assertRaises(runtime.ContextError):
            runtime.build_person_context(req, 'cyanis')
        req = compiler.compile_spec_data(self.spec)['request_seed']
        req['participant_profiles']['cyanis']['authority_text'] += '\n- Age: **999**'
        with self.assertRaises(runtime.ContextError):
            runtime.build_person_context(req, 'cyanis')

    def test_malformed_order_fails_with_compile_error(self):
        self.spec['story_clock'] = 'Chapter 1 after something'
        with self.assertRaises(compiler.CompileError):
            compiler.compile_spec_data(self.spec)

    def test_owning_story_annotations_are_discovered_without_manual_contexts(self):
        original = compiler._read_text
        annotation = [dict(id='test', owner_id='cyanis', kind='local', key='participation', value='silent')]
        def source(root, path):
            text = original(root, path)
            if path == 'docs/02_STORY/CHAPTERS/CHAPTER_01.md':
                text = text.replace('## Beat 1 — Brackenwall / Protocol', '## Beat 1 — Brackenwall / Protocol\n\n```diyse-context\n' + json.dumps(annotation) + '\n```')
            return text
        with patch.object(compiler, '_read_text', side_effect=source):
            req = compiler.compile_spec_data(self.spec)['request_seed']
        self.assertEqual(req['person_runtime_contexts']['cyanis']['scene_local_state']['participation'], 'silent')


class ServiceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        os.environ['PERSISTENCE_PATH'] = str(Path(cls.temp.name) / 'initial.sqlite')
        os.environ['CHARACTER_ID'] = 'ilyra'
        cls.agent = importlib.import_module('person_agent')
        cls.orchestrator = importlib.import_module('scene_orchestrator')

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def setUp(self):
        self.agent.CANON_SNAPSHOT_ID = 'test-canon'
        self.orchestrator.CANON_SNAPSHOT_ID = 'test-canon'
        self.agent.STORE = self.agent.Store(str(Path(self.temp.name) / f'{self.id()}.sqlite'))

    def test_commit_requires_pass_and_author_approval_and_stamps_provenance(self):
        payload = dict(request_id='commit', scene_id='prior', canon_snapshot_id='test-canon',
            canon_check_status='PASS', expected_previous_revision='0', source_story_clock={'chapter': 7, 'sequence': 1},
            filtered_event_ledger={'memories': [memory(owner='seyrik', effects=[effect('relationship', 'trust', 'high', target_id='seyrik')])]})
        with self.assertRaises(self.agent.HTTPException):
            self.agent.commit(self.agent.CommitRequest(**payload))
        payload['author_approved'] = True
        payload['canon_check_status'] = 'FAIL'
        with self.assertRaises(self.agent.HTTPException):
            self.agent.commit(self.agent.CommitRequest(**payload))
        payload['canon_check_status'] = 'PASS'
        first = self.agent.commit(self.agent.CommitRequest(**payload))
        self.assertEqual(first, self.agent.commit(self.agent.CommitRequest(**payload)))
        rows = self.agent.STORE.memories('story', limit=-1)
        self.assertEqual(rows[0]['owner_id'], 'ilyra')
        self.assertEqual(rows[0]['source_scene_id'], 'prior')
        built = self.agent.runtime_context(self.agent.TurnRequest(**request()))
        self.assertEqual(built['person_runtime_context']['relationship_runtime_state']['seyrik']['trust'], 'high')

    def test_person_turn_rebuilds_and_does_not_send_latest_state_or_raw_authority(self):
        self.agent.STORE.commit_story('state', '0', {'state': {'fear': 'FUTURE_STATE_SECRET'}})
        req = request()
        req['scene_context'] = {'authority_packet': {'future': 'AUTHOR_ONLY_SECRET'}}
        req['current_floor_state'] = {'private_knowledge': 'FLOOR_STATE_SECRET'}
        req['person_runtime_context'] = {'epistemic_state': {'future': 'CACHED_SECRET'}}
        model = AsyncMock(return_value={'memory_refs': [], 'observable_candidate': {'speech': 'hello'}})
        with patch.object(self.agent, 'model_json', model):
            asyncio.run(self.agent.turn(self.agent.TurnRequest(**req)))
        sent = json.dumps(model.call_args.args[1])
        for secret in ('FUTURE_STATE_SECRET', 'AUTHOR_ONLY_SECRET', 'CACHED_SECRET', 'FLOOR_STATE_SECRET'):
            self.assertNotIn(secret, sent)
        self.assertEqual(self.agent.STORE.revision(), '1')

    def test_silent_person_no_model_call_and_revision_conflict_stops_build(self):
        req = request()
        assertion(req, 'local', 'participation', 'nonparticipating')
        with patch.object(self.agent, 'model_json', AsyncMock()) as model:
            result = asyncio.run(self.agent.turn(self.agent.TurnRequest(**req)))
            model.assert_not_called()
        self.assertTrue(result['observable_candidate']['silence'])
        req['expected_story_revision'] = '999'
        with self.assertRaises(self.agent.HTTPException):
            self.agent.runtime_context(self.agent.TurnRequest(**req))

    def test_orchestrator_builds_before_director_and_never_commits(self):
        req = request()
        assertion(req, 'local', 'participation', 'silent')
        req['scene_purpose'] = 'offline test'
        req['participant_profiles'] = {'seyrik': {'character_id': 'seyrik'}}
        calls = []
        async def agent_call(cid, method, path, payload=None):
            calls.append(path)
            if path == '/v1/context-snapshot':
                return self.agent.context_snapshot()
            if path == '/v1/runtime-context':
                return self.agent.runtime_context(self.agent.TurnRequest(**payload))
            raise AssertionError(f'Unexpected call: {path}')
        plan = {'scene_mode': 'full_authored_stop_scene', 'movement_lock': True,
                'beat_plan': [{'beat_id': 'b1', 'eligible_speakers': ['ilyra']}]}
        model = AsyncMock(side_effect=[plan, {'status': 'PASS', 'per_character_event_ledgers': {}}])
        with patch.object(self.orchestrator, 'AGENT_URLS', {'ilyra': 'http://fake'}), \
             patch.object(self.orchestrator, 'agent_request', side_effect=agent_call), \
             patch.object(self.orchestrator, 'model_json', model):
            result = asyncio.run(self.orchestrator.build_scene(self.orchestrator.SceneBuildRequest(**req)))
        self.assertEqual(calls, ['/v1/context-snapshot', '/v1/runtime-context'])
        self.assertTrue(result['scene_beats'][0]['silence'])
        self.assertEqual(self.agent.STORE.revision(), '0')
        director = model.call_args_list[0].args[1]
        self.assertFalse(director['person_runtime_contexts']['ilyra']['scene_local_state']['current_desire_to_speak'])
        self.assertNotIn('story_memory_index', json.dumps(director['agent_public_state_snapshots']))

    def test_unauthorized_model_memory_reference_rejected(self):
        model = AsyncMock(return_value={'memory_refs': ['not-authorized']})
        with patch.object(self.agent, 'model_json', model), self.assertRaises(self.agent.HTTPException):
            asyncio.run(self.agent.turn(self.agent.TurnRequest(**request(mode='none'))))

    def test_normal_turn_through_orchestrator_uses_compiled_plan(self):
        spec = json.loads((ROOT / 'tests/dialogue/fixtures/authority_ch1_brackenwall_protocol.json').read_text())
        spec['participants'] = ['ilyra']
        req = compiler.compile_spec_data(spec)['request_seed']
        self.agent.CANON_SNAPSHOT_ID = req['canon_snapshot_id']
        self.orchestrator.CANON_SNAPSHOT_ID = req['canon_snapshot_id']
        async def agent_call(cid, method, path, payload=None):
            if path == '/v1/context-snapshot':
                return self.agent.context_snapshot()
            if path == '/v1/runtime-context':
                return self.agent.runtime_context(self.agent.TurnRequest(**payload))
            if path == '/v1/turn':
                return await self.agent.turn(self.agent.TurnRequest(**payload))
            raise AssertionError(path)
        director = {'scene_mode': 'full_authored_stop_scene', 'movement_lock': True,
                    'beat_plan': [{'beat_id': 'b1', 'eligible_speakers': ['ilyra']}]}
        agent_model = AsyncMock(return_value={'memory_refs': [], 'observable_candidate': {'speech': 'Test line.'}})
        scene_model = AsyncMock(side_effect=[director, {'selected_speaker_id': 'ilyra', 'text': 'Test line.'},
                                            {'status': 'PASS', 'per_character_event_ledgers': {}}])
        with patch.object(self.orchestrator, 'AGENT_URLS', {'ilyra': 'http://fake'}), \
             patch.object(self.orchestrator, 'agent_request', side_effect=agent_call), \
             patch.object(self.orchestrator, 'model_json', scene_model), \
             patch.object(self.agent, 'model_json', agent_model):
            result = asyncio.run(self.orchestrator.build_scene(self.orchestrator.SceneBuildRequest(**req)))
        self.assertTrue(result['commit_ready'])
        self.assertEqual(result['scene_beats'][0]['text'], 'Test line.')
        self.assertEqual(self.agent.STORE.revision(), '0')
        sent = agent_model.call_args.args[1]['request']
        self.assertEqual(sent['person_runtime_context']['hard_context']['identity']['full_name'], 'Ilyra Amarin')
        self.assertNotIn('source_records', json.dumps(sent))

    def test_authorized_old_database_memory_survives_more_than_64_future_rows(self):
        rows = [memory('early', 2)] + [memory(f'future-{i}', 12) for i in range(70)]
        with self.agent.STORE.connect() as con:
            for row in rows:
                self.agent.STORE.add_memory(con, 'story', 'observed_event', row['source_scene_id'], row)
        result = self.agent.runtime_context(self.agent.TurnRequest(**request(3)))
        self.assertEqual(result['person_runtime_context']['memory_authorization']['authorized_memory_ids'], ['early'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
