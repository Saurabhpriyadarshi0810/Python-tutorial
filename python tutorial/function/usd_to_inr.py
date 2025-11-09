def curr(usd):
    inr = usd * 83
    return inr

usd = int(input("enter the amount :"))
print(usd,"dollar is equal to ",curr(usd)," in indian rupee")
