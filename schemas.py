from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class OrderStatus(str, Enum):
    pending = "Pendiente"
    preparing = "En preparación"
    ready = "Listo"
    delivered = "Entregado"

class UserRole(str, Enum):
    client = "Cliente"
    admin = "Administrador"

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    role: UserRole

    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    status: OrderStatus
    user_id: int

class OrderCreate(OrderBase):
    pass

class OrderOut(OrderBase):
    id: int

    class Config:
        orm_mode = True
