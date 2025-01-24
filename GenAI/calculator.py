#abhi45
#Math assignment:
#================================

#code for addition of two numbers
#--------------------------------

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 == 0:
        return "Division by zero not allowed."
    return num1 / num2

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

while True:
    print("\nChoose an Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    selection = input("Enter your choice: ")

    match selection:
        case "1": 
            result = add(num1, num2)
            print(f"Your addition of {num1} and {num2} is: {result}")
        case "2":    
            result = sub(num1, num2)
            print(f"Your subtraction of {num1} and {num2} is: {result}")
        case "3": 
            result = mul(num1, num2)
            print(f"Your multiplication of {num1} and {num2} is: {result}")
        case "4": 
            result = div(num1, num2)
            print(f"Your division of {num1} and {num2} is: {result}")
        case "5":
            print("Exiting from program.")
            break
        case _: 
            retry = input("You have entered a wrong choice. Do you want to continue? (Y/N): ")
            if retry.lower() == 'y': 
                continue
            else:
                break

print("Thanks! We are offline now.")

