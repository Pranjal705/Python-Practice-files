n=int(input('enter the no.of elements u want in universal set'))
U={}
for i in range(n+1):
    U.add(input('enter the next element'))
print(U)
a1=int(input('enter the no. of elements u want in subset a'))
a={}
for j in range(a1+1):
    a.add(input('enter the next element'))
a2=int(input('enter the no. of elements u want in subset b'))
b={}
for k in range(a2+1):
    b.add(input('enter the next element'))
a3=int(input('enter the no. of elements u want in subset c'))
c={}
for l in range(a3+1):
    c.add(input('enter the next element'))
a4=int(input('enter the no. of elements u want in subset d'))
d={}
for m in range(a4+1):
    d.add(input('enter the next element'))
a5=int(input('enter the no. of elements u want in e'))
e={}
for n in range(a5+1):
    e.add(input('enter the next element'))
A=a|b|c|d|e
if U==A:
    print(A)
else:
    print('no such sets')
