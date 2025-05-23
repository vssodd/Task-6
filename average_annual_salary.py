total_salary = 0

for month in range(1, 13):
    monthly_salary = int(input('Enter salary for the month: '))
    total_salary += monthly_salary

average_salary = total_salary / 12
print('Average annual salary:', average_salary)
