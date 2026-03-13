import os
from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

google_maps_api_key = os.environ.get("GOOGLE_MAPS_API_KEY")
if not google_maps_api_key:
    raise ValueError("GOOGLE_MAPS_API_KEY environment variable is not set")

headers = {
    "X-Goog-Api-Key": google_maps_api_key,
}

get_coordinates = McpToolset(
    connection_params=StreamableHTTPConnectionParams(
        url="https://mapstools.googleapis.com/mcp",
        headers=headers,
        timeout=10,
    ), tool_filter=["search_places"]
)

get_weather = McpToolset(
    connection_params=StreamableHTTPConnectionParams(
        url="https://weather-mcp-51955524638.us-central1.run.app/mcp",
        timeout=60,
    )
)

def mock_send_email(email: str) -> str:
    return f"Thanks! I have sent the weather summary to {email}"

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for giving weather updates of a US location and sending weather summaries on email.',
    instruction="""
        You are a helpful assistant that tells the weather of a US location using the 'get_weather' tool.
        When the user provides a location, use 'get_coordinates' to get the latitude and longitude of the place.
        And pass the latitude and longitude with 2 decimal points to the 'get_weather' tool to provide weather details.
        You can also send the weather summary to an email address using the 'mock_send_email' tool.
    """,
    tools=[get_coordinates, get_weather, mock_send_email]
)