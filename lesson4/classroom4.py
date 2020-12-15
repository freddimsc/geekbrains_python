from sys import argv


def my_script(a, b):
    return a / b


full_path, a, b = argv


print(my_script(int(a),int(b)))