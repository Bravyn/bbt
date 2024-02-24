def calculator():
    print("Select Math Operation")
    print("1. Add ")
    print("2. Subtract ")
    print("3. Multiply ")
    print("4. Divide ")

    choice = input("Enter choice: ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Results: ", num1 + num2)
    elif choice == "2":
        print("Results: ", num1 - num2)
    elif choice == "3":
        print("Results: ", num1 * num2)
    elif choice == "4":
        if num2 == 0:
            print("Error: division by 0 not possible, yet")
        
        else:
            print("Results: ", num1 / num2)
    else:
        print("Invalid input")


calculator()
    