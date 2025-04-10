from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
import uuid

class pedidos(SQLModel, table=True):
    id: str  = Field(default=str(uuid.uuid4()), primary_key=True)
    estados: str = Field(default="Pendiente")#estados son pendiente, enviado, entregado

class clientes(SQLModel, table=True):
    id: str  = Field(default=str(uuid.uuid4()), primary_key=True)

class productos(SQLModel, table=True):
    id: str  = Field(default=str(uuid.uuid4()), primary_key=True)
    nombre: str 

class productos_pedidos(SQLModel, table=True):
    id: str  = Field(default=str(uuid.uuid4()), primary_key=True)
    producto_id: str = Field(foreign_key="productos.id")
    pedido_id: str = Field(foreign_key="pedidos.id")
    cantidad: int 
# Code below omitted 👇