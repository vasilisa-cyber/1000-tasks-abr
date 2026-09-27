P = float(input("P= "))
dist = 10
sum = 0
K = 1
while sum < 200:
    dist = dist + dist * P / 100
    sum += sum + dist
    K = K + 1
    
print(K, S)