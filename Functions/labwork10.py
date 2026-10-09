def display_product(**kwargs):
    
    name = kwargs["name"]
    price = kwargs["price"]
    quantity = kwargs["quantity"]

    total = price * quantity

    return f"Product: {name}\nPrice: ₹{price}\nQuantity: {quantity}\nTotal Cost: ₹{total}"
        
print(display_product(name="keyboard",price=899,quantity=3))