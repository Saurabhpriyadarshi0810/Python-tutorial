# type conversion

a = 2
b = 4.25
print (a + b) # a is automatically converted to int by the interpreter to avoid loss of data 

# type casting

x = "saurabh"
y = 34
# print (x+y)  this shows error and x type is not converted

z = str(y) # here we forcefully converted y into string
print(x + z )