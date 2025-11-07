tup = (1,4,9,16,25,36,49,64,81,100)
num = int (input("enter the number you want to find : "))
flag = 0
i = 0
while  i < len(tup) :
    if tup[i] == num:
        flag = 1
        print(num,"is present at index",i)
        break
    i+=1

if flag == 0 :
    print (num," is not present in tuple ")
 