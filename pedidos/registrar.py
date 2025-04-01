from sqlmodel import Session
from db import db
from db.modelos import pedidos, productos_pedidos
from pydantic import BaseModel

class item_en_pedido(BaseModel):
    producto_id: str
    cantidad: int

class pedido_a_registrar(BaseModel):
    cliente_id: str
    productos: list[item_en_pedido]
    
def registrar_nuevo_pedido(pedido: pedido_a_registrar):
    with Session(db) as session:
        nuevo_pedido = pedidos()
        session.add(nuevo_pedido)
        session.commit()
        session.refresh(nuevo_pedido)
        for item in pedido.productos:
            nuevo_producto_pedido = productos_pedidos(producto_id = item.producto_id ,pedido_id = nuevo_pedido.id, cantidad = item.cantidad)
            session.add(nuevo_producto_pedido)
            session.commit()
        return nuevo_pedido
    
