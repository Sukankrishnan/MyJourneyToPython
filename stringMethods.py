#various string methods available in python

sentence = "John is a Teenager"

print(sentence)
print(sentence.upper()) # converts to upper case
print(sentence.lower()) #converts to lower case
print(sentence.find('o')) # it returns index of alphabet 'o'
print(sentence.replace('Teenager', 'boy'))
print("John" in sentence) # "in" operator is used to check the value is present
print(sentence.strip()) # removes any leading and trailing spaces
print(sentence.split()) # splits the string based on space and returns a list
print(sentence.capitalize()) # capitalizes the first letter of the string
print(sentence.count('e')) # counts the number of times 'e' appears in the string
print(sentence.startswith('John')) # checks if the string starts with 'John'
print(sentence.endswith('Teenager')) # checks if the string ends with 'Teenager'
print(sentence.isalpha()) # checks if all characters in the string are alphabets
print(sentence.isdigit()) # checks if all characters in the string are digits
print(sentence.title()) # converts the first character of each word to uppercase
print(sentence.center(50)) # centers the string within a field of given width
print(sentence.encode()) # encodes the string into bytes
print(sentence.format()) # formats the string (useful for inserting variables)