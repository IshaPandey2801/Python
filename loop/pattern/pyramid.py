i = 1

while i <=4:
    #space
    j = 1
    while j <= 4-i:
        print(" ", end="")
        j += 1
    
    # star
    k = 1
    while k <= i:
        print("*", end=" ")
        k += 1
    print()
    i += 1



