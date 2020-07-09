class CoffeeMachine():

    def __init__(self, water, milk, coffee_beans, disp_cups, money):
        self.water_in_machine = water
        self.milk_in_machine = milk
        self.coffee_beans_in_machine = coffee_beans
        self.disp_cups_in_machine = disp_cups
        self.money_in_machine = money
        self.machine_state = ""
        
    def action(self, choice):
        if choice == "buy":
            self.machine_state = "choosing a type of coffee"
        elif choice == "fill":
            self.machine_state = "filling the machine's resources"
        elif choice == "take":
            self.machine_state = "taking all the money"
        elif choice == "remaining":
            self.machine_state = "showing all the remaining resources"

    def buy(self, choice):
        if choice == "1":
            self.make_coffee(250, 0, 16, 1, 4)
        elif choice == "2":
            self.make_coffee(350, 75, 20, 1, 7)
        elif choice == "3":
            self.make_coffee(200, 100, 12, 1, 6)
        # self.machine_state = "choosing an action"

    def make_coffee(self, water, milk, coffee_beans, disp_cups, money):
        if self.water_in_machine >= water:
            if self.milk_in_machine >= milk:
                if self.coffee_beans_in_machine >= coffee_beans:
                    if self.disp_cups_in_machine >= disp_cups:
                        self.water_in_machine -= water
                        self.milk_in_machine -= milk
                        self.coffee_beans_in_machine -= coffee_beans
                        self.disp_cups_in_machine -= disp_cups
                        self.money_in_machine += money
                        print("I have enough resources, making you a coffee!")
                    else:
                        print("Sorry, not enough disposible cup!")
                else:
                    print("Sorry, not enough coffee beans!")
            else:
                print("Sorry, not enough milk!")
        else:
            print("Sorry, not enough water!")
    
    def __str__(self):
        return f"""The coffee machine has:\n{self.water_in_machine} of water\n{self.milk_in_machine} of milk\n{self.coffee_beans_in_machine} of coffee beans\n{self.disp_cups_in_machine} of disposible cups\n${self.money_in_machine} of money"""

    def fill(self, water, milk, coffee_beans, disp_cups):
        self.water_in_machine += water
        self.milk_in_machine += milk
        self.coffee_beans_in_machine += coffee_beans
        self.disp_cups_in_machine += disp_cups
    
    def take(self):
        print(f"I gave you ${self.money_in_machine}")
        self.money_in_machine -= self.money_in_machine


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)

def choose_action():
    return input("Write action (buy, fill, take, remaining, exit):\n")

choice = choose_action()
coffee_machine.action(choice)
while choice != "exit":

    if coffee_machine.machine_state == "choosing a type of coffee":
        coffee_machine.buy(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n"))
        choice = choose_action()
        coffee_machine.action(choice)

    elif coffee_machine.machine_state == "filling the machine's resources":
        water = int(input("Write how many ml of water do you want to add:\n"))
        milk = int(input("Write how many ml of milk do you want to add:\n"))
        coffee_beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
        disp_cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))
        coffee_machine.fill(water, milk, coffee_beans, disp_cups)
        choice = choose_action()
        coffee_machine.action(choice)

    elif coffee_machine.machine_state == "taking all the money":
        coffee_machine.take()
        choice = choose_action()
        coffee_machine.action(choice)

    elif coffee_machine.machine_state == "showing all the remaining resources":
        print(coffee_machine)
        choice = choose_action()
        coffee_machine.action(choice)