X = float(input("X= "))
N = int(input("N= "))

sum = 1
fact = 1
for i in range (1, N +1):
    fact = fact * (2 * i - 1) * (2 * i)
    sum = sum + ((-1) ** i) * (X ** (2 * i)) / fact
    
print(sum)