from fastapi import FastAPI, HTTPException
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL")

app = FastAPI()

@app.get("/search")
async def search(query: str):
    async with httpx.AsyncClient() as client:
        auth_response = await client.get(AUTH_SERVICE_URL + "/auth/health")
        if auth_response.status_code != 200:
            raise HTTPException(status_code=500, detail="Auth service is down")
    return {"results": f"Search results for '{query}'"}


@app.get("/health")
def health_check():
    return {"status": "service  search running"}
