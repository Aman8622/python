num1 = 5.2
num2 = 6.9
num3 = 4
num4 = 6

res1 = num1 + num2
res2 = num3 + num4
print("Float addition: ", round(res1,2))
print("Integer addition: ", res2)

res1 = num1 - num2
res2 = num3 - num4
print("Float subtraction: ", round(res1,2))
print("Integer subtraction: ", res2)

res1 = num1 * num2
res2 = num3 * num4
print("Float multiplication: ", res1)
print("Integer multiplication: ", res2)

res1 = num1 / num2
res2 = num3 // num4
res3 = num3 % num4
print("Float division: ", round(res1,2))
print("Integer division: ", res2)
print("Modulus: ",res3)

res4 = round(3.141592,2)
print("Rounded: ", res4)

res5 = abs(-7)
print(res5)