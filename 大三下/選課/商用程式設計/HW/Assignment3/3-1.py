num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))
operator = input("Choose an operator(add/sub/mul/div) and enter the name:\n")

if(operator == "add"):
    print(num1 + num2)
elif(operator == "sub"):
    print(num1 - num2)
elif(operator == "mul"):
    print(num1 * num2)
elif(operator == "div"):
    print(num1 / num2)
else:
    input("You have enter some fault value...")