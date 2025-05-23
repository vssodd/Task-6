N = int(input('Enter a number: '))
factorial = 1

for number in range(1, N + 1):
    factorial *= number

print(f'The factorial of {N} is {factorial}')
