#Given a number ‘n’, design an algorithm and write the Python program to
#print the digits of ‘n’ that  divides ‘n’. Print the digits in reverse order
#of their appearance in the number ‘n’.  For example, if n is 122 then print 2, 2
#, 1. Use only conditional and iterative statements to write the code. If none of
#the digits divide the number, then print ‘No factors’

#Input Format

#A number, n 

#Output Format

#Digits in the number ‘n’ that divides ‘n’ in reverse order

#n=input()
#numbers=[]
#for i in n:
#    if int(i)!=0 and int(n)%int(i)==0:
            #numbers.append(int(i))
#numbers.reverse()            
#print(numbers)

#if numbers==[]:
#    print('No factors')
#else:
#    for j in numbers:
#        print(j, end=", ")


        


#Roman Letters
#The numeric system represented by Roman numerals originated in ancient Rome and remained the usual way of writing numbers throughout Europe well into the late Middle Ages. Numbers in this system are represented by combinations of letters as shown below:

#Roman

#Numeral

#I

#V

#X

#L

#C

#D

#M

#Value

#1

#5

#10

#50

#100

#500

#1000

 

#Given a letter in Roman numeral, develop an algorithm and write the Python code to print the value of it.
 #If some other letter other than Roman numeral is given as input then print ‘Enter a roman numeral’ and terminate.

#Input Format

#A Roman Letter

#Output Format

#Value equivalent to the letter


#Water in a Dam
#A city has a dam of capacity ‘x’ litres, water comes to the dam from ‘n’ places.
#Given the value of ‘n’ and the quantity of water (in litres and millilitres) that comes from ‘n’ places, Write an  algorithm and
#the corresponding Python code to determine the total amount of water in the dam. Assume that the total quantity of water in the dam,
#will be always less than the capacity of the dam. For example, if there are three places from which water comes to the dam and the water
#from place 1 is 2 litres 500 ml, water from second place is 3 litres 400 ml and water from third place is 1 litre 700 ml then the total quantity of water in dam will be 7 litres 600 ml.

#Input Format

#Number of places from where water comes, n

#Number of litres of water from place-1

#Number of millilitres of water from place-1

#Number of litres of water from place-2

#Number of millilitres of water from place-2

#...

#Number of litres of water from plac- n

#Number of millilitres of water from place- n

#Output Format

#Total litres of water in the dam

#Total millilitres of water in the dam


#n=int(input('enter the no. of places'))
#ln=0
#ml=0
#for i in range(1,n+1):
#    l=int(input('enter the no. of litres'))
#    m=int(input('enter the no. of millilitres'))
#    ln+=l
#    ml+=m
#if ml>=1000:
#    ln+=1
#    ml-=1000
#print(ln,ml)


#Caesar Cipher
#In Caesar cipher, each letter is replaced by another letter which occurs at the
#d-th position (when counted from the position of the original letter),  in the
#English alphabet.  For identifying the position of a letter, we follow the usual
#order of the English alphabet, from a to z. Given a word and a positive integer
#d, use Caesar cipher to encrypt it. For example, if the word is 'ball' and the
#value of 'd' is 3 then the new encrypted word is 'edoo'. 'x' will be replaced by
#'a', 'y' should be replaced by 'b' and 'z' should be replaced by 'c'. While the
#code is submitted for Online Judge (SkillRack), use rstrip(), to remove carriage
#return character in the input.

#Input Format

#Word

#A positive integer 'd'

#Output format:

#Encrypted word

n=input()
l=n.casefold()
r=l.rstrip()
d={'a':'d','b':'e','c':'f','d':'g','e':'h','f':'i','g':'j','h':'k','i':'l','j':'m','k':'n','l':'o','m':'p','n':'q','o':'r','p':'s','q':'t','r':'u','s':'v','t':'w','u':'x','v':'y','w':'z','x':'a','y':'b','z':'c'}
for i in r:
    word=d[i]
    print(word,end='')

























 
