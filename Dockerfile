<<<<<<< HEAD
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
=======
FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev

COPY weather.py .

ENV PORT=8080
EXPOSE $PORT

CMD ["uv", "run", "weather.py"]
>>>>>>> 245bfbe5ab73099f7438238e2e945f261743aabd
