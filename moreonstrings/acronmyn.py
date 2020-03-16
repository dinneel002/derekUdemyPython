original_string = input('convert to acronmy :')
original_string=original_string.upper()
list_of_words = original_string.split()
for word in list_of_words:
    print(word[0],end="")
print()