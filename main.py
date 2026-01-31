from fastapi import FastAPI
import crud 
app = FastAPI() 

@app.get("/products/")
def get_products():
    return crud.get_all_products()  
          
@app.put("/products/{id}")
def change_price(id: int, price: int):
    return crud.update_price(id, price)

@app.delete("/products/{id}")
def delete_product(id: int):
    return crud.delete_product(id)  