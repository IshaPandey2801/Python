"""
Write a program that generates the following output using a for loop:
A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z
z, y, x, w, v, u, t, s,......., a
"""

for alpha in range(65, 91):
    print(chr(alpha), end = ", ")
print()
for alpha in range(122, 96, -1):
    print(chr(alpha), end = ", ")

