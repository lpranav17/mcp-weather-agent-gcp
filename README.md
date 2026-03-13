# 🌤️ MCP Weather Agent on GCP

A multi-tool AI agent built with **Google Agent Development Kit (ADK)** that chains multiple MCP servers to deliver weather updates for any US location.

## 🏗️ Architecture
```
User → ADK Agent (Gemini 2.5 Flash)
           ├── 🗺️ Google Maps MCP → converts city name to coordinates
           ├── 🌤️ Custom Weather MCP → fetches forecast from NWS API
           └── 📧 Email Tool → sends weather summary
```

## 🚀 Live Demo

- **Agent:** https://adk-postcards-51955524638.us-central1.run.app
- **Weather MCP Server:** https://weather-mcp-51955524638.us-central1.run.app

## 🛠️ Tech Stack

- **Google ADK** — AI agent framework
- **Gemini 2.5 Flash** — LLM powering the agent
- **FastMCP** — custom MCP server framework
- **Google Maps Grounding Lite MCP** — geocoding
- **US National Weather Service API** — weather data
- **Google Cloud Run** — serverless deployment

## 📁 Project Structure
```
mcp-weather-agent-gcp/
├── weather.py          # Custom Weather MCP server
├── Dockerfile          # Container for Weather MCP
├── postcards/
│   ├── agent.py        # ADK agent with chained MCP tools
│   └── __init__.py
└── README.md
```

## 🏃 Run Locally

### Weather MCP Server
```bash
uv init weather && cd weather
uv venv && source .venv/bin/activate
uv add fastmcp httpx
uv run weather.py
```

### ADK Agent
```bash
cd adk-postcards
uv add google-adk
uv run adk web
```

## ⚙️ Environment Variables

Create a `.env` file in the `postcards/` folder:
```
GOOGLE_MAPS_API_KEY=your-maps-api-key
GOOGLE_GENAI_USE_VERTEXAI=1
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
```

## 📖 Based On

This project was built following the [Postcards from the Cloud](https://sendmeapostcard.lovee.dev) lab.

## 📄 License

MIT License — feel free to use and build on this!
