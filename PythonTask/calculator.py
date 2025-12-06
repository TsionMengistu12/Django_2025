print("##### Welcome to calculator #####")
num1 = int(input("please enter first number "))
operator = input("enter operator ")
num2 = int(input("please enter second number "))
# print(num1, num2, operator)

def sum(n1, n2):
    return n1 + n2

def div(n1, n2):
    return n1 / n2

def multi(n1, n2):
    return n1 * n2

def sub(n1, n2):
    return n1 - n2

if operator == "+":
    print("their sum is ", sum(num1, num2))
elif operator == "*":
    print("their multiple is ",multi(num1, num2))
elif operator == "/":
    print("their qoutient is ",div(num1, num2))
elif operator == "-":
    print("their difference is ",sub(num1, num2))
else:
    print("invalid operator")
