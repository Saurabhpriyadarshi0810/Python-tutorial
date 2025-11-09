def factorial(n):
    fact = 1 
    for i in range(1,n+1):
        fact = fact * i
        i+=1
    return fact 
    
n = int(input("enter the number :"))
print("factorial of",n,"is :",factorial(n))
