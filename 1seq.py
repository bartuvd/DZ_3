list_num = int(input('Введите количество элементов: '))
result = []
for i in range(list_num):
    num = int(input('Введите элемент: ' ))
    result.append(num)
result.sort()
print('Вывод:', result)

