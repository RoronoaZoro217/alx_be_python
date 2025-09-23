def perform_operation(num1, num2, operation):
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 == 0:
                print('Cannot divide by zero')
                return 0
            else:
                return num1 / num2
        case _:
            print('Invalid operation')
            return 0

            

