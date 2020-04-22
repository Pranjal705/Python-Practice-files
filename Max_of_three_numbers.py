#1. Write a Python function to find the Max of three numbers.
def maxv(a):
  for i in a:
    m=a[0]
    indexx=a.index(m)
    if m<a[indexx+1]:
      a[0],a[indexx+1]=a[indexx+1],a[0]
  return m
  




a=[3,5,2]
print(maxv(a))

#OR

def maxv(a):
    for i in range(len(a)-1):
        if a[0]<a[i+1]:
            a[0],a[i+1]=a[i+1],a[0]
    return a[0]
a=[2,3,4,5,8]
print(maxv(a))
