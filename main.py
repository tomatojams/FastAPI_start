from fastapi import FastAPI
from fastapi.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

joy = FastAPI()

origins = ["http://localhost:5173"]

joy.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

  
@joy.get("/")
async def root():
    return FileResponse("index.html")


@joy.get("/hello")
async def hello():
    return {"message": "안녕하세요 파이보"}


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
