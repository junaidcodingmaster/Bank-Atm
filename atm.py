import os
import time
import inquirer
import pyfiglet
from simple_chalk import chalk
from tqdm import tqdm

# This is ATM class
class atm:
    def __init__(self, username, pin, moneyState, amountMoney):
        self.username = username
        self.pin = pin
        self.moneyState = moneyState

        if self.moneyState == True:
            self.amountMoney = amountMoney
            amount = amountMoney
            printMoney = "   $" + str(amount) + "    "
            rawMoney = pyfiglet.figlet_format(printMoney, font="banner3-D")
            money = chalk.green.bold(rawMoney)
            print("\n")
            print(money)
        else:
            os._exit(0)


# On Start Up
os.system("cls")

# logo
rawLogo = pyfiglet.figlet_format("ATM")
logo = chalk.green.bold(rawLogo)
sideRawLogo = pyfiglet.figlet_format("Bank")
sideLogo = chalk.blue.bold(sideRawLogo)
print(sideLogo + logo)

# Display

# Header
print(
    "Welcome to "
    + chalk.blue.bold("Terminal")
    + " "
    + chalk.green.bold("ATM")
    + " , This terminal is made By Junaid."
)


try:
    username = input("\nEnter Your User Name : ")
    pin = int(input("Enter Your Pin : "))
except KeyboardInterrupt:
    print(chalk.yellow("User Exited"))
    os._exit(0)
except ValueError:
    print(chalk.red("Something went wrong"))
    os._exit(1)

if pin == 4568:
    pass
else:
    print(chalk.red("Invalid Password"))
    os._exit(0)

os.system("cls")

# 2nd Screen

# Logo
print(sideLogo + logo)

# Header
print(
    "Welcome to "
    + chalk.blue.bold("Terminal")
    + " "
    + chalk.green.bold("ATM")
    + " , This terminal is made By Junaid.\n"
)

# Display
print("Welcome", username)
print("__" * 10)
print("\n")

interface = [
    inquirer.List(
        "screen",
        message="Select your option",
        choices=["Withdraw", "Account Transfer", "Fund Transfer"],
    ),
    inquirer.List(
        "screen2",
        message="Select your money withdraw option",
        choices=[
            "Savings",
            "Account Transfer",
            "Fund Transfer",
            "Funds",
            "Home Lone",
            "Lone",
        ],
    ),
]

screen = str(inquirer.prompt(interface)["screen2"])
moneyMode = ""


if screen == "Savings":
    os.system("cls")
    # 3rd Screen
    amount = int(input("Enter your amount : $"))
    print("\n")
    print("Getting your money from savings...")
    for i in tqdm(range(100), desc="Processesing… ", ascii=False, ncols=75):
        time.sleep(0.02)
    moneyMode = "Savings"
    print("\n")
    atm(username, pin, True, amount)

else:
    moneyMode = screen
    os.system("cls")
    print(chalk.red("Unable to connect to bank"), "Select savings to get your money.")
