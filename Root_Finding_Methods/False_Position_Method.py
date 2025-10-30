import math
def f(x):
    return x**2 - 2

a = 1
b = 2
r = math.sqrt(2)
tolarance = 0.0001

for i in range(1, 101):
    c = (a * f(b) - b * f(a)) / (f(b) - f(a))
    err = abs(r - c)
    print(f"iter {i}: app_root: {c:.8f} error: {err:.8f}")

    if err < tolarance:
        break
    if f(c) > 0:
        b = c
    else:
        a = c
