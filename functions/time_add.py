import time

def add(a, b):
    start_time = time.monotonic()
    time.sleep(a)
    time.sleep(b)
    return round(time.monotonic() - start_time, 3)

print(add(1.32, 2.64))