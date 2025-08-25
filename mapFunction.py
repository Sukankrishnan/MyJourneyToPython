#program to write even numbers using map function - map(function, iterable)

def make_even(number):
    if number%2==1:
        return number+1
    else:
        return number

arrayOfNumbers=[234,353,522,543,234,654,347,456]

#using map function, send the array of numbers to make_even function to find even number
evenNumbers=list(map(make_even,arrayOfNumbers)) #list(map...)) builds the entire list in memory at once
print("Even numbers from the array are ", evenNumbers)