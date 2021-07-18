MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resources_sufficient(beverage_ingredients, res):
    for item in beverage_ingredients:
        if beverage_ingredients[item] > res[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def reduce_resources(bev, res):
    for key in bev["ingredients"]:
        res[key] = res[key]-bev["ingredients"][key]

    if "money" in res:
        res["money"] += bev["cost"]
    else:
        res["money"] = bev["cost"]
    return res


def print_resources(res):
    print(f"Water: {res['water']}ml \nCoffee: {res['coffee']}g \nMilk: {res['milk']}ml")
    if "money" in res:
        print(f'Money: {res["money"]}')


def process_payment():
    print("Please insert coins.")
    quarter = input("How many quarters?: ")
    dime = input("How many dimes?: ")
    nickel = input("How many nickels?: ")
    penny = input("How many pennies?: ")
    cents = int(penny) + 5*int(nickel) + int(dime)*10 + int(quarter)*25
    return cents/100


def coins_enough(price, inserted_coins):
    if price > inserted_coins:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        return True


def process_request(request, res):
    resources_enough = resources_sufficient(request["ingredients"], res)
    if resources_enough:
        money = process_payment()
        money_enough = coins_enough(request["cost"], money)
        if money_enough:
            change_given = money - request["cost"]
            print(f"Here's your change {change_given}")
            return reduce_resources(request, res)
    else:
        return res


def run_machine(res):
    # TODO: Ask customer for drink choice
    machine_resources = res
    drink_choice = ""
    while drink_choice != "off":
        drink_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if drink_choice != "off":
            if drink_choice == "report":
                print_resources(machine_resources)
            elif drink_choice == "cappuccino" or drink_choice == "latte" or drink_choice == "espresso":
                global MENU
                machine_resources = process_request(MENU[drink_choice], machine_resources)
            else:
                print("Sorry that is not a valid option")


run_machine(resources)
