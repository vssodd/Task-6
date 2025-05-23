even_positive = int(input('Enter a number: '))
count = 0

for number in range(even_positive):
    if number > 0 and number % 2 == 0:
        count += 1

print('Count of numbers that are both positive and even:', count)
