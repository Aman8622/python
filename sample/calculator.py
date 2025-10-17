print("Simple Calculator \n")

a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))
ch = input("Enter the operation to perform : ")

def add():
    res = a+b
    return res

def sub():
    res = a-b
    return res

def mul():
    res = a*b
    return a*b

def div():
    res = a/b
    return res

def mod():
    res = a%b
    return res

match ch:
    case '+':
        res = add()
        print(str(a) + " + " + str(b) + " = " + str(res))
    case '-':
        res = sub()
        print(str(a) + " - " + str(b) + " = " + str(res))
    case '*':
        res = mul()
        print(str(a) + " * " + str(b) + " = " + str(res))
    case '/':
        res = div()
        print(str(a) + " / " + str(b) + " = " + str(res))
    case '%':
        res = mod()
        print(str(a) + " % " + str(b) + " = " + str(res))
    case _:
        print("enter valid operator")