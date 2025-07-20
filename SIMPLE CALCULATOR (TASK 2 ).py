def calculator():
    print("\nSIMPLE CALCULATOR")
    print("Operations available:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exponentiation (**)")
    
    while True:
        try:
            
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Enter operation (+, -, *, /, %, **): ").strip()
            
            
            if operation == '+':
                result = num1 + num2
                print(f"Result: {num1} + {num2} = {result}")
            elif operation == '-':
                result = num1 - num2
                print(f"Result: {num1} - {num2} = {result}")
            elif operation == '*':
                result = num1 * num2
                print(f"Result: {num1} * {num2} = {result}")
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero!")
                else:
                    result = num1 / num2
                    print(f"Result: {num1} / {num2} = {result}")
            elif operation == '%':
                if num2 == 0:
                    print("Error: Division by zero!")
                else:
                    result = num1 % num2
                    print(f"Result: {num1} % {num2} = {result}")
            elif operation == '**':
                result = num1 ** num2
                print(f"Result: {num1} ** {num2} = {result}")
            else:
                print("Invalid operation! Please enter one of: +, -, *, /, %, **")
            
            # Ask if user wants to perform another calculation
            again = input("\nPerform another calculation? (y/n): ").lower()
            if again != 'y':
                print("\nThank you for using the calculator!")
                break
                
        except ValueError:
            print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    calculator()
