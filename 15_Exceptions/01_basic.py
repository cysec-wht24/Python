# Types of Error:
# Index Error
# key Error
# Zero Division Error
# Type Error
# Name Error

chai_menu = {"masala": 30, "ginger": 40}

try:
    chai_menu["elaichi"]
except KeyError:
    print("The key that you are tying to access does not exists")


print("Hello chai code")

def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError("We don't know that flavor")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavor} chai is served")
    finally:
        print("Next customer please")

serve_chai("masala")
serve_chai("unknown")