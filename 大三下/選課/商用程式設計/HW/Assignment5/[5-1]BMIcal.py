def BMI():
    # BMI calculator

    height = float(input("Please enter your height: "))
    weight = float(input("Please enter your weight: "))

    BMI_val = weight / (height ** 2)
    # print(BMI_val)
    BMI_val = float(int(BMI_val*100)/100)

    print("# BMI(%2f): " + str(BMI_val))

BMI()