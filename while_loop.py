# To generate numbers between 1 and 100

i=1 # initialize
while i<=100:# condition
    print(i)
    i+=1 #increment i=i+1
print("***")

# To generate the sum of numbers between 1 and 100
# 1+2+…+100=?

total=0
i=1
while i<=100:
    total+=i
    i+=1
print("Total is",total)

# To generate the sum of numbers divisible by 7 between  1 and 100
total=0
i=1
while i<=100:
    if i%7==0:
        total+=i
    i+=1
print("Total is",total)

# To get five numbers from user and print its total

i=1
total=0
while i<=5:
    num=int(input("Enter a number:"))
    if num>0:
        total=total+num
    i+=1
print("Total is",total)

# Use of break statement
i=0
while i<10:
    i+=1
    if i==5:
        break
    print("chair",i)
print("***")

# Use of continue statement

i=0
while i<10:
    i+=1
    if i==5:
        continue
    print("chair",i)

# validation check using while

username=input("Enter the user name:")
while len(username)!=5:
    print("Sorry!Username should of length 5 only!")
    username=input("Enter the user name:")
print(username)