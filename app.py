from calculator import add, sub, mul, div

def run():
    print("1) Add\n Subtract\n0) Exit")

choice = input("Select: ")

if choice == "1": print("TODO Add")
a = float(input("a: "))
b = float(input("b: "))

if choice == "2": print(sub (a, b))

if choice == "3": print(mul (a, b))

if choice == "4": print(div (a, b))