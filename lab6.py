import math
import os
import time

# 1


def multiply_list(lst):
    return math.prod(lst)


print(multiply_list([1, 2, 3, 4, 5]))

# 2


def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower


print(count_case("Hello World!"))

# 3


def is_palindrome(s):
    return s == s[::-1]


print(is_palindrome("madam"))
print(is_palindrome("hello"))

# 4


def sqrt_after_delay(num, ms):
    time.sleep(ms / 1000)
    return math.sqrt(num)


print(sqrt_after_delay(16, 1000))

# 5


def all_true(tpl):
    return all(tpl)


print(all_true((True, True, False)))
print(all_true((True, True, True)))

# 6


def list_files_dirs(path):
    dirs = [d for d in os.listdir(
        path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(
        path) if os.path.isfile(os.path.join(path, f))]
    return dirs, files, dirs + files


print(list_files_dirs("."))

# 7


def check_access(path):
    return {
        'exists': os.path.exists(path),
        'readable': os.access(path, os.R_OK),
        'writable': os.access(path, os.W_OK),
        'executable': os.access(path, os.X_OK)
    }


print(check_access("test.txt"))

# 8


def path_info(path):
    if os.path.exists(path):
        return os.path.basename(path), os.path.dirname(path)
    return None


print(path_info("test.txt"))

# 9


def count_lines(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for _ in file)


# Создаём тестовый файл
with open("test.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\n")

print(count_lines("test.txt"))

# 10


def write_list_to_file(lst, file_path):
    with open(file_path, 'w') as file:
        file.writelines(f"{item}\n" for item in lst)


write_list_to_file(["Apple", "Banana", "Cherry"], "fruits.txt")

# 11


def generate_files():
    for i in range(26):
        open(f"{chr(65 + i)}.txt", 'w').close()


generate_files()

# 12


def copy_file(src, dest):
    with open(src, 'r') as source:
        with open(dest, 'w') as destination:
            destination.write(source.read())


copy_file("test.txt", "copy.txt")

# 13


def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        return True
    return False


print(delete_file("copy.txt"))
