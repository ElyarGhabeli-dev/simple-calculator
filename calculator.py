def plus(n_1,n_2):
    return n_1+n_2

def minus(n_1,n_2):
    return n_1-n_2

def multiplication(n_1,n_2):
    return n_1*n_2

def division(n_1,n_2):
    return n_1/n_2

n_1 = int(input('عدد خود را وارد کنید :'))

while True:
    o = input("یکی از چهار عملیات اصلی را وارد کنید ( + - * /) : ")
    if o == '+':
        n_2 = int(input('عدد خود را وارد کنید :'))
        n_1 = plus(n_1,n_2)
    elif o == '-':
        n_2 = int(input('عدد خود را وارد کنید :'))
        n_1 = minus(n_1,n_2)
    elif o == '*':
        n_2 = int(input('عدد خود را وارد کنید :'))
        n_1 = multiplication(n_1,n_2)
    elif o == '/':
        n_2 = int(input('عدد خود را وارد کنید :'))
        n_1 = division(n_1,n_2)
    else:
        break
    print(n_1)