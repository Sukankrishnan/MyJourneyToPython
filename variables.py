#Find new patient

#hardcoded patient name
# patient = "John Smith"

#get input
patient =input("What is your name?")
age=int(input("How old are you?"))
is_newPatient = False

if(is_newPatient):
    print (patient, "who is", age , "is a new patient")
else:
    print(patient, "who is", age, "is not a new patient")


#print Float numbers
float_one= float(input("Enter first number"))
float_two=float(input("Enter second number"))
sum = float_one + float_two
print("Sum of two inputs is " + str(sum))