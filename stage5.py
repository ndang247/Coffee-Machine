water_in_machine = 400
milk_in_machine = 540
coffee_beans_in_machine = 120
disp_cups_in_machine = 9
money_in_machine = 550

def remaining():
    print("The coffee machine has:")
    print(water_in_machine, "of water")
    print(milk_in_machine, "of milk")
    print(coffee_beans_in_machine, "of coffee beans")
    print(disp_cups_in_machine, "of disposable cups")
    print("$" + str(money_in_machine), "of money")

def menu():
    choice = user_choice()
    while choice != "exit":
        if choice == "buy":
            buy()
            choice = user_choice()
        elif choice == "fill":
            fill()
            choice = user_choice()
        elif choice == "take":
            take()
            choice = user_choice()
        elif choice == "remaining":
            remaining()
            choice = user_choice()

def buy():
    choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
    if choice == "1":
        make_coffee(250, 0, 16, 1, 4)
    
    elif choice == "2":
        make_coffee(350, 75, 20, 1, 7)

    elif choice == "3":
        make_coffee(200, 100, 12, 1, 6)

    elif choice == "back":
        NotImplemented # OR return ""

def fill():
    global water_in_machine
    global milk_in_machine
    global coffee_beans_in_machine
    global disp_cups_in_machine
    water_to_add = int(input("Write how many ml of water do you want to add:\n"))
    milk_to_add = int(input("Write how many ml of milk do you want to add:\n"))
    coffee_beans_to_add = int(input("Write how many grams of coffee beans do you want to add:\n"))
    disp_cups_to_add = int(input("Write how many disposable cups of coffee do you want to add:\n"))
    water_in_machine += water_to_add
    milk_in_machine += milk_to_add
    coffee_beans_in_machine += coffee_beans_to_add
    disp_cups_in_machine += disp_cups_to_add

def take():
    global money_in_machine
    print("I gave you $" + str(money_in_machine))
    money_in_machine -= money_in_machine
    
def make_coffee(water, milk, coffee_beans, disp_cups, money):
    global water_in_machine
    global milk_in_machine
    global coffee_beans_in_machine
    global disp_cups_in_machine
    global money_in_machine
    if water_in_machine >= water:
        if milk_in_machine >= milk:
            if coffee_beans_in_machine >= coffee_beans:
                if disp_cups_in_machine >= disp_cups:
                    water_in_machine -= water
                    milk_in_machine -= milk
                    coffee_beans_in_machine -= coffee_beans
                    disp_cups_in_machine -= disp_cups
                    money_in_machine += money
                    print("I have enough resources, making you a coffee!")
                else:
                    print("Sorry, not enough disposible cup!")
            else:
                print("Sorry, not enough coffee beans!")
        else:
            print("Sorry, not enough milk!")
    else:
        print("Sorry, not enough water!")

def user_choice():
    return input("Write action (buy, fill, take, remaining, exit):\n")
    
menu()