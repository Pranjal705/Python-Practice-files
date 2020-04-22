#check for the duplicates in the list.
some_list = ['a','b','c','b','d','m','n','n']
duplicates=[]
for item in some_list:
    if some_list.count(item)>1:
        if item not in duplicates:
            duplicates.append(item)
print(duplicates)

#codesdope level 1 questions

#Take inputs from user to make a list. Again take one input from user and search it
#in the list and delete that element, if found. Iterate over list using for loop.
    
A=[]
n=int(input('enter the no. of elements u want in the list'))
for i in range(1,n+1):
      value=int(input('enter the value u want in the list: '))
      A.append(value)
print(A)
element=int(input('enter the element you want to search'))
for item in A:
    if item==element:
        A.remove(item)
print(A)

#You are given with a list of integer elements.
#Make a new list which will store square of elements of previous list.

numbers=[1,2,3,4,5,6]
s=[]
for number in numbers:
    number=number*number
    s.append(number)
print(s)

#Using range(1,101), make two list,
#one containing all even numbers and other containing all odd numbers.
J=list(range(1,101))
even=[]
odd=[]
for e in J:
    if e%2==0:
        even.append(e)
    else:
        odd.append(e)
print(even)
print(odd)

#From the two list obtained in previous question, make new lists,
#containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9
#in separate lists.


three=[]
four=[]
five=[]
six=[]
seven=[]
eight=[]
nine=[]
ten=[]
for integer in J:
    if integer%3==0:
        three.append(integer)
    elif integer%4==0:
        four.append(integer)
    elif integer%5==0:
        five.append(integer)
    elif integer%6==0:
        six.append(integer)
    elif integer%7==0:
        seven.append(integer)
    elif integer%8==0:
        eight.append(integer)
    elif integer%9==0:
        nine.append(integer)
    else:
        ten.append(integer)
print(three)
print(four)
print(five)
print(six)
print(seven)
print(eight)
print(nine)
print(ten)

#From a list
#containing ints, strings and floats, make three lists to store them separately


anything=['pranjal',5,5.0]
n=[]
f=[]
s=[]
for something in anything:
    if type(something)==str:
        s.append(something)
    elif type(something)==int:
        n.append(something)
    elif type(something)==float:
        f.append(something)
print(s)
print(n)
print(f)

#take two inputs from the user and if they are integer add them if not
#say invalid input
x=input('enter the first value')
y=input('enter the second value')
if x.isnumeric() and y.isnumeric():
    x=int(x)
    y=int(y)
    print(x+y)
else:
    print('invalid inpput')

#print a list of multiples of 14 using the list of multiples of 12
li=[12,24,36,48,60,72,84,96,108,120]
f=[]
m=0
for v in li:
    m=m+2
    v=v+m
    f.append(v)
print(f)

#Codesdope level 2 questions

#Using range(1,101), make a list containing only prime numbers.

    
        
        






















    
