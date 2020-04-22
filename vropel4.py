#Polynomial Addition
#Write an algorithm and the subsequent Python program to add the two given polynomials. Assume that the coefficients of each polynomial are stored in a separate list.

#Eg: 4x3 + 3x + 1 can be stored as [4,0,3,1]

#2x2 - 3x - 4 can be stored as [2,-3,-4]

#Output is [4, 2, 0, -3]

#Input Format:

#First line contains the degree of the first polynomial

#Next line contains the coefficient of xn

#Next line contains the coefficient of xn-1

#...

#Next line contains the coefficient of x0

#Next line contains the degree of the second equation

#Next line contains the coefficient of xn

#Next line contains the coefficient of xn-1

#...

#Next line contains the coefficient of x0

#Output Format:

#Coefficients as a list from the highest degree to the lowest degree



d1=int(input('enter the degree of first equation'))
list1=[]
for i in range(d1+1):
    c=int(input('enter the coefficient'))
    list1.append(c)
print(list1)
d2=int(input('enter the degree of second equation'))
list2=[]
for i in range(d2+1):
    c1=int(input('enter the coefficient'))
    list2.append(c1)
print(list2)
if len(list1)!=len(list2):
    if len(list2)<len(list1):
        x=len(list1)-len(list2)
        for i in range(x):
            list2.insert(0,0)
    elif len(list1)<len(list2):
        y=len(list2)-len(list1)
        for i in range(y):
            list1.insert(0,0)
print(list1)
print(list2)
list1.reverse()
list2.reverse()
list3=[]
for i in range(len(list1)):
    sum2=list1[i]+list2[i]
    list3.append(sum2)
list3.reverse()
print(list3)
        



#Creating Unique List and Searching
#A login register is maintained in a library in which,
#the register number of students are recorded when they enter the library. Sometimes it happens that the students
#visit the library more than once in a day and hence duplicate entries occur so frequently in the register.
#The librarian wants to have a report of all students who have visited on a particular day, ‘x’.
#Given the list  of students who visited the library on the day ‘x’, write an algorithm and the subsequent Python program
#to prepare a report with unique register number of students. Also read a register number ‘r’ and search for it in the list.
#Print ‘Found’ if ‘r’ is in the list and print ‘Not found’ otherwise.

#Input Format:

#First line contains the number of students visited, ‘n’

#Second line contains the register number of first entry

#Third line contains the register number of second entry

#. . .

#N+1th line contains the register number of n-th entry

#Next line contains the register number  ‘r’ that has to be searched

#Output Format:

#A list without duplicate entries

#Print either ‘Found’ or ‘Not found’

#Boundary Conditions:

#Number of students visited >=0


#n=int(input('enter the no. students visited'))
#e=[]
#for i in range(0,n):
 #   r=input()
  #  e.append(r)
#list1=list(dict.fromkeys(e))
#print(list1)
    
#s=input()
#if s in e:
 #   print('Found')
#else:
 #   print('Not found')


 #Arrangement of Plants
#A gardener has the practice of assigning ID to the plants during plantation.
#One day, he makes a note of the heights of plants in his garden.
#He writes the height of the plant against the ID of the plant.
#He then instructs his employee to keep the plants, in ascending order of
#its height. Design an algorithm and write the Python code to display the list
#of ID numbers of plants in ascending order of their height.
#IDs are also numbers. Check for boundary conditions and print 'Invalid input'
#for wrong input. For example, if there are three trees with IDs as
#175, 160, 120 and height as 47, 73 and 23 then the output should be
#[120, 175, 160].

#Input Format:

#First line contains the number of plants, n

#Next line contains the ID of the plant-1

#Next line contains the height of plant-1

#. . .

#Next line contains the ID of the plant-n

#Next line contains the height of plantn

#Output Format:

#IDs sorted according to height. Print one id in one line

#Boundary Conditions:

#All inputs >=0


#import operator
#n=int(input('enter the no. of the plants'))
#if n<0:
#    print('Invalid input')
#else:
#    thisdict={}
#    for i in range(n):
#        ids=int(input('enter the id of the  plant'))
#        h=int(input('enter the height of the plant'))
#        if ids<0 or h<0:
#            print('Invalid Input')
#        else:
#            thisdict[ids]=h
#print(thisdict)
#sorted_dict=sorted(thisdict.items(), key=operator.itemgetter(1))
#print(sorted_dict)
#list1=[]
#for i in range(len(sorted_dict)):
#    list1.append(sorted_dict[i][0])
#print(list1)
#Sparse Matrix
#Write an algorithm and the subsequent Python program to check whether the given
#matrix is sparse or not. A matrix is said to be a “Sparse” if the number  of
#zero entries  in the matrix,  is greater than or equal to the number  of
#non-zero entries. Otherwise it is  “Not sparse”. Check for boundary conditions
#and print 'Invalid input' when not satisfied.

 

#Input Format:

#The first line will contain the number of rows in the matrix, rows

#The Second line will contain the number of columns in the matrix, cols

#The next (rows * cols) lines will contain the elements of the matrix, entered
#row wise

#Output Format:

#Print either Sparse or Not sparse

#Boundary Conditions:

#Number of rows and columns > 0

#CODE
#r=int(input('enter the no. rows'))
#c=int(input('enter the no. of columns'))
#if r<0 or c<0:
#    print('Invalid input')
#else:
#    list1=[]
#    for i in range(0,r+c+1):
#        re=int(input('enter the element'))
#        list1.append(re)
#print(list1)

#list2=[]
#list3=[]
#for j in list1:
#    if j!=0:
#        list2.append(j)
#    else:
#        list3.append(j)
#print(list2)
#print(list3)
#if len(list3) >= len(list2):
#    print('Sparse')
    
#else:
#    print('Not sparse')

#Finding a Friend with Longest Name
#Write an algorithm and the subsequent Python program to store the names
#of your friends, count the number of friends, identify the longest name and
#the number of letters in the longest name. Get the names of friends till 'Stop'
#is entered. For example, if the input sequence is Ravi, Raj, Puela, Stop,
#then the output is 3, Puela and 5.

#When you are coding in the online judge (SkillRack), use rstrip()
#function to remove carriage return from the input string.

#Note: First letter of Stop should be in Upper Case

#Input Format:

#First line is the name of  the first friend

#Second line is the  name of the second friend

#Third line is the  name of the third friend

#….

#Stop

#Output Format:

#umber of friends

#Friend’s name with longest length

#Number of characters in that longest name
#list1=[]
#for i in range(1,101):
#    n=input('enter the name')
#    if n=='Stop':
#        break
#    list1.append(n)
#list2=[]
#for i in list1:
#    list2.append(len(i))
#print(len(list2))
#maxi=max(list2)
#ind=list2.index(maxi)
#print(list1[ind])
#print(maxi)



    
    
    



    






















































































        
        

    











































          
          
          
          
    
    
 
