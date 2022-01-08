n = 7

def printing(i):
    s = ''
    while i > 0:
        s = s + '*'
        i = i - 1
    print(s)
    

def print_triangle(n):
    i = 1
    while  i <= n:
        printing(i)
        i = i + 1      

print_triangle (n)
