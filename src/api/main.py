from fastapi import FastAPI
import datetime

from api.v1.todo.router import router as todo_router

app = FastAPI()


@app.get("/ping")
async def ping():
    return {
        "message": "pong",
        "timestamp": datetime.datetime.now(datetime.timezone.utc),
    }


app.include_router(todo_router, prefix="/api/v1/todo", tags=["todo"])
