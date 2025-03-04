import math
import os
import time

# 1


def multiply_list(lst):
    return math.prod(lst)

# 2


def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

# 3


def is_palindrome(s):
    return s == s[::-1]

# 4


def sqrt_after_delay(num, ms):
    time.sleep(ms / 1000)
    return math.sqrt(num)

# 5


def all_true(tpl):
    return all(tpl)

# 6


def list_files_dirs(path):
    dirs = [d for d in os.listdir(
        path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(
        path) if os.path.isfile(os.path.join(path, f))]
    return dirs, files, dirs + files

# 7


def check_access(path):
    return {
        'exists': os.path.exists(path),
        'readable': os.access(path, os.R_OK),
        'writable': os.access(path, os.W_OK),
        'executable': os.access(path, os.X_OK)
    }

# 8


def path_info(path):
    if os.path.exists(path):
        return os.path.basename(path), os.path.dirname(path)
    return None

# 9


def count_lines(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for _ in file)

# 10


def write_list_to_file(lst, file_path):
    with open(file_path, 'w') as file:
        file.writelines(f"{item}\n" for item in lst)

# 11


def generate_files():
    for i in range(26):
        open(f"{chr(65 + i)}.txt", 'w').close()

# 12


def copy_file(src, dest):
    with open(src, 'r') as source:
        with open(dest, 'w') as destination:
            destination.write(source.read())

# 13


def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        return True
    return False
