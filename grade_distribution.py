students = int(input('Enter the number of students in the class: '))
excellent_count = 0
good_count = 0
satisfactory_count = 0

for _ in range(students):
    grade = int(input('Enter the grade: '))
    if grade == 5:
        excellent_count += 1
    elif grade == 4:
        good_count += 1
    else:
        satisfactory_count += 1

if excellent_count > good_count and excellent_count > satisfactory_count:
    print('There are the most excellent grades.')
elif good_count > excellent_count and good_count > satisfactory_count:
    print('There are the most good grades.')
else:
    print('There are the most satisfactory grades.')
