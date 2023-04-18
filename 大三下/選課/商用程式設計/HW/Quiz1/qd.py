# sequential data (temperature)

tempList = ['29.0', '31.5', '32.1', '21', '30.6']

tempToday = float(input("Please enter today's temperature: "))
tempList.append(tempToday)

print("Today's temperature is " + str(tempToday))

len=1
for temp in tempList:
    print("[" + str(len) + "] " + str(float(temp)))
    len = len+1
print("There are " + str(len-1) + " temperature records in the tempList")