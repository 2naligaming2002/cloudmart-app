from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from datetime import datetime
from app.database import products_container

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return FileResponse("static/index.html")

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "database": "connected",
        "cosmos_endpoint": "connected",
        "timestamp": datetime.utcnow().isoformat()
    }

@app.get("/api/v1/products")
def get_products():
    return list(products_container.read_all_items())

@app.get("/api/v1/products/{product_id}")
def get_product(product_id: str):
    items = list(products_container.read_all_items())
    for item in items:
        if item["id"] == product_id:
            return item
    return {"error": "Product not found"}

@app.get("/api/v1/categories")
def get_categories():
    items = list(products_container.read_all_items())
    return list(set(item["category"] for item in items))
