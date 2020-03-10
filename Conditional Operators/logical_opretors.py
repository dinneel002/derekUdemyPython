# and : if both are true it returns true
#or : if either are true it returns true
#not : converts true into false and vice versa

age = int(input('enter age:'))
if (age >= 1 and age <= 18):
    print('this is an important bday')
elif (age == 21 or age == 50):
    print('imp bday')
elif not age < 65:
    print('imp bday...')
else:
    print('sorry not imp bday')