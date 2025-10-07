#convert KG to LBS or LBS to KG

weight=float(input("Enter your weight"))
weightUnit=input("Is this weight in (K)g or (L)bs:")

if weightUnit.upper() == "K":
    weightInLBS = weight / 0.45
    print("Your weight in LBS is:"+ str(weightInLBS))
elif weightUnit.upper() == "L":
    weightInKG = weight*0.4535
    print("Your weight in KG is:",weightInKG)

#print(weightUnit.upper())

