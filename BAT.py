#1
#Vowelgram
#Vowelgrams are words or sentences that has every vowel (a,e,i,o,u)  of  the
#English alphabet occurring  at the most  once. Write an algorithm and  a
#subsequent Python code to check whether a string is a vowelgram or not. Write a
#function to check if a given string is a vowelgram. For example,”You black tiger
#" is a vowelgram. ( Notice that no vowel occurs more than once )

#Input format

#First line contains the string to be checked

#Output Format

#Print Vowelgram or Not vowelgram

#n=input()
#l=n.casefold()
#if 'a' in l and 'e' in l and 'i' in l and 'o' in l and 'u' in l:
#    print('Vowelgram')
#else:
#    print('Not vowelgram')



#2
#Kangaroo word
#Kangaroo refers to a word carrying another word within it but without
#transposing any letters. Example: encourage contains courage, cog, cur, urge,
#core, cure, nag, rag, age, nor, rage and enrage but not run, gen, gone etc.
#Given two strings, design an algorithm/ flowchart and a Python function to
#determine if the first string is a Kangaroo word of second.

#Input Format:

#String1

#String2

#Output Format:

#Print True or False

#Boundary Conditions:

#m,n>0

#s1=input().rstrip()
#s2=input().rstrip()
#c=0
#j=0
#for i in range(len(s1)) :
#    if j<len(s2) :
#        if s1[i]==s2[j] :
#            c+=1
#            j+=1
#if c==len(s2) :
#    print('True')
#else :
#    print('False') 



#3
#Consogram
#onsograms are words or sentences that has every consonant( letters other than
#a,e,i,o,u)  of  the English alphabet occurring  at least  once. Write an
#algorithm and  a subsequent Python code to check whether a string is a consogram
#or not. Write a function to check if a given string is a consogram. For example,
#”"The quick brown fox jumps over the lazy dog"" is a consogram.

#Input format

#First line contains the string to be checked

#Output Format

#Print Consogram or Not consogram

#n=input()
#l=n.casefold()
#if 'b' in l and 'c' in l and 'd' in l and 'f' in l and 'g' in l and 'h' in l and 'j' in l and 'k' in l and 'l' in l and 'm' in l and 'n' in l and 'p' in l and 'q' in l and 'r' in l and 's' in l and 't' in l and 'v' in l and 'w' in l and 'x' in l and 'y' in l and 'z' in l:
#   print('Consogram')
#else:
 #  print('Not consogram')

#4
#Pengram
#Pengrams are words or sentences containing every letter of the English alphabet
#at the most once. Write an algorithm and  a subsequent Python code to check
#whether a string is a pengram or not. Write a function to check if a given
#string is a pengram. For example, "He is at work" is a pengram. Since every
#letter of the english alphabet occurs at the most once

#Input format

#First line contains the string to be checked

#Output Format

#Print Pengram or Not pengram



#n=input('enter the string')
#l=n.replace(' ','')
#list2=[]
#for i in l:
#   if n.count(i)>1:
#      list2.append('False')
#if 'False' in list2:
#   print('Not pengram')
#else:
#   print('Pengram')
      
#5
#Pangram1
#Pangrams are words or sentences containing every letter of the English alphabet
#at least once. Write an algorithm and  a subsequent Python code to check whether
#a string is a pangram or not. Write a function to check if a given string is
#pangram. For example, "The quick brown fox jumps over the lazy dog" is a panagra
#m.

#Input format

#First line contains the string to be checked

#Output Format

#Print Pangram or Not pangram

#n=input()
#l=n.casefold()
#if 'b' in l and 'c' in l and 'd' in l and 'f' in l and 'g' in l and 'h' in l and 'j' in l and 'k' in l and 'l' in l and 'm' in l and 'n' in l and 'p' in l and 'q' in l and 'r' in l and 's' in l and 't' in l and 'v' in l and 'w' in l and 'x' in l and 'y' in l and 'z' in l:
#   print('Pangram')
#else:
#   print('Not pangram')

#6
#Deficient Numbers
#A number is said to be a deficient number if the sum of the proper divisors are
#less than that number. All divisors  of a number other than 1 and itself,   are
#called proper divisors. 8 is a deficient number since the sum of the proper
#divisors are 6 (proper divisors of 8 are 2 and 4) Examples of deficient numbers
#include 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 21, 22, and 23.
#Given a number, write an algorithm and the subsequent Python code to check
#whether the given number is deficient or not.

#Input format

#Number to be checked

#Output Format

#Print Deficient or Not deficient



#n=int(input('enter the number'))
#sum1=0
#for i in range(2,n):
#   if n%i==0:
      #sum1+=i
#if sum1<n:
#   print('Deficient')
#else:
#   print('Not deficient')
      
#7
#IST (Indian Standard Time) is 5 hours 30 minutes ahead of GMT(Greenwich Mean Tim
#e). Develop an algorithm and write the Python code to find day and IST, given da
#y and time in GMT.
#For example, if day is Sunday and time in GMT is 23:05 then in IST is Monday
#(Next day) and time is 04:35. Check boundary conditions and print 'Invalid input
#' for wrong input.
#Write appropriate functions for accomplishing the task.
#Use rstrip() to remove extra spaces while reading strings
#Input Format
#Day
#Hours
#minutes of time in GMT
#Output Format
#Day
#Hours
#minutes of time in IST
#Boundary Condition:
#All hour > 0 and <24
#Minutes > 0 and < 60
#Seconds > 0 and <60
#Day is Sunday or Monday or Tuesday or Wednesday or Thursday or Friday or Saturda
#y


#days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
#n=input('enter the day')
#n1=n.capitalize()
#d=n1.rstrip()
#h=int(input('enter the hours'))*60
#m=int(input('enter the minutes'))
#total=h+m+330
#if h>0 and h<1440 and m>0 and m<60 and d in days:
#    if total>1440:
#        for i in range(len(days)-1):
#            if d==days[i]:
#                print(days[i+1])
#                break
#        print(total//60-24)
#        print(total%60)
#    else:
#        print(d)
#        print(total//60)
#        print(total%60)
#else:
#    print('Invalid input')



    











































































































































