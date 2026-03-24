# Simple console calculator


from calculator import add, sub

def run():
    print("1) Add\n Subtract\n0) Exit")

choice = input("Select: ")

if choice == "1": print("TODO Add")
a = float(input("a: "))
b = float(input("b: "))

if choice == "2": print(sub (a, b))