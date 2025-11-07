Student = {
    "name":"Saurabh",
    "roll":"24CS34",
    "regno": 24105156033,
    "branch":"CSE",
    "sem":"2nd"
}

print(Student.keys())
print(Student.values())
print(Student.items())
print(Student.get("name")) # it is used because when key is wrong it returns none not error 
print(Student.update({"city":"hajipur"}))
print(Student)