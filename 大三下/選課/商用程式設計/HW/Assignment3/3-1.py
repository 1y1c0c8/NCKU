do=True
while do:
    val1=int(input("Enter first number: "))
    val2=int(input("Enter second number: "))

    keep_checking=True
    while keep_checking:
        opr=input("Enter add/minus/mul/div to calculate the two number above")

        if opr=="add":
            print(val1+val2)
        elif opr=="minus":
            print(val1-val2)
        elif opr=="mul":
            print(val1*val2)
        elif opr=="div":
            print(round(val1/val2, 2))
        keep_checking=False
    do=input("Do you want to try again?(True/False)")
    do=do.lower()
    if do=="true":
        do=True
    else:
        do=False