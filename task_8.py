n = int(input("Введите число N "))
k = int(input("Введите степень K "))

def summa(n, k):
    x = sum(i ** k for i in range(n+1))
    return x

print("Результат: " + str(summa(n,k)))