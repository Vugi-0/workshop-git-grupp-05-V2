from calculator import add, sub

def run():
    print("1) Add\n2) Substract\n3) Multiply\n4) Divide\n0) Exit Program")

choice = input("Select: ")

if choice == "1": print("TODO Add")
a = float(input("a: "))
b = float(input("b: "))

if choice == "2": print(sub (a, b))


