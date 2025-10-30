rows = 4
cols = 4
x = [0, 1, 2, 3]
y = [1, 2, 4, 8]

matrix = [[0] * cols for _ in range(rows)]

for i in range(4):
    matrix[i][0] = y[i]

for i in range(1, 4):
    for j in range(4 - i):
        matrix[j][i] = (matrix[j + 1][i - 1] - matrix[j][i - 1]) / (x[j + i] - x[j])

print("\n--- FINAL UPDATED MATRIX ---\n")
for i in range(4):
    print(matrix[i])

xx = 2.1
ans = 0

for i in range(4):
    p = 1
    for j in range(i):
        p *= (xx - x[j])
    p *= matrix[0][i]
    ans += p

print(f"\nEstimated value at x = {xx} is {ans}")
