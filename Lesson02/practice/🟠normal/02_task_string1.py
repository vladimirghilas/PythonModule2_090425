string = input("enter your string")
if string[0:3] == "id:" and string[3:].isdigit():
    print("Yes")
else:
    print("No")