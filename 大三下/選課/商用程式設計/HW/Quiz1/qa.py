# 

numA = int(input("Please enter A's score:"))
numB = int(input("Please enter B's score:"))

if numA > numB :
    print("A is greater than B")
elif numA < numB:
    print("B is greater than A")
else:
    print("A is equal to B")

print("A* B = " + str(numA * numB) + "\nA is " + str(numA) + " ,B is " + str(numB))