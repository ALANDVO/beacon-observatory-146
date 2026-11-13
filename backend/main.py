from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
import os

app = FastAPI(
    title="DeepTutor API",
    description="AI-powered personalized tutoring system",
    version="0.1.0"
)

# Security middleware
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["localhost", "127.0.0.1"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import and include routers
from backend.routers.hello import router as hello_router
app.include_router(hello_router)

# Mount static files for frontend (use correct relative path)
src_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "src")
app.mount("/static", StaticFiles(directory=src_dir), name="static")

@app.get("/")
async def root():
    return {"message": "Welcome to DeepTutor API", "version": "0.1.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": "2026-11-13T06:25:00Z"}

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"error": exc.detail, "status_code": exc.status_code}, exc.status_code

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
