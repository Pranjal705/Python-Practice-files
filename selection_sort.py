#selection_sorting
#1. First we found the min value of the list
#2.Then we swaped the first value with the min value which created sorted and unsorted part
#3.We repeated step 1 and step 2 for the unsorted part till we get the all list sorted

#For non-repeated numbers
list1 = [56,3,2,78,6,0]
print(list1)
for i in range(len(list1)):
    min_val = min(list1[i:])
    min_ind = list1.index(min_val)
    list1[i],list1[min_ind]=list1[min_ind],list1[i]
print(list1)

#For repeated numbers
list1 = [56,2,2,78,6,0]
print(list1)
for i in range(len(list1)-1):
    min_val = min(list1[i:])
    min_ind = list1.index(min_val,i)
    list1[i],list1[min_ind]=list1[min_ind],list1[i]
print(list1)



