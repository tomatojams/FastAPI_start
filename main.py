from fastapi import FastAPI
app = FastAPI()

from fastapi.responses import FileResponse

@app.get("/")
async def root():
    return FileResponse('index.html')


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

from pydantic import BaseModel

class UsrData(BaseModel):
    name: str
    phone :str

@app.get("/send")
async def send(data:UsrData):
    print(data)
    return  '전송완료'
