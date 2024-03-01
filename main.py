# Convert Euro or USD to HKD
def convert_currency(amount, currency):
    if currency == 'USD':
        return amount * 7.76
    elif currency == 'Euro':
        return amount * 8.92
    else:
        return "Invalid currency"

# Calculate the minimum number of coins
def calculate_minimum_coins(amount):
    coins = [10, 5, 2, 1]
    count = [0, 0, 0, 0]

    for i in range(len(coins)):
        count[i] = amount // coins[i]
        amount %= coins[i]

    return count

# Calculating the total amount of principle and compound interest
def calculate_interest(principal, rate, time):
    compound_interest = principal * (1 + rate) ** time - principal
    total_amount = principal + compound_interest

    return total_amount

# Main function
def main():
    print("Welcome to IBS! Please choose one of the following functions")
    print("1. Converting Euro or USD to HKD")
    print("2. Calculating the minimum number of coins")
    print("3. Calculating the total amount of principle and compound interest")
    print("4. Quit")

    while True:
        choice = input('Enter your choice: ')

        if choice == '1':
            currency = input("Currency to be converted to HKD (Euro / USD): ")
            amount = float(input("Amount to be converted: "))
            converted_amount = convert_currency(amount, currency)
            print(f"{amount} {currency} = {converted_amount} HKD\n")
        elif choice == '2':
            amount = float(input("Input an amount: "))
            count = calculate_minimum_coins(int(amount))  # Convert amount to integer
            print(f"The minimum numbers of coins for {int(amount)} dollars are:")  # Display amount as integer
            denominations = ['10-dollar', '5-dollar', '2-dollar', '1-dollar']
            for i in range(len(count)):
                print(f"{denominations[i]} coin(s): {int(count[i])}")  # Display count as integer
            print()
        elif choice == '3':
            principal = float(input("Input principle:  "))
            rate = float(input("Input interest rate:  "))
            time = int(input("Input number of years compounded: "))
            total_amount = calculate_interest(principal, rate, time)
            print(f"The total amount after {time} years with a {rate*100}% interest rate is {total_amount}\n")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.\n")

main()
