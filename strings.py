#use 3 single or doublequotes for multi line strings
multiLineString="""This is a multi line string.
It can span multiple lines.
It preserves the line breaks and spaces."""
print(multiLineString)

#Slicing
inputString="This sentence is to practice string slicing."
#slices from index 2 to 9
print("Sliced string from index 2 to 9:", inputString[2:10])
#slices from index 5 to the end
print("Sliced string from index 5 to end:", inputString[5:])
#slices from the beginning to index 15
print("Sliced string from beginning to index 15:", inputString[:16])
#slices the entire string
print("Sliced entire string:", inputString[:])
#negative indexing - starts from the end
print("Sliced string using negative indexing from -10 to -1:", inputString[-10:-1])