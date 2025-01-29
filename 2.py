# Booleans
# Example 1
print(8 > 6)
print(5 == 7)
print(4 < 2)

# Example 2
a = 150
b = 300

if b > a:
    print("b is larger than a")
else:
    print("b is smaller or equal to a")

# Example 3
print(bool("World"))
print(bool(20))

x = "Python"
y = 50

print(bool(x))
print(bool(y))

# Example 4
print(bool("xyz"))
print(bool(456))
print(bool(["grape", "mango", "pear"]))

# Example 5
print(bool(False))
print(bool(None))
print(bool(-1))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# Example 6


class myclass():
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))

# Example 7


def myFunction():
    return False


print(myFunction())

if myFunction():
    print("SUCCESS!")
else:
    print("FAILURE!")

# Example 8
x = 123
print(isinstance(x, float))

# Operators
# Example 1
x = 10
x += 4
x -= 2
x *= 3
x /= 6
x %= 2
x //= 1
x **= 2
print(x)

# Example 2
print(20 == 15)
print(7 != 5)
print(9 > 6)
print(3 < 10)
print(8 >= 8)
print(12 <= 18)

# Example 3
a = 12
b = 7
print(a > 10 and b < 10)
print(a < 15 or b > 10)
print(not (a == 12 and b > 5))

# Example 4
x = ["cat", "dog"]
y = ["cat", "dog"]
z = x
print(x is z)
print(x is not y)
print(x == y)

# Example 5
colors = ["red", "green", "blue"]
print("green" in colors)
print("yellow" not in colors)

# Example 6
a = 6  # 0110 in binary
b = 3  # 0011 in binary
print(a & b)
print(a | b)
print(a ^ b)
print(~b)
print(a << 2)
print(b >> 1)

# Example 7
print((3 + 2) * (7 - 5))
print(15 + 5 * 3)
print(8 - 4 + 2 - 1)

# Lists
thislist = ["Pen", "PineApple", "Apple", "Pen"]
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "bandana", "chopper"]
print(thislist[1])

thislist = ["kiwi", "banana", "shery", "shery", "lady", "melon", "water"]
print(thislist[2:5])

thislist = ["Pen", "PineApple", "Pen"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")


thislist = ["apple", "banana", "assesiation"]
thislist[1] = "pipe"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["IRAK", "waterAfrica"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "boxofcheese")
print(thislist)


thislist = ["apple", "banana", "cherry"]
thistuple = ("kira", "Light")
thislist.extend(thistuple)
print(thislist)


thislist = ["aaaapple", "banana", "cherry"]
thislist.clear()
print(thislist)

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

thislist = ["reserse", "nigger "]
thislist.reverse()
print(thislist)

thislist = ["is BIG"]
mycock = thislist[:]
print(mycock)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# Tuples
thistuple = tuple(("ban", "goro", "gggg"))

print(thistuple)

thistuple = ("apes", " is not ", "dumb")
if "apes" in thistuple:
    print("Yes", "You are Bananas")

x = ("HILE", "HILE", "cherry")
y = list(x)
y[2] = "Hitler"
x = tuple(y)

print(x)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

niggers = ("Big weight", "Big Eyes", "BBB")
mytuple = niggers * 2
print(mytuple)

# Sets

thisset = set(("apple", "banana", "cherry"))
print(thisset)

thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

# Dictionareis

thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x)  # before the change

car["color"] = "white"

print(x)  # after the change

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"color": "red"})

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)

for x, y in thisdict.items():
    print(x, y)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# If else

x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

a = 33
b = 200
if b > a:
    print("b is greater than a")

a = 33
b = 200

if b > a:
    pass

# While Loops
i = 1
while i < 6:
    print(i)
    i += 1

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# For Loops
fruits = ["ape", "banana", "happy"]
for x in fruits:
    print(x)

fruits = ["apple", "banan", "banana"]
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    if x == "apple":
        continue

    print(x)

for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")

adj = ["black", "big", "cock"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
