# Scope and Name Resolution
# Local: Inside a function
# Enclosing: From outer function if nested 
# global: top level script/module
# Built-in:  like the print()

loyalty_points = 0

def process_transactions(transactions: list[int]) -> int:
    total = 0
    for amount in transactions:
        total += amount
    
    def apply_bonus() -> int:
        nonlocal total
        if total > 1000:
            return total + 50
        else:
            return total
    
    total = apply_bonus()
    global loyalty_points
    loyalty_points += total // 100
    
    return total

# *args, **kwargs
def generate_invoice(customer_name: str = "Guest", *items: str, **charges: float) -> str:
    total_amount = 0.0
    invoice_line = [f"Invoice for {customer_name}:"]
    if items:
        print("Items:\n")
        for item_name in items:
            invoice_line.append(f"- {item_name}")
            
    if charges:
        invoice_line.append("Charges:\n")
        for name, value in charges.items():
            invoice_line.append(f"{name.capitalize()}: {value}")
            total_amount += value
    invoice_line.append(f"Total Amount Due: {total_amount}")
    
    return "\n".join(invoice_line)

# Types of Functions:

# Pure vs Impure
# Pure = no side effects at all
# → no changing globals
# → no printing
# → no reading files
# → no randomness
# → always same output for same input

# Impure = any side effect
# → modifying globals
# → printing
# → writing files
# → using random
# → using time
# → reading user input
# → network calls

# Recursive Functions
# Lambdas(Anonymous function)
def pure_add(a: int, b: int) -> int:
    return a + b
    
counter = 0

def impure_increment() -> int:
    global counter
    counter += 1
    return counter
    
def factorial_recursive(n) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)
        
def square_list(nums: list[int]) -> list[int]:
    return list(map(lambda n: n ** 2, nums))

