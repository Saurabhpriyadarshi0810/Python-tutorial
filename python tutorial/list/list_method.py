alist = [2,1,3]

#append - means it add an element in the end 
alist.append(4)
print(alist)

# sort -  used to arrange in accending order 
alist.sort()
print(alist)

# to sort in desending order 

alist.sort(reverse = True)
print(alist)

# sorting also occur apply in strings 
# reverse method is used to reverse the  original list

fruits = ['mango' ,'banana','litchi','apple']
fruits.reverse()
print(fruits)


fruits.sort()
print(fruits)

fruits.sort(reverse = True)
print(fruits)

#insert() is  used to add element at a particular index 

fruits.insert(3,"pineapple")
print(fruits)

# remove the first occurance of the given element 

num = [1,2,3,4,1,5,6,2]
# num.remove(2)
# print(num)

''' pop is used to remove and return the element present at  the given index 
and if the index is not given then it do it with the last element '''

print(num.pop(1))
print(num)

print(num.pop())
print(num)

