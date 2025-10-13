import sys

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

def add(a,b):
    res = a+b
    return res

def sub(a,b):
    res = a-b
    return res

def mul(a,b):
    res = a*b
    return a*b

def div(a,b):
    res = a/b
    return res

def mod(a,b):
    res = a%b
    return res

if operation == "add":
    output = add(num1, num2)
    print(output)
elif operation == "sub":
    output = sub(num1, num2)
    print(output)
elif operation == "mul":
    output = mul(num1, num2)
    print(output)
elif operation == "div":
    output = div(num1, num2)
    print(output)
elif operation == "mod":
    output = mod(num1, num2)
    print(output)