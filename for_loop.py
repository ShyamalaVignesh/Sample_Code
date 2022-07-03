for i in "Chennai":
    print(i)

for i in [1,2,3,4,5]:
    print(i)

for i in range(10):
    print(i)
    print("Hai")

for i in range(1,11):
    print(i)

for i in range(1,11,2):
    print(i)

for i in range(10,0,-1):
    print(i)

# To generate the sum of numbers between 1 and 100
# 1+2+…+100=?

total=0
for i in range(1,101):
    print(i)
    total+=i
print("Total is:",total)

# To generate the sum of numbers divisible by 7 between  1 and 100

total=0
for i in range(1,101):
    if i%7==0:
        total+=i
print("Total is:",total)

# Use of break and continue in for loop

for i in range(1,11):
    print("Chair",i)
    if i==5:
        break

for i in range(1,11):
    if i==5:
        continue
    print("Chair",i)

# Nested For Loop

for i in range(5):
    for j in range(3):
        print(i,j)
