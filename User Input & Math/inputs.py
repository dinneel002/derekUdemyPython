#name=input('what is ur name: ')
#print('hi',name)

num_1,num_2=input('enter 2 numbers :').split(',')
#print(num_1,num_2)
num_1=int(num_1)
num_2=int(num_2)
sum_1=num_1+num_2
diff=num_1-num_2
mul=num_1*num_2
quo=num_1//num_2
rem=num_1%num_2

print('{} + {} = {}'.format(num_1,num_2,sum_1))
print('{} - {} = {}'.format(num_1,num_2,diff))
print('{} * {} = {}'.format(num_1,num_2,mul))
print('{} / {} = {}'.format(num_1,num_2,quo))
print('{} % {} = {}'.format(num_1,num_2,rem))


