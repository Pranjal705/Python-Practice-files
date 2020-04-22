#Dictionaries

something={
'a':'jkl',
'b': 2 ,
'c': 3 ,
'd': 4
}

print(something['a'][0])

print(something.items())#it gives the list of all the items in the dictionary in tupled form inside.

print('a' in something.keys())#it checks if the given key is in the dictionary or not

print('jkl' in something .values())#it checks if the given value is in the dictionary or not


print(something.clear())#it clears the dictionary but does not return the value
print(something)

something2={
'greet':'hello',
'name':'Pranjal'
}
print(something2.pop('greet'))#it pops out particular item and also returns the value
print(something2)



something3=something2.copy()#it copies the dictionary
print(something3)

something2.update({'greet':'Hi'})
print(something2)


#Loopin in dictionaries
for item in something2.items():
    print(item)

for item in something2.keys():
    print(item)

for item in something2.values():
    print(item)
