# Write a Python program to get the largest number from a list.
lst=[1, 2, -8, 0]
max1 = lst[ 0 ]
for a in lst:
    if a > max1:
        max1 = a
print("Maximum Element",max1)

#Write a Python program to remove duplicates from a list.

a = [10,20,30,20,10,50,60,40,80,50,40]
uniq_items=[]
for x in a:
    if x not in  uniq_items:
        uniq_items.append(x) # add dup element in list
print("Unique items in list:",uniq_items)

# To get a list as input from the user.
element_list=[]
n=int(input("Enter the number of elements in the list:"))
for i in range(n):
    element=input("Enter the element:")
    element_list+=[element]
print("New list:",element_list)

# To get a list as input from the user.

element_list=eval(input("Enter the element list:"))
print("New list:",element_list)

#list comprehension
lst  =  [x ** 2  for x in range (1, 11)   if  x % 2 == 1]
print(lst)