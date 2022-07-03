#To check if a string is palindrome or not.

name = input("Enter any string:")
if name==name[::-1]:
    print("palindrome")
else:
    print("Not a palindrome")

#Write a Python program to change a given string to a new string
# where the first and last chars have been exchanged.

#Sample String  : abcd     Expected Result: dbca

str1="abcd"
print(str1[-1:] + str1[1:-1] + str1[:1])

# Write a Python program to display the vowels of a given text.

str1='I Love India'
vowels = "aeiuoAEIOU"
for i in str1:
    if i in vowels:
        print(i)

# Write a Python program to remove spaces from a given string.

#Sample String: "w 3 res ou r ce"
#Expected Result: "w3resource"


str1 = "w 3 res ou r ce"
print( str1.replace(" ", ""))

# Count the no of alphabets and digits in a string.

a=input("Enter the string:")
alpha_count=0
digit_count=0

for i in range(len(a)):
    if a[i].isalpha():
        alpha_count+=1
    if a[i].isdigit():
        digit_count+=1
print("no of alphabets:",alpha_count)
print("no of digits",digit_count)



