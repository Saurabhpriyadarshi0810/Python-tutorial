# if else synatx

age = int(input("enter your age :"))

if age >= 18 :
    print("eligible for voting.")
else:
    print("not eligible for voting.")


color = input("enter the color:")
if color.lower() == "red":
    print("Stop")
elif color.lower() == "green":
    print("Go")
elif color.lower() == "yellow":
    print("look")
else:
    print("invalid color")