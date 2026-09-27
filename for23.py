X = float(input("X= "))
N = int(input("N= "))

sum = 1
fact = 1
for i in range (N + 1):
    sum = sum + ((-1) ** i) * (X ** (2 * i + 1)) / fact
    fact = fact * (2 * i + 2) * (2 * i + 3)
print(sum)