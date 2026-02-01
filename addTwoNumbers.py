#Program to add two numbers
#Values assigned to the variables
numberOne=5
numberTwo=8

#using + operator
total=numberOne+numberTwo
print("Using + operator:", total)

#using sum() function - useful when adding multiple numbers
print("Total using sum function:", sum([numberOne,numberTwo]))

print("Hello World!", end="!")  #end parameter to avoid new line
print(" This is on the same line.")


#getting input from the user and converting to Integer
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Sum of two inputs is ",a+b)
print("The sums\rstring\n num of \"two numbers\" is ", a+b) #\r is carriage return. It will overwrite the line from the beginning. "The sum" is overwritten by "string". "m of " remains.
print("new\noverwrite")
