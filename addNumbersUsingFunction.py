#Add two numbers using function
def addNum(numberOne,numberTwo):
    total=numberOne+numberTwo
    return total

#get 2 numbers from the user and converting to integer
valueOne=int(input("Enter first number: "))
valueTwo=int(input("Enter second number: "))

#store and print the returned value from function
totalSum=addNum(valueOne, valueTwo)
print("Sum of two numbers: ",totalSum)