# number 1
print("hello everynyan")

# syntax
if 5 > 2:
    print("Five is greater than two! Ez")

# this is a comment

# Variables
x = 69
y = "John SINA"
print(x)
print(y)

x, y, z, k = "Pen", "Pineapple", "Apple", "Pen"
print(x)
print(y)
print(z)
print(k)
# Data types
x = 3
print(type(x))


# numbers
x = 1
y = 1.2
z = 1j

print(type(x))
print(type(y))
print(type(z))

# Casting
x = int(1)   # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3

# String
print("Salam")
print('Salam')

print("Everything is fine")
print("He is nicknamed 'Johnny'")
print('He is also called "Johnny"')

a = "HEY"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Пример 1
x = "John"
y = "John"
print(x, y)

# Пример 2
x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()

# Пример 3
x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()
print("Python is " + x)

# Пример 4
x = "awesome"


def myfunc():
    global x
    x = "fantastic"


myfunc()
print("Python is " + x)
