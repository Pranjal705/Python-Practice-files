#Minimum distance points
#Given 'n' points in an X-Y plane , write an algorithm and the subsequent Python
#ode to determine the pair of points that are closer. Distance between two poin
#ts (x1, y1) and (x2, y2) is determined using the formula.

 


 

#Consider only two decimal places of distance for comparison. When there are mul
#tiple points with the same minimum distance print all points.

#Input Format

#Number of points

#x coordinate of point1

#y coordinate of point1

#x coordinate of point2

#y coordinate of point2

#...

#Output format

#Point1 and Point2 that have minimum distance between them


#n=int(input('enter the no. points'))

#Letter Identification
#Given three words, write an algorithm and the subsequent Python code to
#identify the following letters:

#Letters common to all the three words
#Letters in first two words but not in third word
#Letters in first word but not in second and third word
#Letters in all the three words
#For example, if the words are apple, camel, element then letters in common to
#all the three words -  i, e

#Letters in first two words but not in third word – a

#Letters in first word but not in second and third word  - p

#Letters in all the three words – a, p, p, l, e, c, m, n, t

#Hint: Use sets in Python. While reading input, use rstrip() function to remove
#extra spaces 

#Input Format

#First line contains word1

#Second line contains word2

#Third line contains word3

#Output Format

#List of letters common to all the three words in lexicographical order

#List of letters common to first two words but not in third word in
#lexicographical order

#List of letters in first word but not in second or third word in
#lexicographical order

#List of all letters in the three words in lexicographical order




#w1=input('enter the word 1: ')
#w2=input('enter the word2: ')
#w3=input('enter the word3: ')
#a=set()
#b=set()
#c=set()
#for i in w1:
#    a.add(i)
#for j in w2:
#    b.add(j)
#for k in w3:
#    c.add(k)
#d=a.intersection(b)
#e=d.intersection(c)
#k=list(e)
#k.sort()
#print(k)
#f=a.intersection(b)
#j=f.difference(c)
#l=list(j)
#l.sort()
#print(l)
#g=b.union(c)
#h=a.difference(g)
#m=list(h)
#m.sort()
#print(m)
#i=a|b|c
#n=list(i)
#n.sort()
#print(n)    

#Rook and a Queen
#Given the position of a Rook and a queen in a chess board (8X8 board),  write an
#algorithm and the subsequent Python code to determine the common positions where
#both rook and queen can be placed in the next move. Rook can move through any
#number of cells,  either horizontally or vertically. Queens can move through any
#number of cells,  either horizontally, vertically or diagonally.  Each cell in
#the chess board may be represented as a 2-tuple (row,col). For example, if the
#current position of the rook is (3,1) then the next possible position of the
#rook may be either in the same column {(2,1),(1,1),(4,1),(5,1),(6,1),(7,1),(8,1)
#} or in the same row {(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8)}. If the queen i
#s in the position (5,3) then it can be placed in the same row {(5,1),(5,2),(5,4)
#,(5,5),(5,6),(5,7),(5,8)} or same column {(1,3),(2,3),(3,3),(4,3),(6,3),(7,3),
#(8,3)} or along the diagonal of the current position {(6,4),(7,5),(8,6),(4,2),
#(5,1),(6,2),(7,1),(4,4),(3,5),(2,6),(1,7)}. Then the common cells for next move
#are {(3,3), (5,1), (7,1)}.

#The output is a set of common board positions where both queen and rook can be
#placed. The positions must be printed in sorted order, sort it by row.
#When rows are same,  sort it by column.

 

#(Hint: Use built-in function to sort the values)

#Input Format

#Row position of rook

#Column position of rook

#Row position of queen

#Column position of queen

#Output Format

#Common position1

#Common position2

#...

r1=int(input('enter the row position of rook: '))
c1=int(input('enter the column position of rook: '))
r2=int(input('enter the row position of queen'))
c2=int(input('enter the column position of queen'))
r_c=[1,2,3,4,5,6,7,8]
set1=set()
set2=set()
p_of_rook=(r1,c1)
set3=set()
for i in r_c:
    a=(r1,i)
    set3.add(a)
set3.remove(p_of_rook)
for j in r_c:
    b=(j,c1)
    set3.add(b)
set3.remove(p_of_rook)
print(set3)
p_of_queen=(r2,c2)
set4=set()
for i in r_c:
    c=(r2,i)
    set4.add(c)
set4.remove(p_of_queen)
for j in r_c:
    d=(j,c2)
    set4.add(d)
set4.remove(p_of_queen)
print(set4)
set5=set()
for k in range(r_c.index(r2),len(r_c)):
    e=(r_c[k+1],r_c[k-1])
    set5.add(e)
print(set5)
    
    










































































    
