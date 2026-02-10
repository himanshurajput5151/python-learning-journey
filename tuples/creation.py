#Topic : Tuple
#Creation:#Tuple is immutable represented by()

t1 = (1,2,3,4,5)
t2 = tuple([1,2,3,4])
t3 = tuple('python')
t4 = ()

print(t1)
print(t2)
print(t3)
print(t4)

t5 = (5,)   ##when passing single element use , (comma)
t6 = ('hello',)

print(t5)
print(t6)

t5 = (6)
print(type(t5)) ##type is int

t7 = tuple({1:'a',2:'b',3:'c',4:'d'})  ## dictionary as iterable
print(t7)

t8 = tuple({'g','e','b','a'})   ## set as iterable
print(t8)


t9 = 3,4,5,67,100           ##if multiple data is passed to single variable it is packed into tuple
print(t9)
