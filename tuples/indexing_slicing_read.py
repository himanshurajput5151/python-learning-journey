#Topic : Tuple
## perform indexing and slicing on tuple
## since tuple is immutable we can perform only read operation

t1 = (1,2,3,4,5,6)

#Indexing
print(t1[0])
print(t1[len(t1)-1])
print(t1[len(t1)-len(t1)])
print(t1[-4])

#Slicing [start:stop:step] -> all are optional, default start = 0, stop = len(tuple), step = 1

print(t1[:])                            #to print entire tuple
print(t1[0:])                           #to print entire tuple
print(t1[int(len(t1)/2):])              #to print 2nd half of tuple
print(t1[:int(len(t1)/2)])              #to print 1st half of tuple
print(t1[::-1])                         #to print tuple in reverse
print(t1[::2])                          #to print alternate values


print(t1[6:3:-1])                       ## three of them will give same result
print(t1[-1:-3:-1])
