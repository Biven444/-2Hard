from sys import excepthook


def generate_password(n):
    password= ''
    for i in range(1,n):
        for j in range(i + 1, n ):
            if n % ( i + j) == 0:
                password += str(i) + str(j)
    return password
while True:
    try:
        a = int(input('Введите число от 3 до 20: '))
        if 3 <= a  and a <=20:
            break
        else:
            print('Число введено не верно')
    except ValueError:
        print()
print(generate_password(a))















