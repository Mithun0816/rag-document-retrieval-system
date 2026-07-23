from fastapi import FastAPI
import uvicorn
from migrations.migration import Migration
from routers.router import router as kb_router
from routers.router import router as search_router


app=FastAPI(
    title="Gym consultation rag api",
    description=" RAG API for fym consultation knowledge base and search",
    version=1.0
)

@app.on_event("startup")
async def startup_event():
    """Run migrations and seed data on application startup"""
    migration = Migration()
    migration.run_startup_migration()
    
    

app.include_router(kb_router)
app.include_router(search_router)

if __name__ == "__main__":
    
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
        log_level="info"
    )