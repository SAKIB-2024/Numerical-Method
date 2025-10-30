import math
def f1(x):
    return math.exp(-x) - x
def f2(x):
    return -math.exp(-x) - 1

prev = 0
tolarance = 0.001

for i in range(1, 11):
    x = prev - f1(prev) / f2(prev)
    err = abs(x - prev)
    prev = x
    if err < tolarance:
        print(f"Iteration {i}")
        break
    
print(x)
