N = int(input("Введите число: "))
final_sum = 0
for i in range((2 * N) + 1):
    final_sum += i ** 2
print(final_sum)