 #Get input in the console and find prime numbers from the input.
listOfNumbers=list(map(int,input("Enter the numbers with space to find prime numbers").split()))

for  number in listOfNumbers:
    if number<2:
        print(number, " is not a prime number")
    else:
        for j in range (2,number):
            if number%j==0:
                print(number, " is not a prime number")
                break
        else:
            print(number, " is a prime number")

#Get the numbers from the user in console and save in list
#Iterate the list using for loop
    #Consider less than 2 are not prime numbers
    #else
    #iterate the list from second number
        #


