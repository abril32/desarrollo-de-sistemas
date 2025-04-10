from contextlib import asynccontextmanager
from fastapi import FastAPI
from db import create_db_and_tables

@asynccontextmanagers
async def Iniciar_app(app: FastAPI):
    print("Inicia la app")
    create_db_and_tables()
    yield
    print("Cierra app")

app= FastAPI(lifepan=Iniciar_app)
