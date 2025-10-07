#for loop declares a loop variable to iterate each item from the collection
#collection includes tuples, lists, strings and dictionaries
#for variable in iterable: <body>

#print each item from the list
programmingLanguages=["java", "javascript", "python", "C#", "C", "C++"]
print("The languages in the collection:  ")
for languages in programmingLanguages:
    print(languages)

#The languages in the collection:
#java
#javascript
#python
#C#
#C
#C++

#print each character in string
print("\n\nPrint each character")
inputValue="hello"

for character in inputValue:
    print(character)

#Print each character
#h
#e
#l
#l
#o

#sum of even numbers
numbers=[1,2,2,4,4,5,6,24,45]
total=0
for number in numbers:
    if number%2==0:
        total=total+number
print("Total is ",total)

#Total is  42

a=range(10)
print(a)
for b in a:
    print(b)
c=range(5,10,2)
for i in c:
    print(i)
