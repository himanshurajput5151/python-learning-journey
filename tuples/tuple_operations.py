#Topic : Tuple
## Operation -> Concatenation(+), Repetition(*), Membership(in, not in), Packing and Unpacking, Comparison

# 1) Concatenation(+)

t1 = (1,2,3)
t2 = (3,4,5)
t3 = t1+t2
print(t3)

# 2) Repetition(*)

t4 = (5,6,7)
t5 = t4*2
print(t5)

# 3) Membership (in,not in)

t1 = ([1,2,3],[4,5],6,7,{8,9,10}, {'a':23,'b':56})
print([1,2,3] in t1)
print({8,9,10} in t1)
print({'a':23} in t1)
print({'a':23, 'b': 56} in t1)
print(6 in t1)


# 4) packing

#when multiple value are given to single var it packs them as tuple

fruits = 'mango' , 'apple' , 'cherrry', 'grapes'
print(fruits)

num = 1,2,3,4,5,6
print(num)

# 5) unpacking
# if you assign tuple to multiple variable it will unpack the tuple and assign the value to given variables.

a,b,c,d,e,f = t1
print(a,b,c,d,e,f)          #op [1, 2, 3] [4, 5] 6 7 {8, 9, 10} {'a': 23, 'b': 56}

t2=(1,2,3,4,5)
a,b,*c = t2
print(a,b,c)                #op 1 2 [3, 4, 5]

*a,b,c = t2
print(a,b,c)                #op [1, 2, 3] 4 5

# 6) Comparison operator

t1 = (1,2,3)
t2 = (1,2,3)
t3 = (33,4,5)
t4 = (5,)

print(t1==t2)
print(t3>t2)
print(t4>t2)
