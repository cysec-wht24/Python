def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        cost = price * quantity
        print(f"total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not on menu")
    except TypeError:
        print("Quantity must be in number")

process_order("ginger", 2)
process_order("masala", "two")

# custom exceptions 
def brew_chai(flavor):
    if flavor not in ["masala", "ginger", "elaichai"]:
        # raise keyword is to manually (raise)trigger exceptions
        # https://docs.python.org/3/tutorial/errors.html#raising-exceptions
        raise ValueError("Unsupported chai flavor...")
    print(f"brewing {flavor} chai...")


brew_chai("mint")

class OutOfIngredientsError(Exception):
    pass

def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Missing milk or sugar")
    print("chai is ready...")


make_chai(0, 1)