"""
Задача №1
Напишіть функцію,
яка створює комбінацію двох послідовностей таким чином як у вихідних даних.
Вхідні дані:
1 2 3 4 5
a b c d e
Вихідні дані:
1 a 2 b 3 c 4 d 5 e
Автор: Мотовилець Марія
"""
def solution():
    n1 = input("Введіть послідовність 1: ").split()
    n2 = input("Введіть послідовність 2: ").split()
    comb = n1 + n2
    res = []
    len1 = len(n1)
    len2 = len(n2)
    
    i = 0
    if len1 < len2:
        limit = len1
    else:
        limit = len2
    while i < limit:
        res.append(n1[i])
        res.append(n 2[i])
        i += 1
    return ' '.join(res)

res = solution()
print(res)
