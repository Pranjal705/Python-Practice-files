Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> subject='python'
>>> print(subject.upper())
PYTHON
>>> print(subject.lower())
python
>>> print(course.find(h))
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(course.find(h))
NameError: name 'course' is not defined
>>> print(course.find('h'))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(course.find('h'))
NameError: name 'course' is not defined
>>> course=begineers
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    course=begineers
NameError: name 'begineers' is not defined
>>> couse='begineers'
>>> print(course.find('g'))
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(course.find('g'))
NameError: name 'course' is not defined
>>> course='begineers'
>>> print(course.find('g'))
2
>>> print(course.find('begineers'))
0
>>> course='python for begineers'
>>> print(coure.replace('begineers', 'absolute begineers'))
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(coure.replace('begineers', 'absolute begineers'))
NameError: name 'coure' is not defined
>>> print(course.replace('begineers', 'absolute begineers'))
python for absolute begineers
>>> print('python' in course)
True
>>> print('and' in course)
False
>>> print(len())
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(len())
TypeError: len() takes exactly one argument (0 given)
>>> print(len(course))
20
>>> 
