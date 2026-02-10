#Topic : Tuple
#Just like list we can create comprehension of tuples

l1 = [1,2,3,4,5,6]

t1 = (*(item**2 for item in l1),)           # '*' is required for unpacking iterable
print(t1)


l2 = list("pyTHhon235$%")
t2 = tuple(item.lower() for item in l2)
print(t2)

t3 = (*(item for item in l2 if item.isalnum()),)
print(t3)

## using range function
t4 = (*(item for item in range(5)),)
print(t4)


## make odd and even tuple from list l1

odd = (*(item for item in l1 if item%2!=0),)
even = (*(item for item in l1 if item%2==0),)

print("Odd: ",odd)
print("Even: ",even)