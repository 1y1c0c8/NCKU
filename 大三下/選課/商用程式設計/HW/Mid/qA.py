totalVal = 0
index=4
with open('content.txt', 'r') as f:
    while index>0:
        totalVal += int(f.readline())
        index -= 1
print('Sum: ' + str(totalVal))
