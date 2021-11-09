num1 = float(input())
num2 = float(input())
op = input()
zero_msg = "Division by 0!"

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2 if num2 != 0.0 else zero_msg)
elif op == "*":
    print(num1 * num2)
elif op == "mod":
    print(num1 % num2 if num2 != 0.0 else zero_msg)
elif op == "pow":
    print(num1 ** num2)
elif op == "div":
    print(num1 // num2 if num2 != 0.0 else zero_msg)
