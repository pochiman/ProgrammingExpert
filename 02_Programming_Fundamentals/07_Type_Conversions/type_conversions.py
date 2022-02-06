x = "4"
y = int(x) + 4
print(type(y))
print(type(x))
print(y)

y = int("4") + 4
print(y)

y = float("4.5") + 4
print(y)

y = float("4") + 4
print(y)

y = int(4.7)
print(y)

y = bool("0")
print(y)

y = bool("")
print(y)

y = bool(" ")
print(y)

y = bool(-9)
print(y)

y = bool(0)
print(y)

y = str(0) + "0"
print(y)

y = str(1) + "0"
print(y)

number = input("Enter a number: ")
result = int(number) + 5
print("The result is:", result)

number = input("Enter a number: ")
result = float(number) + 5
print("The result is:", result)