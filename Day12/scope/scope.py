# Global scope
variable = 10

def func():
    # Local scope
    variable = 5
    print(f"Local scope: {variable}")

func()
print(f"Global scope: {variable}")
