#Simple Interest
#Given the principal(p),rate of interest (r) in percentage and number of years (n) to be invested.
#Write an algorithm and Python code to print the total amount that will be given after 'n' years. Formula to calculate simple interest is pnr/100.

#For example, if principal is 1000, rate of interest is 15% and number of years is 2 then the total amount returned will be 1300

#Input Format 

#First line contains the principal, p
#Second line contains the rate of interest, r
#Third line contains the number of years, n

#Output Format
#First line contains the amount to be received after n years




P=int(input('enter the principal amount: '))
r=int(input('enter the rate of interest'))
n=int(input('enter the number of years'))
I=(P*n*r)/100
A=P+I
print(f'The amount to be paid after {n} years is: {A}')

#Line and a Point
#Consider a line with equation 5*x + 10*y - 20 =0, given a point (x,y),
#write a Python code to check if it lies either on the line or on the left side or on the right side of the line.
#A point (x1,y1)  is said to lie on the line if 5*x1+10*y1-20 = 0 and the point lies on left side if 5*x1+10*y1-20 < 0
#and the point lies on the right side of the line if 5*x1+10*y1-20  > 0.

#Input Format

#First line contains the x-coordinate of the point, p

#Second line contains the y-coordinate of the point, p

#Output Format

#Print "On" or "Left" or "Right" without quotes

#Print On when the point lies on the line, left if the point is left to the line and right otherwise



a=int(input('enter the x-coordinate of the point'))
b=int(input('enter the y-coordinate of the point'))
f=5*a
g=10*b
i=20
j=f+g-i
if j==0:
    print('On')
elif j<0:
    print('Left')
else:
    print('Right')



#Given a value 'n', write an algorithm and Python code to print a decreasing patter as follows. When n is 5, the pattern looks as below:

#*****
#****
#***
#**
#*

#Input Format
#First line contains the value of 'n'

#Output Format
#Pattern



n=int(input('enter a positive integer'))
for i in range(n,0,-1):
    print('*'*i)


#sum of digits of a number
#Given a number 'n', write a Python code to find sum of digits. For example if n is 564 then sum = 5+6+4 = 15

#Input Format

#First line contains the number, n

#Output Format

#First line should contain the sum of digits of number n



a=input('enter the number')
a1=str(a)
if a1.isnumeric():
    l=[]
    for i in range(0,len(a1)):
        l.append(a1[i])
        sum=0
    for i in l:
        n=int(i)
        sum=sum+n
    print(sum)
else:
    print('invalid input')

    
#perfect number
#Given a number 'n', write a Python code to check if it is a perfect number.
#A number is said to be a perfect number if it is equal to its sum of its good factors.
#All factors of 'n' excluding itself are good factors of a number.
#For example, 6 is  a perfect number as 1+2+3 = 6

#Input Format

#First line contains the number, n

#Output Format

#Print Yes if the number is a perfect number and No otherwise

k=int(input('enter the number'))
sum2=0
for i in range(1,k):
    if k%i==0:
        sum2+=i
if sum2==k:
    print("yes")
else:
    print('No')
        




































