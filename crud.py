from db import users, products
current_user = users[2] 

def get_products():
    return products
def get_buyer_products():
    if current_user["role"] != "buyer":
        return "icazen yoxdur"
    return current_user["products"]

def update_price(product_id, new_price):
    if current_user["role"] != "seller":
        return "yalniz seller ede biler"

    for p in products:
        if p["id"] == product_id:
            p["price"] = new_price
            return p

    return "product tapilmadi"


def delete_product(product_id):
    if current_user["role"] not in ["admin", "seller"]:
        return "icazen yoxdur"

    global products
    products[:] = [p for p in products if p["id"] != product_id]
    return "product silindi"