#Calculator
num_1,operator,num_2 = input('enter numbers :').split()
#print(num_1,operator,num_2)
num_1=int(num_1)
num_2=int(num_2)
sum_1=num_1+num_2
diff=num_1-num_2
mul=num_1*num_2
quo=num_1/num_2
rem=num_1%num_2
# put the calculator condition here
if operator == '+':
    print('{} + {} = {}'.format(num_1,num_2,sum_1))
elif operator == '-':
    print('{} - {} = {}'.format(num_1,num_2,diff))
elif operator == '*':
    print('{} * {} = {}'.format(num_1,num_2,mul))
elif operator == '/':
    print('{} / {} = {}'.format(num_1,num_2,quo))
elif operator == '%':
    print('{} % {} = {}'.format(num_1,num_2,rem))
else:
    print('no proper operator was given')


