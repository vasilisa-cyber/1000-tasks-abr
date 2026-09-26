N = int(input("N= "))
sum = 0
fact = 1
for i in range(1, N + 1):
    fact = fact * i
    sum = sum + fact
print(sum)