What do you understand by this?


>>> print("you can do it")
you can do it
>>> a='1'
>>> s=int(a);
>>> print(s)
1
>>> b = 1
>>> if a == b
  File "<python-input-5>", line 1
    if a == b
             ^
SyntaxError: expected ':'
>>> if a == b
  File "<python-input-6>", line 1
    if a == b
             ^
SyntaxError: expected ':'
>>> if a == b print("true")
  File "<python-input-7>", line 1
    if a == b print("true")
              ^^^^^
SyntaxError: invalid syntax
>>> if a == b
  File "<python-input-8>", line 1
    if a == b
             ^
SyntaxError: expected ':'
>>> if a == b:
...     print("yes, a equals b")
... else:
...     print("a is not equal to b")
...
a is not equal to b
>>>

"""
1. Printing in the print() function.
2. Converting string to integer as 's' and printing the integer value
3. Colon an corresponding code block is missing in if condition
Syntax:
if(condition): 
    codeblock (indentation of 4 spaces)
Solution:  
if a==b:
    print("same")
    
4. a is a string and b is an integer. If syntax is wrong
Solution:
if int(a)==b:
    print("same")

5. Should be careful in indentation. Syntax includes indentation
if a==b:
    print("true")
    
6. Wrong syntax

7. Correct syntax. a is string and b is integer. So, both are not equal.
"""