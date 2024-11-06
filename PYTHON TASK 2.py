num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
operator=input("Enter operator (+,-,*,/)")
if operator == "+":
    add=num1+num2
    print("Addtion of",num1,"and",num2,"is:",add)
elif operator == "-":
    subtract=num1-num2
    print("Subtracion of",num1,"and",num2,"is:",subtract)
elif operator == "*":
    multiply=num1*num2
    print("Multiplication of",num1,"and",num2,"is:",multiply)
elif operator == "/":
    divide=num1/num2
    print("Division of",num1,"and",num2,"is:",divide)
else:
    print("Enter a valid operator")
