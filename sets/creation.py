#Topic : Sets
#In this we'll learn to create sets using different ways.

## Sets are unordered collection of distinct and heterogeneous elements
## they are immutable
##behind the scene they are stored with the help of hash table


s1 = {1,2,3,4,5,6}
s2 = set('python')                                  #set(iterable)
s3 = {5}                                            #set should contain at least one element
s4 = {(1,2,3), 'python', tuple('hello')}            #list are not allowed in sets as they give hashable error because they are immutable

print(s1)
print(s2)
print(s3)
print(s4)

s5 = set('imhEEllo')
##  print(s5[2])                                ## slicing and indexing does not work on sets because they are unordered

## Set Comprehension

s6 = {item.lower() for item in s5 }
print(s6)

s7 = {1,2,3,4,5,6}
s8 = {item**2 for item in s7}
print(s8)

s9 = {(3,6,9,12,15,18,21)}
s10 = {item**3 for tup in s9 for item in tup if item < 10}          ##break into nested loop
print(s10)

s11 = {item for item in range(2,20,3)}
print(s11)

s12 = {item for item in [5,6,7,8]}
print(s12)


s14 = set(['5', 6, '8', 8])
print(s14)