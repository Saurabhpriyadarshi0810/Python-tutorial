f = open("demo.txt","r")

data = f.read()
print(data)
print(type(data))

f.close()

f = open("demo.txt","w")

data =  f.write(" i want to to reset demo.txt")

f.close()

f = open("sample.txt","a")

data =  f.write(" i want to to reset demo.txt")

f.close()