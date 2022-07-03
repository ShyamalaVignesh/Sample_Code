# One-way If

num = int(input("Enter a number:"))
if num > 0:
    print("No is positive")

# Two-way if

num = int(input("Enter a number:"))
if num >= 0:
    print("No is positive")
else:
    print("Num is negative")

# Multi - way if

num = int(input("Enter a number:"))
if num > 0:
    print("No is positive")
elif num < 0:
    print("Num is negative")
else:
    print("It is Zero")
print("*********")

# to check login details as username="Shyamala" and pwd=123

user_name = input("Enter the UserName:")
pwd = int(input("Enter the Password:"))
if user_name == "Shyamala" and pwd == 123:
    print("Valid Login")
elif user_name == "Shyamala" and pwd != 123:
    print("Valid Username but Invalid Pwd")
elif user_name != "Shyamala" and pwd == 123:
    print("Valid Password but Invalid Username")
else:
    print("Invalid Username And Password")

# To check Login details using Nested-if

user_name = input("Enter the UserName:")
pwd = int(input("Enter the Password:"))
if user_name == "Shyamala":
    if pwd == 123:
        print("Valid Login")
    else:
        print("Valid Username but Invalid Pwd")
elif pwd == 123:
    print("Valid Password but Invalid Username")
else:
    print("Invalid Username And Password")
