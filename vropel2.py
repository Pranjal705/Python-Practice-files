#Keyboard Letters
#Given an  English word,  write an algorithm and the subsequent Python code to
#check if the given word can be typed using just a single row of the keyboard.
#(e.g. POTTER, EQUITY). Print 'Yes' if the letters of the word are from a single
#row and print 'No' otherwise.

#Input format:

#A word

#Output format:

#Print ‘Yes’ if all letters of the word are from same row in a keyboard
#list1=['Q','W','E','R','T','Y','U','I','O','P','q','w','e','r','t','y','u','i','o','p']
#list2=['A','S','D','F','G','H','J','K','L','a','s','d','f','g','h','j','k','l']
#list3=['Z','X','C','V','B','N','M','z','x','c','v','b','n','m']
#row1=set(list1)
#row2=set(list2)
#row3=set(list3)
#n=input('enter the word')
#list4=[]
#for i in n:
#    list4.append(i)
#a=set(list4)
#if a.issubset(row1):
#    print('Yes')
#elif a.issubset(row2):
#    print('Yes')
#elif a.issubset(row3):
#   print('Yes')
#else:
#    print('No')

#Time Conversion
#Given a time in the 12-hour format with the suffix , either AM/PM, convert that
#into a 24-hour format. 12-hour format is hours:minutes:seconds followed by AM or
#PM, where the hours range from 0 to 12, minutes range from 0 to 59, seconds rang
#e from 0 to 59.  24-hours format is hours:minutes and seconds , where hours rang
#e from 0 to 23, minutes range from 0 to 59, seconds range from 0 to 59. All the
#three components: hours, minutes, seconds are represented in the two digit forma
#t.

#Note Midnight 12 o’clock is 12:00:00AM in the 12-hour format and it is 00:00:00
#in 24- hour format. 12 Noon is 12:00:00PM in the 12-hour format and it is 12:00:
#    00 in the 24- hour format.

#For example, if input is 07:05:45PM then the output is 19:05:45 and if the inpu
#t
#is 07:05:45AM then the output is 07:05:45.

#Input format:

#Time in 12-hour format with suffix, either  AM or PM

#Output format:

#Print time in 24-hour format

#Boundary Conditions:

#0 < hour, minute and seconds < 60

#Meridium should be either “AM” or “PM”


#if 'AM' in n:
 #   n.remove('AM')
   # print(n)


#Distinct Letter
#A word is called as a good word if all the letters of the word are distinct.
#That is, all the letters of the word are different from each other letter.
#Else, the word is called as a bad word.

#Write an algorithm and the subsequent Python code to check if the given word is
#good or bad.: e.g. START, GOOD, BETTER are bad: WRONG is good! Make the
#comparison to be case insensitive.

#Input format:

#A word

#Output format:

#Print ‘Good’ if all letters of the word are distinct and print ‘bad’ otherwise

n=input('enter a word')
l=n.casefold()
list1=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            list1.append(i)
            break
if list1!=[]:
    print('Bad word')
else:
    print('Good word')
        


















































































    





                  
            
