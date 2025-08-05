#function to add 2 numbers
def addNum(num1,num2):
    total=num1+num2
    return total

#get 2 numbers from the user
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

#store and print the returned value from function
sum=addNum(num1, num2)
print("Sum of two numbers: ",sum)