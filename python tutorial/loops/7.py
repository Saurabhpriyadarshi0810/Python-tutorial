tup = (1,4,9,16,25,36,49,64,81,100)
num = int (input("enter the number you want to find : "))
flag = 0

for i in tup :
    if i == num:
        flag = 1
        print(num,"is present")
        break
    

if flag == 0 :
    print (num," is not present in tuple ")
 