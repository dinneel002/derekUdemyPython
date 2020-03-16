samp_string = "This is a very important string  "
#print(samp_string.lstrip())
print("Uppercase :",samp_string.upper())
print("Lowercase :",samp_string.lower())
a_list = samp_string.split()
for i in a_list:
    print(i)
print("How many ts?:",samp_string.count('is'))
print("String Index :",samp_string.find('string'))
print("Replace very :",samp_string.replace(' very',' kind of'))
letter_z = "z"
print('Is "z" a letter or number :', letter_z.isalnum())
print('Is "z" a letter :', letter_z.isalpha())
print('Is "z" a number :',letter_z.isdigit())
print('Is "z" a space :',letter_z.isspace())


a_list = ["Bunch", "of", "random", "words"]
print(" ".join(a_list))