tup = (25,12,14,15,63,14,14,1,78)
print(tup)
print(type(tup))

tup1 =(1,)
print(tup1)
print(type(tup1))


tup2 =(1) # this is not tuple 
print(tup2)
print(type(tup2))

tup3 =10,25,14,15
print(tup3)
print(type(tup3))


# slicing same as it is in list 

# tup3[1] =5 # it gives us error as tuple is immutable 


# tuple methods 

print(tup.index(14))  # returns index of first ocuurance of the given element 
print(tup.count(14))  # returns count of occurance of the given element in the given tuple.