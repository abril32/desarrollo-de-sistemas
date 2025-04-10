from fastapi import FastAPI
from clientes.registrar import registrar_nuevo_cliente
from db import create_db_and_tables
from db.modelos import clientes, pedidos, productos
from db.pedidos.registrar import registrar_nuevo_pedido
from productos.produc import registrar_nuevo_producto
from clientes.consultar import consultar_pedidos
import requests

url = 'https://127.0.0.1:8000'

try:
    response = requests.get(url)
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        print("La solicitud fue exitosa.")
    else:
        print(f"Recibí un código de estado {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Hubo un error al hacer la solicitud: {e}")


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

@app.get("/pedidos/{cliente_id}")
def get_pedidos(cliente_id: str):
    pedido =  consultar_pedidos(cliente_id)
    return {"pedidos": pedido}