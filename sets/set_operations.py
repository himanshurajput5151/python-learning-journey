#Topic : Sets

# Union, Intersection, intersection_update
# difference, difference_update, symmetric_difference
# symmetric_difference_update

s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8,9,10}
print(s1)
s3 = s1.union(s2)
s4 = s1.intersection(s2)
#   s1.intersection_update(s2)          #modifies the set on which it is called
s5 = s1.difference(s2)
s6 = s1.symmetric_difference(s2)

print(s3)
print(s4)
print(s6)

s1.difference_update(s2)                ##modifies the set on which it is called
s1.symmetric_difference_update(s2)      #modifies the set on which it is called

set1 = {1,2,3,4,5,6}
set2 = {5,6,7,8,9}


s1 = set1 | set2        #union
s2 = set1 & set2        #intersection
s3 = set1 - set2        #difference
set1 &= set2            #intersection_update
set1 -= set2            #difference_update
s4 = set1 ^ set2        #symmetric_difference
set1 ^= set2            #symmetric_difference_update
