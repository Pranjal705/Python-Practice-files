basket=[1,2,3,4,5]
print(basket)

print(max(basket))
print(min(basket))

#adding

basket.append(100)
print(basket)

basket.insert(6,101)
print(basket)

basket.extend([102,103])
print(basket)

#removing

basket.pop() #it pops out the last element of the list
print(basket)

basket.pop(5)#it removes the item of the 5th index
print(basket)

basket.remove(1)#it removes the item 1
print(basket)

basket.clear() #it clears all the elements from the list
print(basket)

alphabets = ['a','x','b','c','d','e','d']
print(alphabets)

print(alphabets.index('a')) #it gives the index of the item in the list

print('d' in alphabets) #it tells if the element is in the list or not

new_alphabets=alphabets.sort()#sorts the list but does not return the value
print(alphabets)
print(new_alphabets)

new_alphabets=sorted(alphabets)#sorts  the list and also returns the value
print(alphabets)
print(new_alphabets)

new_alphabets.reverse()#it reverses the value but not return it
print(new_alphabets)

print(new_alphabets[::-1])#it is the method of reversing the elements by slicing

print(list(range(1,101)))
sentence=['hi','my','name','is','Pranjal']
new_sentence='!'.join(sentence)#it adds the string in each item of the list
print(new_sentence)


#list unpacking

a,b,c, *other,d=[1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
print(d)

#Looping in Lists
s=0
my_list=[1,2,3,4,5,6,7,8,9]
for item in my_list:
    s+=item
print(s)






























