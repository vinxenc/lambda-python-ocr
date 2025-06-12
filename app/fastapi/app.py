from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from Lambda"}

# Add a catch-all route for debugging
@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def catch_all(request: Request, path: str):
    body = await request.body()
    try:
        body_json = json.loads(body) if body else {}
    except:
        body_json = {"raw": str(body)}
    
    return {
        "path": path,
        "method": request.method,
        "query_params": dict(request.query_params),
        "headers": dict(request.headers),
        "body": body_json
    }