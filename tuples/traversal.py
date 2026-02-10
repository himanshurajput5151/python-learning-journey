#Topic : Tuple
#Different ways to traverse to Tuple

t1 = tuple("pythonHELlo")

##using for-each loop
for item in t1:
    print(item)

## using for loop and range function
for i in range(len(t1)):
    print(t1[i])

## using while loop

i=0
while (i<len(t1)):
    print(t1[i])
    i=i+1
