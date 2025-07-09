import os
from time import sleep as s

try:
    def add(num1,num2):
        print(f"\n{num1}+{num2} = {num1+num2}")

    def Subtract(num1,num2):
        print(f"\n{num1}-{num2} = {num1-num2}")

    def Multiply(num1,num2):
        print(f"\n{num1}*{num2} = {num1*num2}")

    def Divide(num1,num2):
        try:
            print(f"\n{num1}/{num2} = {num1/num2}")

        except ZeroDivisionError:
            print("\nCannot divide a number with Zero")

    def Reminder(num1,num2):
        print(f"\n{num1}%{num2} = {num1%num2}")

    def power(num1,num2):
        print(f"\n{num1}**{num2} = {num1**num2}")
        

    while True:
        os.system('cls')
        try:
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))

        except ValueError:
            input("\nEnter a valid option\nPress Enter to continue")
            continue

        while True:     
                    choice = int(input('''
--- Press Ctrl+C to quit ---
What would you like to do?
1. Add
2. Subtract
3. Multiply
4. Divide
5. Remainder
6. Power
Enter your choice : '''))

                    if choice == 1:
                        add(number1, number2)

                    elif choice == 2:
                        Subtract(number1, number2)

                    elif choice == 3:
                        Multiply(number1, number2)

                    elif choice == 4:
                        Divide(number1, number2)

                    elif choice == 5:
                        Reminder(number1, number2)

                    elif choice == 6:
                        power(number1, number2)

                    else:
                        input("\nEnter a valid option\nPress Enter to continue")
                        continue
                    
                    if not(input("\n" \
                    "To continue with the same number enter y if not leave it blank")):
                        break

                    else:
                        os.system('cls')
                        print(f'number 1 ={number1}')
                        print(f'number 2 ={number2}')



except KeyboardInterrupt:
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in "Thanks for using":
        s(0.07)
        print(i,end = '')
    quit()