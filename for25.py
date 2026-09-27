X = float(input("X= "))
N = int(input("N= "))

sum = 0
for i in range (1, N + 1):
    sum = sum + ((-1) **(i - 1)) * (X ** i) / i
print(sum)