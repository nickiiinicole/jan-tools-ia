import pytest
from fastmcp import Client
import asyncio
@pytest.fixture
def client():
    return Client("http://0.0.0.0:3355/mcp")

@pytest.mark.asyncio
async def test_tools(client):
    async with client:
        tools = await client.list_tools()
        lista_tools = [t.name for t in tools]
        assert 'sumar' in lista_tools
        assert 'restar' in lista_tools
        assert 'multiplicar' in lista_tools
        assert 'raiz_cuadrada' in lista_tools

@pytest.mark.asyncio
async def test_sum(client):
        tools = await client.list_tools()
        result = await client.call_tool("sumar", {
            "a":9, 
            "b":9
        })
        assert result.content[0].text == "18"


@pytest.mark.asyncio
async def test_rest(client):
        tools = await client.list_tools()
        result = await client.call_tool("restar", {
            "a":9, 
            "b":9
        })
        assert result.content[0].text == "0"

@pytest.mark.asyncio
async def test_multiplicar(client):
        tools = await client.list_tools()
        result = await client.call_tool("multiplicar", {
            "a":9, 
            "b":9
        })
        assert result.content[0].text == "81"


@pytest.mark.asyncio
async def test_raiz(client):
        tools = await client.list_tools()
        result = await client.call_tool("raiz_cuadrada", {
            "a":16
        })
        assert result.content[0].text == "4"

