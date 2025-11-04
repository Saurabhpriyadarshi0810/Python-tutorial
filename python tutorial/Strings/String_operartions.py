# concatenation(+) : it is used to add two string 

str1 = "Saurabh"
str2 = "Priyadarshi"
str = str1+" "+str2
print (str)

# len() :- used to calculate length of string 

print(len(str))

# index :- postion given to each character of a string

print(str[1])

# slicing :- used to access part of string 

print(str[4:10]) # [a:b:c] a is starting index , b is ending index and b is excluded , c is step .
print(str[4:])
print(str[:10])
print(str[::-1])


# string function 

print(str.endswith("rshi"))
print(str.capitalize())
print(str.replace("Saurabh","nanhe"))
print(str.find("nanhe")) 
print(str.count("a")) 
