N = int(input('Введите количество карточек: '))
sum = 0
for i in range(1, N):
    remaining_card = int(input('Введите номер оставшейся карточки: '))
    sum += remaining_card
total = (N * (N + 1)) // 2
print('Номер пропавшей карточки:', total - sum)
