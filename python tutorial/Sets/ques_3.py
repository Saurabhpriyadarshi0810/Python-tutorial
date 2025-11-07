dic = {}
print("enter 3 subject and its marks ")
for i in range (1,4):
    subject = input("enter the subject name :")
    marks = int(input("enter the subject marks :"))
    dic.update({subject:marks})

print(dic)
