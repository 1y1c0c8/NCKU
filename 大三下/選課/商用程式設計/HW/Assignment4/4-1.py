element = [1,2,3,4,5,6,7,8,9]
targetLen = len(element)

# mul:1~9
for mul in range(1, 10):
# index:0~8
    for index in range(0, targetLen):
        target = element[index] * mul
        if target < 10:
            print(target, end=" \t")
        else:
            print(target, end="\t")
    print("\n")
