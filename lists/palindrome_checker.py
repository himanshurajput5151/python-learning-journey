#Topic : List
#to check whether the list is palindrome or not

l1 = list(map(int,input("Enter Number: ").split()))
l2 = l1[::-1]
if l1==l2 :
    print("Palindrome")
else:
    print("Not palindrome")
