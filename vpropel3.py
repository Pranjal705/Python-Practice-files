#Age in Seconds
#Houseflies have an approximate life of four weeks. Given the number of days a
#housefly lived, design an algorithm and write the Python code to determine its
#approximate age in seconds. Check for boundary conditions and print ‘Invalid
#input’ if condition is not satisfied. For example, if a housefly lived for 21
#days then its approximate age in seconds is 21*24*60*60 is 1814400.

#Input Format

#Number of days, n

#Output Format

#Number of seconds

#Boundary Conditions

#n>0 and n <28

#n=int(input('enter the no. of days'))
#if n<0 or n>28:
#    print('Invalid input')
#else:
#    days=n*24*60*60
#    print(days)


#Multiples of a number
#Write a Python Script to find the multiples of a given number up to
#a specific range.

#Input:

#Number

#range

#Output:

#Multiples of a number.

#For example, if a Number is 5 and range is '3' , the output is 5 10 15

#CODE
#n=int(input('enter the number'))
#r=int(input('enter the range'))
#for i in range(1,r+1):
#    m=n*i
#    print(m,' ',end='')




#Arithmetic Expression
#Write a python script to read a number from the user,
#find the difference between the sum of squares up to that number and the number itself. 

#Input:

#Number

#Output:

#Difference between the sum of squares up to that number and itself. 

#For example if a number is 3, then output will be 11 ( i.e 1 2 + 2 2 + 3 2   - 3 = 11)

#CODE

n=int(input('enter the number'))
sum1=0
for i in range(1,n+1):
    sq=i**2
    sum1=sum1+sq
o=sum1-n
print(o)





















