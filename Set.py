set1 = set([1,2,3,4,5])
set2 = set([3,4,5,6,7])
set3 = set([1,2,3,4,5,6,7, 8])

print(set1)
print(set2)
print(set3)

#Symmetric Difference of two sets using symmetric_difference(). 

A = set1.symmetric_difference(set2)
print(A)
