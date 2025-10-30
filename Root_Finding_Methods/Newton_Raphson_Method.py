import math
def f1(x):
    return math.exp(-x) - x
def f2(x):
    return -math.exp(-x) - 1

prev = 0

for i in range(1, 11):
    x = prev - f1(prev) / f2(prev)
    err = abs(x - prev)
    prev = x
    print(f"Iteration num : {i}  current_root: {x:.5f}  Abs_err: {err:.8f}")
