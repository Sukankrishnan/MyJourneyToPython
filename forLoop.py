#for loop declares a loop variable to iterate each item from the collection
#collection includes tuples, lists, strings and dictionaries
#for variable in iterable: <body>

programmingLanguages=["java", "javascript", "python", "C#", "C", "C++"]
print("The languages in the collection:  ")
for languages in programmingLanguages:
    print(languages)

#print each character
print("\n\nPrint each character")
inputValue="hello"

for character in inputValue:
    print(character)

#sum of even numbers
numbers=[1,2,2,4,4,5,6,24,45]
total=0
for number in numbers:
    if number%2==0:
        total=total+number


print("Total is ",total)
