x = {2: "hello", "1": 5}

print(x[2])     # hello
print(x["1"])   # 5

########## ########## ########## ########## ##########

x = {}

x["key"] = "value"

print(x)        # {'key': 'value'}
print(x["key"]) # value

########## ########## ########## ########## ##########

x = {"key": 1}

x["key"] = "value"

print(x["key"]) # value

########## ########## ########## ########## ##########

x = {"key": 1}

x["key2"] = "value"

print(x)        # {'key': 1, 'key2': 'value'}

########## ########## ########## ########## ##########

x = dict()

x["key2"] = "value"

print(x["key2"])    # value

########## ########## ########## ########## ##########

x = {1: 1, 2: 2, 3: 3}

del x[1]

print(x)        # {2: 2, 3: 3}

########## ########## ########## ########## ##########

x = {1: 1, 2: 2, 3: 3}

contains = 1 in x

print(contains) # True

########## ########## ########## ########## ##########

x = {2: 1, 3: 3}

values = x.values()

print(values)   # dict_values([1, 3])

########## ########## ########## ########## ##########

x = {2: 1, 3: 3}

values = list(x.values())

print(values[0])    # 1

########## ########## ########## ########## ##########

x = {2: 1, 3: 3}

keys = x.keys()

print(keys) # dict_keys([2, 3])

########## ########## ########## ########## ##########

x = {2: 1, 3: 3}

keys = list(x.keys())

print(keys[0])  # 2

########## ########## ########## ########## ##########

x = {2: 1, 3: 3}

items = x.items()

print(items)    # dict_items([(2, 1), (3, 3)])

########## ########## ########## ########## ##########

x = {2: 1, 3: 3}

items = list(x.items())

print(items)    # [(2, 1), (3, 3)]

########## ########## ########## ########## ##########

x = {2: 1, 3: 3}

print(len(x))   # 2

########## ########## ########## ########## ##########

x = {2: 1, 3: 3}

for key in x:
    value = x[key]
    print(key, value)

# 2
# 2 1
# 3 3

########## ########## ########## ########## ##########

x = {2: 1, 3: 3}

for key, value in x.items():
    print(key, value)

# 2 1
# 3 3

########## ########## ########## ########## ##########

x = {2: 1, 3: 3}

x[4] = x.get(4, 0) + 1

print(x)    # {2: 1, 3: 3, 4: 1}

########## ########## ########## ########## ##########

x = {2: 1, 3: 3, 4: 1}

x[4] = x.get(4, 0) + 1

print(x)    # {2: 1, 3: 3, 4: 2}

########## ########## ########## ########## ##########

characters = {}

string = "hello world"

for char in string:
    characters[char] = characters.get(char, 0) + 1

print(characters)   # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

########## ########## ########## ########## ##########

counts = {}

while True:
    num = input("Number (enter q to quit): ")

    if num == "q":
        break

    num = int(num)
    counts[num] = counts.get(num, 0) + 1

print(counts)

########## ########## ########## ########## ##########

d = {"a": 1, "b": 1, "c": 1, "d": 1}
l = ["a", "b", "c", "d"]

"d" in d

"d" in l