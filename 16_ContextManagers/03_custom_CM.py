class MyContext:
    def __enter__(self):
        print("Entering context")
        return "Resource"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")

# Usage
with MyContext() as resource:
    print("Using", resource)