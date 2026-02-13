#Topic : Sets
# Input = words_set = {'plea','medical','listen','leap','decimal','silent','pale','enlist'}

# output = result = {('plea,'leap'),('plea','leap'),('medical','decimal'),
#                       ('listen','silent'),('listen','enlist'),
#                       ('leap','pale'),('silent','enlist)
#                      }


words_set = {'plea','medical','listen','leap','decimal','silent','pale','enlist'}
result = set()


for item in words_set:
    for word in words_set:
            if item!=word and sorted(item) == sorted(word):
                    pair = tuple(sorted((item,word)))
                    result.add(pair)


print(result)