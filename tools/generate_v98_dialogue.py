#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, re, subprocess, sys

OUT = Path("docs/03_DIALOGUE/LINE_COMPLETE")
CHECKPOINT = "3fd07e92eda04f31ba613a654b3b1b28071f44e6"
OVERLAY = "> **Current migration overlay:** v2.20/Audit135 + later explicit corrections. Non-dialogue mechanical specifications embedded in this historical authoring source are context only; their live authority is in the system domains.\n\n"
EXTRACT = "> **Dialogue-domain extraction:** Exact approved spoken lines and relevant narrative staging are retained from the repository source. Combat moveset/stat/Card-effect sections are intentionally omitted because their current authority lives in `09_ENEMIES_AND_ENCOUNTERS` and `07_CARDS`.\n\n"
HEADER = """# {sid} — {title}
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current whole-project written authority:** **v2.20 / Audit135**, plus later explicit user corrections/current domain migrations.  
**Repository source checkpoint used for exact dialogue extraction:** `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Dialogue authority rule:** exact accepted spoken wording is preserved unless a later bounded canon correction directly supersedes a term or line. Story function lives in `02_STORY`; combat mechanics live in `05_BATTLE_SYSTEM` / `09_ENEMIES_AND_ENCOUNTERS`; Card mechanics live in `07_CARDS`; progression lives in `10_PROGRESSION_AND_EXP`.

**Source form:** converted from current Godot dialogue file `game/content/dialogue/chapter_00/{sid}.tres`.
**Scene kind:** {kind}
**Participants (source IDs):** {parts}

> Spoken text below is copied exactly from the current Resource. Current-facing staging terminology is normalized only where a later canon correction retired an internal label.

"""
TITLES = {"S001":"Opening","S002":"Wreck Field Exploration","S003":"Evacuation Relay Decision","S004":"Field Triage Camp","S005":"Confrontation","S006":"Aftermath","C01":"The Fire Is Too Close","C02":"Food After Triage"}
MAP = {
'CHAPTER_01/C03': {'source': 'docs/chapters/dialogue/chapter_01/C03.md', 'source_sha': '8b07878f19d5dc59413be0c6b84d649d839ab918d02e245519fd1f224bb6754f', 'target_sha': 'd435671ff7d012f8f10082126c7ddcec395df73cbb90c578ef556ad6c0e1c842'},
'CHAPTER_01/C04': {'source': 'docs/chapters/dialogue/chapter_01/C04.md', 'source_sha': '184ffa726a67a7f433f5a3d9205725111b73ab1a442671aa093e6a32d38bd35f', 'target_sha': 'fa480b4efe37fc0717c8be8f185de24097172aa4d6626c655bbd7324ff4c2164'},
'CHAPTER_01/C05': {'source': 'docs/chapters/dialogue/chapter_01/C05.md', 'source_sha': 'a3a511743947a1d5274596ab23f57a193ec8b8ecd5b3ea14b70e5325e9bd307f', 'target_sha': '6899065ccc2a1d071bb2b0485c3f9f68348e83ecc61a29f86cddad19b623cdf3'},
'CHAPTER_01/S007': {'source': 'docs/chapters/dialogue/chapter_01/S007.md', 'source_sha': '0f06baf0213a33f73ca7179a8b11435f40aab6dc7e844bf15f7c4335e6bdff5b', 'target_sha': 'a60dddd97634bb572163f2f5d255707533e9169c1f04570554165568df297fdd'},
'CHAPTER_01/S008': {'source': 'docs/chapters/dialogue/chapter_01/S008.md', 'source_sha': '66d30f731f859ec75ae0a45154c85522afc205a6a138ea641aa93a7079b6285d', 'target_sha': '4733c3465718f68df24dfe39bf65409164fee7c67c0c0de324b46149cc98329f'},
'CHAPTER_01/S009': {'source': 'docs/chapters/dialogue/chapter_01/S009.md', 'source_sha': '85205c88ad07e4e88d9253273ed01db6c288cf3241a60574dfb984a8dc85286b', 'target_sha': '72409987e578ae3efdfab2570c0fbb97afc7e1158b8b806b8262873ed9e68d3f'},
'CHAPTER_01/S010': {'source': 'docs/chapters/dialogue/chapter_01/S010.md', 'source_sha': '9b4f38d5b97a3ea023cf46f76ac9825214a22c34263fed501124615346946fed', 'target_sha': 'adb2a82c04f1a5e0708a0fa15e43e5d82668b4d540b33b29fb8ef37411c69f7d'},
'CHAPTER_01/S011': {'source': 'docs/chapters/dialogue/chapter_01/S011.md', 'source_sha': '4520ab2af222a2c6cbfc41bdb3b18ac24adeb3a1f156bf1933867e9c4d6de774', 'target_sha': '25c2d3509b331cad6854ebd2f3a71bd40434a4e6f40bdcb8a0c899e468c7f43f'},
'CHAPTER_02/C06': {'source': 'docs/chapters/dialogue/chapter_02/C06.md', 'source_sha': '09c302e81b092467520718419685e4c9a2e92b489233457bf6732a5ab45ba685', 'target_sha': '33ae743168304974be9c5cb7a8e0f279548750928de8880368e99a86da448cff'},
'CHAPTER_02/C07': {'source': 'docs/chapters/dialogue/chapter_02/C07.md', 'source_sha': '77dc9ff8de6bf42e4eca01f760296519677332130af200385189631177db192a', 'target_sha': 'ec6743f9f97216a730046b51500a872e95e6da2cab13d363d2a059f30ac2c4e5'},
'CHAPTER_02/S012': {'source': 'docs/chapters/dialogue/chapter_02/S012.md', 'source_sha': 'b35f43f7da44f55731a687c469f935eead0a3558253d8717874243ec51b79133', 'target_sha': 'f1c95b59b3cd58f91ccf526623a1d2b0d7ca1334a281287074543897879b9b9f'},
'CHAPTER_02/S013': {'source': 'docs/chapters/dialogue/chapter_02/S013.md', 'source_sha': 'f68df5757533e93979802b2e5990a45ec4bef7a7fe43575c3b57ddae6d055b44', 'target_sha': '22fda3100cf85ab8e75338c1d93b42155362bd04b1e47a904250d1bf28cb2ee8'},
'CHAPTER_02/S014': {'source': 'docs/chapters/dialogue/chapter_02/S014.md', 'source_sha': 'a4e908a40c24c3c86f00a7bb1b22a77ea6d696925ae0466457c53af4e92368fb', 'target_sha': 'f1491925a2902c915d82f75a750f2e0016aa5fb3c6b2633f8c8830a3fa438003'},
'CHAPTER_02/S015': {'source': 'docs/chapters/dialogue/chapter_02/S015.md', 'source_sha': '60b81fbf0cb3c2733cb15c9cbd307587d43c8744bf6b9a94f66aaa299869ddca', 'target_sha': '9d357d4609c1bfbe91d1f06ad66a5e425b036384aff491a721f585aec694d5b1'},
'CHAPTER_02/S016': {'source': 'docs/chapters/dialogue/chapter_02/S016.md', 'source_sha': '87afebc3cbfce04b4dc6c84f5149035d70c059623d32d35b3798c805288e12ae', 'target_sha': 'b877ab18ff20d1f7223b79496101e32f9c5ead81e03a5af4f2e86d695d5e9508'},
'CHAPTER_03/H01': {'source': 'docs/chapters/dialogue/chapter_03/H01.md', 'source_sha': '81e7501d0c8ae02b9665b56c153cbba64e8193dcbe15d1804c31fae61e8fc9c8', 'target_sha': '3048aec20907930742ab21c36af2185883ad73b9f00d8f31b767914ea7856b1a'},
'CHAPTER_03/H02': {'source': 'docs/chapters/dialogue/chapter_03/H02.md', 'source_sha': '2d38dd3f01c03e4515688dc207576055a3443190cd4ddef633b75d85e2b12a57', 'target_sha': 'cd13e8124dd2ca68a12cf64b06b5c5774d63033f3a54a249f70212ff1805b9c1'},
'CHAPTER_03/H03': {'source': 'docs/chapters/dialogue/chapter_03/H03.md', 'source_sha': '1fe10c7d653cab03c173914b307d96869922903f1c6fcc81ead6198303367116', 'target_sha': '72712f092a402a34303b164435671a6a282fe37bebdd14e4154674913223a9cc'},
'CHAPTER_03/H04': {'source': 'docs/chapters/dialogue/chapter_03/H04.md', 'source_sha': '7f73004c00df2212775510520e4069603c55c37927c43a52732043da2fcab83a', 'target_sha': '4a9c33b2139a06b8d4ad3cf308a5805466493c1d5743df3d919d9d3c54925728'},
'CHAPTER_03/S017': {'source': 'docs/chapters/dialogue/chapter_03/S017.md', 'source_sha': '5db98f663654380574912cb218322a65f50d284dbb32b3cd096a74acb9c3d4e6', 'target_sha': '70cf2ed6c3bfb8f6f554256457aec3b5d941eb4aa7e980cbcc6e3339971fd7a8'},
'CHAPTER_03/S018': {'source': 'docs/chapters/dialogue/chapter_03/S018.md', 'source_sha': 'f56be96a3a4968e72cd12d27ca6af869664ef3dd7e4f162956b3230731d2cc90', 'target_sha': 'e320eb586ff0aa1819af2335f83f71d125bb08ae0fa0ef436cd327c6482b2949'},
'CHAPTER_03/S019': {'source': 'docs/chapters/dialogue/chapter_03/S019.md', 'source_sha': '2a3c4bc9da40371323ca46f44edea9c7449b2c5368959c5563711b59d78f6fc5', 'target_sha': '8b252089982979d13fd5d21ae7b5b3937885169104f13c7de05e49b45f18c720'},
'CHAPTER_03/S020': {'source': 'docs/chapters/dialogue/chapter_03/S020.md', 'source_sha': '265c0b19f30c4587582c50bf53a8310c565942100762e11a68506bfc0a7c34fe', 'target_sha': '937e77c6718d90ec76906a3e43986b37d73bca4dc38313837206a2d9b1ca90cb'},
'CHAPTER_03/S021': {'source': 'docs/chapters/dialogue/chapter_03/S021.md', 'source_sha': 'b873803597f553446d82bfd22be0acf0ab9695446221ac287d85eeffdbd10458', 'target_sha': '810cd6a49eb22c4348433a046b5fd76b8b94d850b386211dfd11fbb9f99f196b'},
'CHAPTER_04/C08': {'source': 'docs/chapters/dialogue/chapter_04/C08.md', 'source_sha': 'cb6a34f51bd6bee2521f5520e42df4f29ab16be77bf77b24e7f5390f69444b43', 'target_sha': '73d83428861e4aaf9ca92e2e9a7fa9a04dc83ffae276d77b1e905a9a3801f71a'},
'CHAPTER_04/C09': {'source': 'docs/chapters/dialogue/chapter_04/C09.md', 'source_sha': '8f5f1be6eaa0700b07fd57672829597bde7fe6f528e27ab9b5a1a660b7120fef', 'target_sha': 'd00120ff0eb415db14422cb5e22f5741bca3558272379b2b92f2726a16efbec9'},
'CHAPTER_04/H05': {'source': 'docs/chapters/dialogue/chapter_04/H05.md', 'source_sha': '9f351c143bc4963d44017810275329a2bf077c2051b29ab16a6976462551e41e', 'target_sha': '4d9496c1e82f70ffd864d39a85d5772fa225b74ff0d1f17109584722eeb81e6c'},
'CHAPTER_04/HUNT_04_CROWN_PROTOTYPE_DIALOGUE': {'source': 'docs/chapters/dialogue/chapter_04/HUNT_04_CROWN_PROTOTYPE.md', 'source_sha': '25ff0d87ea911c387ca93466acdcb7cb47312c3f5ab5a20f46502551c676fcc5', 'target_sha': '15ce39996a4fd9fbe61452d72c966466c8afa0c591ddb3146422cf359b3fe326'},
'CHAPTER_04/S022': {'source': 'docs/chapters/dialogue/chapter_04/S022.md', 'source_sha': '84c75fb63caa2602913636191783211035f457cf46d20dcb2bca09c019d4673a', 'target_sha': '5c5c54bc12b5f93562d0e1b95645d9b8c3835d17750156488663d26fe1de70e4'},
'CHAPTER_04/S023': {'source': 'docs/chapters/dialogue/chapter_04/S023.md', 'source_sha': '7f54f320cf8a495bc1426210a2101be69a3bf281062f92608e1382f2178f380a', 'target_sha': '0c7bd46102fc391b63ebec45f94ce4668a6ac064e0add24500926cdf6522ef66'},
'CHAPTER_04/S024': {'source': 'docs/chapters/dialogue/chapter_04/S024.md', 'source_sha': 'b685bd7eec50653072a5684de983636d1ff2da6b782c96b2649669f3894fd377', 'target_sha': '2cc6740e9870e4cb2bbac81dba7f45799eac0f888e14c9464d772599152e3a18'},
'CHAPTER_04/S025': {'source': 'docs/chapters/dialogue/chapter_04/S025.md', 'source_sha': 'f3dccf604892bc5c11573e42a94c192af7b4426344dc0e7630fb43cc48c758d9', 'target_sha': 'c54505eb38684b07de9ab12c617367b705eb650f4c4f3f75078f6ee1a25c0131'},
'CHAPTER_04/S026': {'source': 'docs/chapters/dialogue/chapter_04/S026.md', 'source_sha': '1475309d0fb1135a35abe6a5c2e9c39eecd54b04aa6578d6f97f28d811e80eab', 'target_sha': 'e87107e86482c5ad531581e546e8955d0282572d15b712061eb477cbdea3443f'},
'Ch0/C01': {'source': 'game/content/dialogue/chapter_00/C01.tres', 'source_sha': 'e53e8459a59a350353b383bad31b7532bbee3a633f310131dd15f3da53d74f0f', 'target_sha': '26e5dfc1ed75024bd137c98bdbb481d49ed347f21ff1de93f6d69fea6dfd9668'},
'Ch0/C02': {'source': 'game/content/dialogue/chapter_00/C02.tres', 'source_sha': 'b8865cfcc2583b542e67756e3f7b5ac4b89610377c5b0a95a93d27474a6ded38', 'target_sha': '64e304ea6671f30a5ab734ff9806840f28b781c2bc9210706204424c724d2df4'},
'Ch0/S001': {'source': 'game/content/dialogue/chapter_00/S001.tres', 'source_sha': '8714a9d0c2ddde8ea5127b212b934bf8ca92b2a5853b190263bdfe3f280d4375', 'target_sha': '1ee5f5f024cff9d3963177a96aaa4efef7a8634c3d81eb02b20a960c2a74e579'},
'Ch0/S002': {'source': 'game/content/dialogue/chapter_00/S002.tres', 'source_sha': '33e2a892b0466139a9be5015f2bd296130206d05a14f55a50101c4f852559ce4', 'target_sha': '2a8747e96e56170792f1adbf21269696efd481828ff0d2223276155138a23e7f'},
'Ch0/S003': {'source': 'game/content/dialogue/chapter_00/S003.tres', 'source_sha': '046ea4b19d6ef424e55f3bab9e47fea24cead7cdf32107d640213ea57a279bc0', 'target_sha': '04e61f21bb934e92de09899f3aa08f75760d49dffbd8ad70068b5d44da3a3662'},
'Ch0/S004': {'source': 'game/content/dialogue/chapter_00/S004.tres', 'source_sha': '7966be914176842ff730cc321a2e979093a95fead24a1c26c75411c0f286f260', 'target_sha': '1044ab2d3dc5b96042171ad51b68868a310d54c08861deba0b5e1e6d402c4ef1'},
'Ch0/S005': {'source': 'game/content/dialogue/chapter_00/S005.tres', 'source_sha': 'a12a87669f3ebf8993aeafc0c66e85ee3963509a7f5874779686152ba7f25e2d', 'target_sha': 'cc353fe3f2d3de38dc4735b1642c4f8b21468973c102872138cf223ad91479e6'},
'Ch0/S006': {'source': 'game/content/dialogue/chapter_00/S006.tres', 'source_sha': '7daf57fc0acdf576418162aa3679fbdda9fc7c8363248c45421f697d181837fe', 'target_sha': 'd1f0b4cb358d583a173a3e19f3910113a62c1897fd9345da99a67f88067a3e68'}
}

def sha_bytes(b): return hashlib.sha256(b).hexdigest()
def source_bytes(path): return subprocess.check_output(["git", "show", f"{CHECKPOINT}:{path}"])
def unesc(x): return json.loads('"' + x + '"')

def parse_tres_text(s):
    kind=re.search(r'^scene_kind = "([^"]*)"', s, re.M).group(1)
    pm=re.search(r'^participants = Array\[String\]\(\[(.*?)\]\)', s, re.M)
    parts=re.findall(r'"([^"]+)"', pm.group(1)) if pm else []
    body=s[s.index("beats = [")+len("beats = ["):]
    if body.endswith("]"): body=body[:-1]
    chunks=re.split(r'\n\}, \{\n', body)
    beats=[]
    for ch in chunks:
        def fld(name):
            m=re.search(rf'"{name}":\s*"((?:\\.|[^"])*)"', ch, re.S)
            return unesc(m.group(1)) if m else ""
        beats.append((fld("beat_id"), fld("speaker_id"), fld("text"), fld("staging")))
    return kind, parts, beats

def gen_ch0(src, source_text):
    sid=Path(src).stem
    kind, parts, beats=parse_tres_text(source_text)
    out=HEADER.format(sid=sid,title=TITLES[sid],kind=kind,parts=", ".join(parts))
    for bid, speaker, text, staging in beats:
        text=text.replace("Broken Champion's Ward","incomplete protective response")
        staging=staging.replace("Broken Champion's Ward","incomplete protective response")
        out += f"## {bid}\n"
        if text: out += f"**{speaker.replace('_',' ').upper()}:** {text}\n"
        if staging: out += f"\n*Staging: {staging}*\n"
        out += "\n"
    return out.rstrip()+"\n"

def gen_md(scene, src, text):
    if scene=="CHAPTER_04/HUNT_04_CROWN_PROTOTYPE_DIALOGUE":
        i7=text.index("# 7. CROWN PROTOTYPE — COMBAT IDENTITY")
        i10=text.index("# 10. DEFEAT")
        ir=text.index("### FIRST-CLEAR REWARD")
        i12=text.index("# 12. AFTERMATH")
        i14=text.index("# 14. CHEAP 2.5D PRODUCTION PASS")
        return (EXTRACT + text[:i7] + text[i10:ir] + text[i12:i14]).rstrip()+"\n"
    out=OVERLAY+text
    if scene=="CHAPTER_01/S009": out=out.replace("No future Sixfold Accord knowledge.","No future Sixfold Volition knowledge.")
    if scene=="CHAPTER_03/S019": out=out.replace("**NIMERA:** Might. Elements. Grace. Resource. Change. Ruin.","**NIMERA:** Might. Elements. Grace. Acuity. Change. Ruin.")
    return out

def target_path(scene):
    if scene.startswith("Ch0/"): return OUT/"CHAPTER_00"/(scene.split("/",1)[1]+".md")
    chapter,name=scene.split("/",1)
    return OUT/chapter/(name+".md")

def main():
    generated=0
    for scene, meta in MAP.items():
        src=meta["source"]
        sb=source_bytes(src)
        if sha_bytes(sb) != meta["source_sha"]: raise SystemExit(f"SOURCE HASH FAIL {scene}: {src}")
        source_text=sb.decode("utf-8")
        text=gen_ch0(src, source_text) if scene.startswith("Ch0/") else gen_md(scene,src,source_text)
        tb=text.encode("utf-8")
        got=sha_bytes(tb)
        if got != meta["target_sha"]: raise SystemExit(f"TARGET HASH FAIL {scene}: {got} != {meta['target_sha']}")
        dst=target_path(scene); dst.parent.mkdir(parents=True, exist_ok=True); dst.write_bytes(tb); generated+=1
    if generated != 41: raise SystemExit(f"COUNT FAIL {generated}")
    print("PASS: generated and SHA-validated 41/41 exact v98 dialogue transcripts.")

if __name__=="__main__": main()
