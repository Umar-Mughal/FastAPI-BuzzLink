from fastapi import FastAPI

app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "hello world"}


@app.get("/")
def hello_world():
    return "hello wod"