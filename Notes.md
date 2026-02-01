print("The sums\rstring\n num of \"two numbers\" is ", a+b) 
#\r is carriage return. It will overwrite the line from the beginning. "The sum"<7 char> is overwritten by "string"<6 char>. "m" remains. So, the output is 
stringm
num of "two numbers" is 10

To print on the same line, use end parameter (Output is "Hello World")
print("Hello", end=" ")
print("World")

To print type of variable print(type(var))