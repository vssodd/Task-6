a = int(input('Enter number a: '))
b = int(input('Enter number b: '))
total = 0
count = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        total += i
        count += 1
        print(total / count)

x = int(input('Enter a number: '))

for i in range(1, x + 1):
    tens = i // 10
    units = i % 10
    if i == 3 * tens * units:
        print(i)
