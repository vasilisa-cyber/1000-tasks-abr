n = int(input("Введите трёхзначное число = "))
first_number = n // 100
middle_number = (n // 10) % 10
last_number = n % 10
first_number , middle_number , last_number = last_number , middle_number , first_number
print(first_number , middle_number , last_number)