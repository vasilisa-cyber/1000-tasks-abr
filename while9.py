N = int(input("N= "))
K = 0
prod = 1
while prod <= N:
    prod *= 3
    K += 1
print(K)