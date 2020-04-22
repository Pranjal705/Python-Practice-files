Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Repeated print
>>> print('a'*15)
aaaaaaaaaaaaaaa
>>> print('\n'*15)
















>>> print('a\n'*15)
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a

>>> #complex numbera
>>> complex(2)
(2+0j)
>>> ocmplex(2,3)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    ocmplex(2,3)
NameError: name 'ocmplex' is not defined
>>> complex(2,3)
(2+3j)
>>> print(2.imag)
SyntaxError: invalid syntax
>>> print(2.real)
SyntaxError: invalid syntax
>>> A=complex(2,3);print(A)
(2+3j)
>>> print(A.imag)
3.0
>>> print(A.real)
2.0
>>> basic_pay=int(input('enter the basic_pay:'))
enter the basic_pay:25000
>>> net_salary=12*int(basic_pay)
>>> print(basic_pay)
25000
>>> print(net_salary)
300000
>>> #assignment statement
>>> spam='Spam'
>>> print(spam)
Spam
>>> spam,ham='yum','YUM'
>>> print(spam,ham)
yum YUM
>>> [spam,ham,bam]=['yum','YUM','Yum']
>>> print[spam,ham,bam]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print[spam,ham,bam]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> print(spam,ham,bam)
yum YUM Yum
>>> a,b,c,d='spam'
>>> print(a)
s
>>> print(b,c,d)
p a m
>>> a,*b=spam
>>> print(a,*b)
y u m
>>> spam=ham='lunch'
>>> print(ham)
lunch
>>> spam=42
>>> spam+=2
>>> print(spam)
44
>>> a,b,c=range(1,4)
>>> d
'm'
>>> a
1
>>> b
2
>>> c
3
>>> nudge=1
>>> wink=2
>>> T=nudge;nudge=wink;wink=T
>>> nudge,wink
(2, 1)
>>> #basic arithmetic operations in python
>>> 4+5
9
>>> 8-5
3
>>> 4*5
20
>>> 19/3
6.333333333333333
>>> 19//3
6
>>> 19%3
1
>>> 2**4
16
>>> 2**3+2*(2+3)
18
>>> #built in format function
>>> 12/5
2.4
>>> format(12/5, '.2f'))
SyntaxError: unmatched ')'
>>> format(12/5, '.2f')
'2.40'
>>> 5/7
0.7142857142857143
>>> format(5/7, '.3f')
'0.714'
>>> format(2**100, '.6e')
'1.267651e+30'
>>> num(100)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    num(100)
NameError: name 'num' is not defined
>>> num=10
>>> num
10
>>> id(num)
1421723712
>>> k=num
>>> id(k)
1421723712
>>> k=k+1
>>> k
11
>>> 1|2
3
>>> #bitwise operations
>>> 1|2
3
>>> 1&2
0
>>> 
