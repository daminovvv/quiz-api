import uvicorn
from fastapi import FastAPI

from src.api.routers import routers

app = FastAPI()
app.include_router(routers)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app)
