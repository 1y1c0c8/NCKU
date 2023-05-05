ans = ''

fruits = []
ans = raw_input('Please enter your favorite fruit:')
while ans != 'banana':
    if len(fruits)==0 :
        fruits.append(ans)
    elif (ans not in fruits):
        fruits.append(ans)
    ans = raw_input('Please enter your favorite fruit:')
fruits.append('banana')

str_ans=''
length = len(fruits)
index=0
while index < length-1:
    str_ans += fruits[index]
    str_ans += ', '
    index+=1

str_ans += fruits[index]

print('There are ' + str(length) + ' kinds of fruits you love, including [' + str_ans + ']')
