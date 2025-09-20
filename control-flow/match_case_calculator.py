num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")
result = 0

match operation:
    case '+':
        result = num1 + num2
        print('The result is',result)
    case '-':
        result = num1 - num2
        print('The result is',result)
    case '*':
        result = num1 * num2
        print('The result is',result)
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print('The result is',result)