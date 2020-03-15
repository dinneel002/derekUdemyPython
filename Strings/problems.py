norm_string = input('Enter a string to hide in upper case:')
sect_string=''
for char in norm_string:
    sect_string+=str(ord(char)-23)
print(sect_string)
norm_string=''
for i in range(0,len(sect_string)-1,2):
    char_code = sect_string[i]+ sect_string[i+1]
    norm_string+= chr(int(char_code)+23)
print(norm_string)