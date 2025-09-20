length = int(input("Enter the size of the pattern:"))
row = 0

while row < length:
    for column in range(1,length + 1):
        print('*',end = '')
    
    print()
    row += 1