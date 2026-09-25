n = int(input("Введите трёхзначное число = "))
first_number = n // 100
middle_number = (n // 10) % 10
last_number = n % 10
sum = first_number + middle_number + last_number
prod = first_number * middle_number * last_number
print(sum , prod)