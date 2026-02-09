#Topic : List
# Rotate the List by n places


word_number = input("Enter Number with Spaces: ")
word_number = word_number.split()
l1 = [int(item) for item in word_number]

times = int(input("Enter the number of times you want to rotate List: "))
times = times%len(l1)       ##if times is greater than the size of list

rotated_list = []

for i in range(len(l1)):
    if i >=times:
        rotated_list.append(l1[i])

for i in range(0,times):
    rotated_list.append(l1[i])


print(rotated_list)