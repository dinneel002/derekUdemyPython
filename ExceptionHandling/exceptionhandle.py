while True:
    try:
        number = int(input('enter the number :'))
        break
    except ValueError:
        print("You didn't enter a number")
    except:
        print('an unknown error occured')
print('thanks for the number')