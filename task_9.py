mas = [1, 2, 4, 6, 3, 7, 11, 10, 31, 16, 29, 20, 14]
mas1 = []
mas2 = []

def res(mas):
    mas3 = []
    for i in range(len(mas)):
        if i % 2 == 0:
            mas1.append(mas[i])
        else:
            mas2.append(mas[i])
    mas3 = mas1 + mas2
    return mas3

print(mas1)
print(mas2)
print(mas)
print(res(mas))