# Write a program that prints all unique combinations of 1, 2 and 3.

i = 1
while i <= 3:
    j = 1
    while j<=3:
        k = 1
        while k <= 3:
            if i == j or j == k or k == i:
                k += 1
                continue
            else:
                print(i, j , k)
            k += 1
        j += 1
    i += 1




# better way
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            if i != j and j != k and k != i:
                print(i, j, k)
