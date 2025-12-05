from fastapi import FastAPI
from .routes import router

app = FastAPI(title="FastAPI Mini API", description="Simple microservice boilerplate")

app.include_router(router)

@app.get("/ping")
def ping():
    return {"msg": "pong"}
