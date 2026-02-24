from google.adk.agents import LlmAgent
from toolbox_core import ToolboxSyncClient

# Connect to running MCP toolbox server
toolbox = ToolboxSyncClient("http://localhost:5000")

# Load tools defined in tools.yaml
toolbox_tools = toolbox.load_toolset()

root_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="ecommerce_agent",
    description="Analytics agent for ecommerce BigQuery dataset.",
    instruction="""
You are an ecommerce analytics assistant.

Use the available tools to answer user questions.
Select the most appropriate tool.
Fill required parameters carefully.

Do not invent tools.
Do not answer from memory if a tool is available.
""",
    tools=toolbox_tools,
)