k = int(input("Введіть кількість кошиків: "))
m, n = map(int, input('Введіть вагу винограду: ').split())
kg1 = m * k
gr1 = n * k

a = int(input("Введіть кількість кошиків: "))
b, c = map(int, input('Введіть вагу винограду: ').split())
kg2 = b * a
gr2 = c * a

kg = kg1 + kg2
gr = gr1 + gr2

while gr >= 1000:
    gr = gr - 1000
    kg = kg + 1

print("Дівчинка зібрала:", kg, "кг", gr, "гр", "винограду")
