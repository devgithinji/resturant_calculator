TIP = 0.18
SALES_TAX = 0.07


def is_number(number_string):
    try:
        float(number_string)
        return True
    except ValueError:
        return False


def calculate(food_amount):
    tip = TIP * food_amount;
    sales_tax = SALES_TAX * food_amount;
    grand_total = food_amount + tip + sales_tax

    print(f'Tip = ${tip:.2f}')
    print(f'Sales Tax = ${sales_tax:.2f}')
    print(f'Grand Total = ${grand_total:.2f}')


def ask_input():
    food_charge = input('Please enter food charge: $')
    if is_number(food_charge):
        calculate(float(food_charge))
        ask_input()
    else:
        print('Invalid input ')
        ask_input()


ask_input()
