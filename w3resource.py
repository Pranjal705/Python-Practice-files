def maxv(a):
    for i in range(len(a)-1):
        if a[0]<a[i+1]:
            a[0],a[i+1]=a[i+1],a[0]
    return a[0]
a=[2,3,4,5,8]
print(maxv(a))

#2. Write a Python function to sum all the numbers in a list. Go to the editor
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20

def addition(a):
  summ=0
  for i in a:
    summ=summ+i
  return summ
  
a=[8,2,3,0,7]
print(addition(a))

#3. Write a Python function to multiply all the numbers in a list. Go to the editor
#Sample List : (8, 2, 3, -1, 7)
#Expected Output : -336 

def multiplier(a):
  p=1
  for i in a:
    p=p*i
  return p
a=[8,2,3,-1,7]
print(multiplier(a))

#5. Write a Python function to calculate the factorial 
#of a number (a non-negative integer).
#The function accepts the number as an argument.

def factorial(a):
  b=1
  for i in range(0,a):
    b=b*(a-i)
  return b
    
print(factorial(0))


#6. Write a Python function to check 
#whether a number is in a given range.
def check(a,r):
  b1=r[1]
  b2=r[len(r)-1]
  if a>=b1 and a<=b2:
    return "Yes"
  else:
    return 'No'
    
r1=range(0,5)
print(check(4,r1))


