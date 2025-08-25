#program to write squaring the numbers

numbers=[1,2,3,4,5]

#lambda is a one line, anonymous function without a name
squaredNumbers=list(map(lambda square: square*2,numbers))
print(squaredNumbers)