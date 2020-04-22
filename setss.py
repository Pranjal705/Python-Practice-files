my_list=[1,2,3,4,5,5]
print(set(my_list))#it converted the above list into a set i.e
                 #it made every element of the list unique
A={1,2,3,4,5}
B={4,5,6,7,8,9}
print(A.difference(B))#it gives the A-B elements but doesnot update A.
print(A)

print(A.discard(5))#it removed the element 5 from set A but didinot return the value
print(A)

print(A.difference_update(B))#It removed the A-B elements from the set A.
print(A)

R={'a','b','c','d','e','f'}
S={'e','f','g','h','i'}
print(R.intersection(S))

print(R.union(S))#it gave the union of R and S.

print(R.isdisjoint(S))#It says if the two sets are disjoint or not.

print(R.issubset(S))#It says if R is the subset of S or not.

print(R.issuperset(S))#It says if R is the super set of S or not.


