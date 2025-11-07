# set is mutable but its element is immutable that why element of set can't be list and dictionary

collection = set()

print(collection)

collection.add(1)
collection.add(2)
collection.add(3)

print(collection)

collection.remove(2)
print(collection)

print(collection.pop()) # it removes first element 
print(collection)

collection.clear() # clear set
print(collection)



# if we remove element from set which is not present it gives us key error.
# when we add list and dictionary in set it gives unhasable error 



a = {1,2,3,4,5,6,7,8,9,10}
b = {5,6,7,8,9,10,11,12,13}

print(a.union(b))
print(a.intersection(b))
