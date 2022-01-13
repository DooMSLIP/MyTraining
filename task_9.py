mas = [1, 2, 4, 6, 3, 7, 11, 10, 31, 16, 29, 20, 14]
mas1 = []
mas2 = []


def res(mas):
    for i in range(len(mas)):
        if mas[i] % 2 == 0:
            mas1.append(mas[i])
        else:
            mas2.append(mas[i])
    return mas1, mas2

print(res(mas))
