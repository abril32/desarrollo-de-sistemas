from fastapi import FastAPI
from clientes.registrar import registrar_nuevo_cliente
from db import create_db_and_tables
from db.modelos import clientes, pedidos, productos
from pedidos.registrar import registrar_nuevo_pedido
from productos.produc import registrar_nuevo_producto

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok"}

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/clientes")
def post_clientes(cliente: clientes):
    return registrar_nuevo_cliente(cliente)

@app.post("/pedidos")
def post_pedidos(pedido:pedidos):
    return registrar_nuevo_pedido(pedido)

@app.post("/productos")
def post_productos(producto:productos):
    return registrar_nuevo_producto(producto)