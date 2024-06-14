# Create class and 4 functions of arithmetic operations and use it

class Demo:
    def __init__(self):
        pass

    def add(self, a, b):
        print(a + b)

    def sub(self, a, b):
        print(a - b)

    def multi(self, a, b):
        print(a * b)

    def div(self, a, b):
        print(a / b)

obj = Demo()

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Select operation: ")
print("1.Add")
print("2.Sub")
print("3.Multi")
print("4.Div")

choice = int(input("Enter choices: "))

if choice == 1:
    print(obj.add(a,b))

elif choice == 2:
    print(obj.sub(a,b))

elif choice == 3:
    print(obj.multi(a,b))

else:
    print(obj.div(a,b))





