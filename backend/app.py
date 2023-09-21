from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from api.api_router import api_router



app = FastAPI()

origins = [
    "http://localhost:3000",
]
app = FastAPI(openapi_url=f"/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router, prefix="")



