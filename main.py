first = int(input('Введите значение first:'))
second = int(input('Введите значение second:'))
third = int(input('Введите значение third:'))
if first == second and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)