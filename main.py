from fastapi import FastAPI
from fastapi.responses import FileResponse

from pydantic import BaseModel

joy = FastAPI()


@joy.get("/")
async def root():
    return FileResponse("index.html")


@joy.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


class UsrData(BaseModel):
    name: str
    phone: str


@joy.get("/send")
async def send(data: UsrData):
    print(data)
    return "전송완료"
