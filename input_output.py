# to find area of a rectangle
length = float(input("Enter the length:"))
breadth = float(input("Enter the breadth:"))
area = length*breadth
print("Area of a rectangle:", area)

# To evaluate algebraic exp:a= 3x² − 2xy + y

x=int(input("Enter the value of x:"))
y=int(input("Enter the value of y:"))
ans=3*x**2-2*x*y+y # Processing
print("Answer is:",ans)

# Output Formatting

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=a+b
print("sum is",c)#parameters
print("Sum of",a,"and",b,"is",c)
print("Sum of {} and {} is {}".format(a,b,c)) # Formatted output
print("Sum of %d and %d is %d"%(a,b,c))



