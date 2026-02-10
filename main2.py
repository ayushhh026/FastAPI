from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Product(BaseModel):
        id: int
        name: str 
        description: str 
        price: float 
        quantity: int 

products = [
    Product(
        id=1,
        name="phone",
        description="budget phone",
        price=99,
        quantity=10
    ),
    Product(
        id=2,
        name="laptop",
        description="gaming laptop",
        price=999,
        quantity=6
    )
]

@app.get("/")
def greet():
    return "Welcome to the server"

@app.get("/product")
def get_all():
    return products

@app.get("/product/{id}")
def get_product_by_id(id : int):
    for product in products:
        if product.id==id:
            return product
      
    return "product not found"

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product


@app.put("/product")
def update_product(id: int,product: Product):
    for i, p in enumerate(products): # enum creates a list of two items (index,value)
        if p.id == id:
            products[i]=product
            return "Product added successfuly"
    return "No product found"

@app.delete("/product")
def delete_product(id:int):
    for i, p in enumerate(products): # enum creates a list of two items (index,value)
        if p.id == id:
            del products[i]
            return "product deleted"
    return "Product not found"