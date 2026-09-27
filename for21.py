N = int(input("N= "))

sum = 1
fact = 1
for i in range(2, N + 1):
    fact = fact + i
    sum = sum + 1 / fact
print(sum)