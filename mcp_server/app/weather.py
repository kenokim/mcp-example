# weather.py
import sys
from mcp.server.fastmcp import FastMCP
import httpx

# MCP 서버 생성
print("Starting server initialization...", file=sys.stderr)

mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(city: str) -> str:
    """도시의 현재 날씨를 반환합니다"""
    return f"{city}의 날씨는 맑음입니다."

@mcp.tool()
def get_alerts(region: str) -> str:
    """지역의 날씨 경보를 반환합니다"""
    return f"{region}의 날씨 경보: 없음"

if __name__ == "__main__":
    print("Initializing server...", file=sys.stderr)
    mcp.run(transport='stdio')