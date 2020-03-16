rand_string = "   this is an import string   "
rand_string = rand_string.lstrip()
rand_string = rand_string.rstrip()
print(rand_string)

# capitalizing a string
print(rand_string.capitalize())
print(rand_string.upper())

a_list=["Bunch","of","random","words"]
print(" ".join(a_list))

for i in a_list:
    print(i)
a_list2=rand_string.split()
print(a_list2)

print("How many is :",rand_string.count('an'))

print(rand_string.find('an'))
print(rand_string.replace(' an',' a kind of'))