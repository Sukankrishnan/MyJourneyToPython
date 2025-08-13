#Adding two numbers assigned to the variables
numberOne=5
numberTwo=8

#using + operator
total=numberOne+numberTwo
print("Using + operator:" , total)

#using sum() function - useful when adding multiple numbers
print("Total using sum function:", sum([numberOne,numberTwo]))

#getting input from the user and converting to Integer
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Sum of two inputs is ",a+b)
