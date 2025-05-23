x = int(input('Введите число: '))
for i in range(1, x + 1):
    a = i // 10  # Tens digit
    b = i % 10   # Units digit
    if i == 3 * a * b:
        print(i)
