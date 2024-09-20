first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(i) - len(j)) for i, j in zip(first, second) if len(i) != len(j))
second_result = (len(first[x]) == len(second[y]) for x in range(len(first)) for y in range(len(second)) if x == y)

print(list(first_result))
print(list(second_result))
