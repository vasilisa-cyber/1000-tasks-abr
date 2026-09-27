X = float(input("X= "))
N = int(input("N= "))

sum = 0
for i in range (0, N + 1):
    sum = sum + ((-1) ** i) * (X ** (2 * i +,1)) / (2 * i + 1)
print(sum)