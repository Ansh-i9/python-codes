while True:
    car = int(input(" One: "))
    bike = int(input(" Two: "))
    op = input('Enter your op: "+","-","*": ')

    if op == "+":
        print(car + bike)
    elif op == "-":
        print(car - bike)
    elif op == "*":
        print(car * bike)
    else:
        print("⚠️ Invalid operator! Please use +, -, or *")
