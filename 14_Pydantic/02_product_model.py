# Always use type annotation
# Always use the appropriate type
# like the int, float, str, bool etc
# set a sensible default
# Pydantic will always try to do this - 
# "123" -> 123
# "true" -> True
# 123 -> 123.0


from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

# in above we have designed a model

product_one = Product(id=1, name="Laptop", price=999.99, in_stock=True)

product_two = Product(id=2, name="Mouse", price=100)

product_three = Product(name="keyboard")