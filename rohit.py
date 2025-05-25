number = input("Enter a number: ")
if number.startswith("0b") or number.startswith("0B"):
    base = 2
    try:
        int(number, base)
        print("The number system is: Binary")
    except ValueError:
        print("Invalid binary number")
elif number.startswith("0o") or number.startswith("0O"):
    base = 8
    try:
        int(number, base)
        print("The number system is: Octal")
    except ValueError:
        print("Invalid octal number")
elif number.startswith("0x") or number.startswith("0X"):
    base = 16
    try:
        int(number, base)
        print("The number system is: Hexadecimal")
    except ValueError:
        print("Invalid hexadecimal number")
else:
    base = 10
    try:
        int(number)
        print("The number system is: Decimal")
    except ValueError:
        print("Invalid decimal number")