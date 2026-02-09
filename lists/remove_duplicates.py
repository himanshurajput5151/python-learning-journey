# Topic : List
#Remove duplicates from the List

duplicate_list = [1,2,3,2,4,5,6,8,4,2,3]

distinct_list = []

for item in duplicate_list:
    if item not in distinct_list:
        distinct_list.append(item)

print(distinct_list)
