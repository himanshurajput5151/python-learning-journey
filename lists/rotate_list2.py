#Topic : List
#going to rotate the list by n places using slicing

l1 = list(map(int, input("Enter Numbers: ").split()))
n = int(input("Enter number of rotation: "))

l2 = l1[n:] + l1[:n]

print(l2)