#Topic : List
#split the list according to odd and even

list1 = list(map(int,input("Enter Number: ").split()))

odd = [x for x in list1 if x%2!=0]
even = [x for x in list1 if x%2==0]
print(odd)
print(even)