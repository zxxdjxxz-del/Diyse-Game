FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY external-services/canary/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY external-services/canary/person_agent.py /app/person_agent.py
COPY external-services/canary/runtime_context.py /app/runtime_context.py
COPY external-services/canary/brains /app/brains
COPY external-services/canary/context /app/context
ENV PORT=8080
EXPOSE 8080
CMD ["python", "/app/person_agent.py"]
