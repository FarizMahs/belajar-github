num1 = float(input("Input 1st number: "))
print("""
+
x
-
/
""")

choosetype = input("Choose one: ")
num2 = float(input("Input 2nd number: "))

if choosetype == "+":
    result = num1 + num2
    print(result)

elif choosetype == "x":
    result = num1 * num2
    print(result)

elif choosetype == "-":
    result = num1 - num2
    print(result)

elif choosetype == "/":
    if num2 != 0:
        result = num1 / num2
        print(result)
    else:
        print("Cannot divide by zero.")

else:
    print("Please choose a valid option.")

