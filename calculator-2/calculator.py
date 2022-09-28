"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

print('Welcome to our calculator.')
print('Enter the letter s whenever you wish to exit.')

while True:
    
    user_input = input('Enter your equation: ')
    tokens = user_input.split(' ')
    func = tokens[0]
    num1 = float(tokens[1])

    #lst = ['+','-','*','/','** 2','** 3','** num2',"%"]
    
    #if "s" in tokens:
        #print('Goodbye')
        #break

    if len(tokens) < 2:
        print('ERROR. Not enough values.')
        continue

    if len(tokens) < 3:
        num2 = "0"

    else:
        num2 = float(tokens[2])

    if len(tokens) > 3:
        num3 = tokens[3]

    elif func == '+':
        sum = add(num1,num2)
        print(sum)
        
    elif func == '-':
        sum = subtract(num1,num2)
        print(sum)
    
    elif func == '*':
        sum = multiply(num1,num2)
        print(sum)
    
    elif func == '/':
        sum = divide(num1,num2)
        print(sum)

    elif func == 'pow':
        sum = pow(num1, num2)
        print(sum)

    elif func == 'mod':
        sum = mod(num1,num2)
        print(sum)

    elif func == 'cube':
        sum = cube(num1)
        print(sum)

    elif func == 'square':
        sum = square(num1)
        print(sum)
