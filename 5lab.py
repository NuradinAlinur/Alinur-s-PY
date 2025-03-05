import re

# 1
pattern1 = r'a*b'


def match_pattern1(s):
    return bool(re.fullmatch(pattern1, s))


print(match_pattern1("aaab"))  
print(match_pattern1("b"))     
print(match_pattern1("c"))     

# 2
pattern2 = r'a{1}b{2,3}'


def match_pattern2(s):
    return bool(re.fullmatch(pattern2, s))


print(match_pattern2("abb"))   
print(match_pattern2("abbb"))  
print(match_pattern2("a"))     

# 3
pattern3 = r'^[a-z]+_[a-z]+$'


def match_pattern3(s):
    return bool(re.fullmatch(pattern3, s))


print(match_pattern3("hello_world"))  
print(match_pattern3("Hello_World"))  

# 4
pattern4 = r'[A-Z][a-z]+'


def match_pattern4(s):
    return re.findall(pattern4, s)


print(match_pattern4("Hello World Test"))  

# 5
pattern5 = r'a.*b$'


def match_pattern5(s):
    return bool(re.fullmatch(pattern5, s))


print(match_pattern5("acb"))  
print(match_pattern5("ab"))   
print(match_pattern5("abc"))  

# 6
def replace_delimiters(s):
    return re.sub(r'[ ,.]', ':', s)


print(replace_delimiters("Hello, world. Python is great!"))  

# 7
def snake_to_camel(s):
    return ''.join(word.title() for word in s.split('_'))


print(snake_to_camel("hello_world_test"))  

# 8
def split_uppercase(s):
    return re.split(r'(?=[A-Z])', s)


print(split_uppercase("HelloWorldTest"))  

# 9
def insert_spaces(s):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)


print(insert_spaces("HelloWorldTest"))  

# 10
def camel_to_snake(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()


print(camel_to_snake("HelloWorldTest"))  
