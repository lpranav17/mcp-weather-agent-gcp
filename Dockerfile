FROM python:3.11-slim
WORKDIR /app

RUN adduser --disabled-password --gecos "" myuser

RUN apt-get update && apt-get install -y nodejs npm && rm -rf /var/lib/apt/lists/*

USER myuser
ENV PATH="/home/myuser/.local/bin:$PATH"

RUN pip install google-adk==1.26.0

COPY --chown=myuser:myuser postcards /app/agents/postcards

EXPOSE 8080

CMD adk web --port=8080 --host=0.0.0.0 --session_service_uri=memory:// --artifact_service_uri=memory:// "/app/agents"