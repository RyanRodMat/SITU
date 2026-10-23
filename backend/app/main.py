#importa as bibliotecas necessárias
from fastapi import FastAPI
from pydantic import BaseModel

#declara uma referência ao nosso app
app = FastAPI()

#chama o método HTTP GET na URL base
@app.get("/")
def home():
    return {"mensagem: Página principal"}

#chama o GET no path /trotes
@app.get("/trotes")
def buscarTrote():
    return{"mensagem: Página dos trotes"}