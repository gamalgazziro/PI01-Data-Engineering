from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class BaseModel:
    titulo: str
    autor: str
    

#esta es la ruta raíz
@app.get('/')
def index():
    return "holiwis"

@app.get('/libros/{id}')
def mostrar_libro(id):
    return{'data':id}
