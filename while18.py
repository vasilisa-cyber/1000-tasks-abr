P = float(input("P= "))
count = 0
sum = 0
K = 1
while N > 0:
    ost = N % 10
    sum += sum + ost
    count = count + 1
    N = N // 10
print(count, S)