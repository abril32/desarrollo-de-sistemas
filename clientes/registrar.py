from sqlmodel import Session
from db import db
from db.modelos import clientes


def registrar_nuevo_cliente(cliente: clientes):
    with Session(db) as session:
        session.add(cliente)
        session.commit()
        session.refresh(cliente)
        return cliente
    


