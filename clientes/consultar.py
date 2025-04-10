from sqlmodel import Session, select
from db import db
from db.modelos import pedidos

def consultar_pedidos(cliente_id: str):
    with Session(db) as session:
        consulta = select(pedidos).where(pedidos.cliente_id == cliente_id)
        Pedidos = session.exec(consulta)
        return Pedidos
    