i = 1
while i <= 10:
    if (i%2)==0:
        i+=1
        continue
    if i== 9:
        break
    print('odd :',i)
    i +=1