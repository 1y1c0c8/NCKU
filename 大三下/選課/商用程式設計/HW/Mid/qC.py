import string

def calculator():
    numA = int(raw_input('Please enter the first number.'))
    numB = int(raw_input('Please enter the second number.'))

    op = str(raw_input('Please enter the operation symbol.'))
    if op=='+':
        result = numA + numB
        print('Ans: ' + str(result))
    elif op=='-':
        result = numA - numB
        print('Ans: ' + str(result))
    elif op=='*':
        result = numA * numB
        print('Ans: ' + str(result))
    elif op=='/':
        result = numA // numB
        print('Ans: ' + str(result))

calculator()