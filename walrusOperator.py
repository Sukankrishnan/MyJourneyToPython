#walrus operator introduced in python 3.8

while (x:=input("Enter text"))!=3:
    print(f"{x} is greater than 3")
    print(x)

numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")