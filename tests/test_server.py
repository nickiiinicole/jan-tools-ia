from fastmcp import Client
import asyncio
async def test_server():
    async with Client("http://127.0.0.1:3355/mcp") as client:
# List available tools
        tools = await client.list_tools()
        print("Available tools:", [t.name for t in tools])
        print(tools[0])