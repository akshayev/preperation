operator = input("enter the operator (+,-,*,/)")


n1 = float(input("enter the number 1 : "))
n2 = float(input("enter the number 2 : "))

if operator == "+":
    result = n1 + n2
elif operator == "-":
    result = n1 - n2
elif operator == "*":
    result = n1 * n2
elif operator == "/":
    if n2 == 0:
        result = "error : division by zero"
    else:
        result = n1 / n2
else:
    result = "error : invalid operator"
    
print(result)