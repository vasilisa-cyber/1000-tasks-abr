N = int(input("N= "))
K = 0
prod = 1
while prod * 3 < N:
    prod *= 3
    K += 1
print(K)