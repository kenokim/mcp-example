# mcp-example
- https://modelcontextprotocol.io/quickstart/server

## Claude desktop 연동 예제
### 소스코드 디렉토리에서 아래 명령어 실행
- cd mcp_server
- uv venv
- source .venv/bin/activate
- uv pip install -r requirements.txt

### Claude desktop 에서 수정
```JSON
{
    "mcpServers": {
        "weather": {
            "command": "uv",
            "args": [
                "--directory",
                "/ABSOLUTE/PATH/TO/PARENT/FOLDER/weather",
                "run",
                "weather.py"
            ]
        }
    }
}
```

### Claude desktop 실행
- 대화 창의 도구 박스에 weather 관련 도구가 나타나면 성공