X = float(input("X= "))
N = int(input("N= "))
sum = 1
fact = 1
for i in range (1, N +1):
    fact = fact * i
    sum = sum + (X ** i) / fact
print(sum)