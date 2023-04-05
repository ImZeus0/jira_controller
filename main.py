import os
import pathlib
from modules.jira.endpoints import router
import uvicorn as uvicorn
from fastapi import FastAPI, Request

app = FastAPI()

app.include_router(router, prefix='/jira')


@app.post('/')
async def root(request: Request):
    return {"message": "Hello World app"}


if __name__ == '__main__':
    cwd = pathlib.Path(__file__).parent.resolve()
    uvicorn.run('main:app', port=3000, host='0.0.0.0', reload=True)
