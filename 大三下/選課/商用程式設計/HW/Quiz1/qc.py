# BMI calculator

height=1.6
weight = float(input("Please enter your weight: "))

BMI = weight / (height ** height)
#print(BMI)
BMI = float(int(BMI*100)/100)
# print("# BMI(%2f): " + str(BMI))

if (BMI<18.5):
    print("Underweight")
elif (BMI>=18.5 and BMI<24.0):
    print("Normal")
elif (BMI>=24):
    print("Overweight")
print("# BMI(%2f): " + str(BMI))
