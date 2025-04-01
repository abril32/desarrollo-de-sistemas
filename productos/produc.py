from sqlmodel import Session
from db import db
from db.modelos import productos

def registrar_nuevo_producto(producto: productos):
    with Session(db) as session:
        session.add(producto)
        session.commit()
        session.refresh(producto)
        return producto
    