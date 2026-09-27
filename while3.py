N = float(input("N= "))
K = float(input("K= "))
count = 0
While N >= K:
N -= K
count += 1
print(count, N)