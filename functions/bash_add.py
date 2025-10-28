import os

def add(a, b):
    return os.popen(f"echo $(({a} + {b}))").read().strip()

add(1, 2)