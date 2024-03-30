name = "ahmed"
name2 = list(name)

print(str(name2))
name3 = list(name)

name3.append("1")
if name2 == name3:
    print("Yes, you")
else:
    print("No, you")