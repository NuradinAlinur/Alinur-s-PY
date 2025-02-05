# Funtions
def my_function():
    print("KYS- Kiss your ass")


my_function()


def my_function():
    print("KYS- Kiss YOur Sister")


def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Emil", "Refsnes")


def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Licufer")


def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Lox")


def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Kazakhstan")
my_function("Brazil")


def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("Recursion Example Results:")
tri_recursion(6)

# Lambda


def x(a): return a + 10


print(x(5))


def x(a, b, c): return a + b + c


print(x(69, 69, 69))


def x(a, b): return a * b


print(x(69, 69))


def x(a, b, c): return a + b + c


print(x(66, 55, 44))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(22))
print(mytripler(33))

# Classes and Objects


class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# Inheritance


class Person:

    def __init__(self, fname, lname):

        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("Alinur", "Nuradin")
x.printname()
