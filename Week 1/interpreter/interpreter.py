exp = input("Expression: ")
exp = exp.split(" ")
sign = exp[1].strip()
num1 = exp[0].strip()
num2 = exp[2].strip()
num1 = float(num1)
num2 = float(num2)

if (sign == '+'):
    result = num1 + num2
elif (sign == '-'):
    result = num1 - num2
elif (sign == '*'):
    result = num1 * num2
elif (sign == '/'):
    result = num1 / num2

print(f"{result:.1f}")