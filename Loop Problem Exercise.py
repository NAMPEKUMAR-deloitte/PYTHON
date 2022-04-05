#a
n = int(input())
for i in range(n):
    print(''.join(map(str,str(11**i))),end="")
    print('0'*(n-i-1))

#b
h = eval(input())

for x in range(h):
    print(" " * (h - x), "*" * (2*x + 1))
for x in range(h - 2, -1, -1):
    print(" " * (h - x), "*" * (2*x + 1))

#c
row = int(input())

for i in range(row):
    for j in range(row - i):
        print(' ', end='')

    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == row - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
rows = int(input())
for i in range(0, rows):
    for j in range(0, rows):
        if i == 0 or j == (rows-1) or j == i:
            print('*', end='')
        else:
            print(' ', end='')
    print()