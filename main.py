from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from middlewares.error_handler import ErrorHandler
from routers.auth import auth_router
from routers.product import product_router
from config.database import engine, Base

#Se crea la instancia
app = FastAPI()
app.title = "Catálogo de productos"
app.version = "3.0.0"


app.add_middleware(ErrorHandler)
app.include_router(product_router)
app.include_router(auth_router)
Base.metadata.create_all(bind=engine)

# Primer endpoint 
@app.get("/", tags=['home']) # Ruta de inicio
def message():
    return HTMLResponse(content="<h1> Catálogo de productos </h1>")
