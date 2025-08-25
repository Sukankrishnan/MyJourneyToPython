#program that takes 'n' digits and adds it up

#n = 0123456789 - SyntaxError: leading zeros in decimal integer literals are not permitted

number=1234567890
#convert integer to string of each character, convert each string into integer using map function and make it a list
digits=list(map(int,str(number)))

#print digits
print("Digits are ",digits)

#add and print all the digits
sumOfDigits=sum(digits)
print("Sum of 'n' digits: ",sumOfDigits)