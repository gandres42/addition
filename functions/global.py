import subprocess

def add(a, b):
    # dynamically create variables
    stock_env = list(globals().keys())
    for i in range(int(a)): globals()[f"a_{i}"] = None
    for i in range(int(b)): globals()[f"b_{i}"] = None
    saved_globals = {k: v for k, v in globals().items() if k not in stock_env}

    global_count = 0
    for var_name in ['a', 'b']:
        sub_count = 0
        while True:
            code = f"""
globals().update({saved_globals})
try:
    {var_name}_{sub_count}
except NameError:
    exit(1)
"""
            result = subprocess.run(["python", "-c", code], capture_output=True)
            if result.returncode != 0: break
            sub_count += 1
        global_count += sub_count
        
    return global_count

print(add(12, 4))