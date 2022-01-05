set1 = set([1,2,3,4,5])
set2 = set([3,4,5,6,7])
set3 = set([1,2,3,4,5,6,7, 8])

print(set1)
print(set2)
print(set3)

#The intersection_update() method.

set3.intersection_update(set1, set2)

print(set3)
