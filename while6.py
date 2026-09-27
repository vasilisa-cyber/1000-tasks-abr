N = int(input("N= "))

prod = 1
while N > 1:
    prod = prod * N
    N = N - 2
print(prod)