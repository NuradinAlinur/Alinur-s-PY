import re

# 1
pattern1 = r'a*b'
def match_pattern1(s):
    return bool(re.fullmatch(pattern1, s))

# 2
pattern2 = r'a{1}b{2,3}'
def match_pattern2(s):
    return bool(re.fullmatch(pattern2, s))

# 3
pattern3 = r'^[a-z]+_[a-z]+$'
def match_pattern3(s):
    return bool(re.fullmatch(pattern3, s))

# 4
pattern4 = r'[A-Z][a-z]+'
def match_pattern4(s):
    return re.findall(pattern4, s)

# 5
pattern5 = r'a.*b$'
def match_pattern5(s):
    return bool(re.fullmatch(pattern5, s))

# 6
def replace_delimiters(s):
    return re.sub(r'[ ,.]', ':', s)

# 7
def snake_to_camel(s):
    return ''.join(word.title() for word in s.split('_'))

# 8
def split_uppercase(s):
    return re.split(r'(?=[A-Z])', s)

# 9
def insert_spaces(s):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)

# 10
def camel_to_snake(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
