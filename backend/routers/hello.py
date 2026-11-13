from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

router = APIRouter(prefix="/api", tags=["hello"])

class HelloRequest(BaseModel):
    name: Optional[str] = None
    timestamp: Optional[datetime] = None

@router.get("/hello")
async def get_hello():
    """Simple hello endpoint for testing"""
    return {"message": "Hello from DeepTutor API!", "status": "success"}

@router.post("/hello")
async def post_hello(request: HelloRequest):
    """Post hello with optional name parameter"""
    name = request.name or "World"
    timestamp = request.timestamp or datetime.now()
    
    return {
        "message": f"Hello, {name}!",
        "timestamp": timestamp.isoformat(),
        "status": "success"
    }

@router.get("/greet/{name}")
async def greet_name(name: str):
    """Personalized greeting endpoint"""
    if not name.strip():
        raise HTTPException(status_code=400, detail="Name cannot be empty")
    
    return {
        "message": f"Hello, {name}!",
        "length": len(name),
        "status": "success"
    }
