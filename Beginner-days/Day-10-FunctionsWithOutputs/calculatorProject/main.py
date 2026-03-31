from art import logo

def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
def mod(n1, n2):
    return n1 % n2
def pow(n1, n2):
    return n1 ** n2

continue_flag = True

print(logo)

result = input("Enter first number: ")
answer = int(result)

while continue_flag:
    print(f"{result}")
    operator = input("""Select the operator(write the simbol):
    | + | - | * | / | % | ^ | = | AC | OFF | """)

    if operator in ["+", "-", "*", "/", "%", "^", "=", "AC", "OFF"]:
        if operator == "AC":
            result = input("Enter first number: ")
            answer = int(result)
        elif operator == "=":
            continue_flag = False
            result += "=" + str(answer)
        else:
            num2 = int(input("Enter second number: "))
            result += operator + str(num2)
            if operator == "+":
                answer += num2
            if operator == "-":
                answer -= num2
            if operator == "*":
                answer += mul(answer, num2)
            if operator == "/":
                answer += div(answer, num2)
            if operator == "%":
                answer += mod(answer, num2)
            if operator == "^":
                answer += pow(answer, num2)
    else:
        continue_flag = False
print(result)
