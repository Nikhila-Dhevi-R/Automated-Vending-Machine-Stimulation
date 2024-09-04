# Dictionary storing product names and their prices
products = {"Sandwich": 2,
    "Pizza": 3,
    "Burger": 2.5} 

# Initialize total money collected by the vending machine
total_collected_money = 0
product_list = []

while True:
    index = 0
    print("\nWelcome to the Vending Machine!")
    print("Available products: ")
    print("Enter 0 to exit the machine.")
    
# Display the products with their respective prices
    for product in products:
        index += 1
        product_list.append(product)
        print(f"{index}. {product}  -  ${products[product]}")

# User input for product selection
    user_input = int(input("Enter an item number: "))
    
    if user_input == 0:
        print("Thank you for using our services!")
        break
    
    elif user_input == 99:
# Owner's menu for withdrawing money
        print("\nWelcome to the owner's space")
        print(f"Total collection so far is ${total_collected_money}")
        owner_input = int(input("Press 1 to withdraw the money, 0 to cancel: "))
        
        if owner_input == 1:
            print("\nAmount withdrawal successful!")
            total_collected_money = 0
            break
        else:
            break
# Determine the user's product choice and its price
    selected_product = product_list[user_input - 1]
    product_price = products[selected_product]
    
# User input for payment
    amount_received = float(input(f"Please enter ${product_price} in coins (Enter 0 to cancel): "))
    
    if amount_received == 0:
        print("Transaction cancelled")
        break
    
# If the user enters enough or more money
    if amount_received >= product_price:
        print(f"Dispensing {selected_product}, please collect your change of ${amount_received - product_price}")
        total_collected_money += product_price
    
# If the user doesn't enter enough money
    elif amount_received < product_price:
        additional_amount = float(input(f"Insufficient funds, please enter ${product_price - amount_received} more (Enter 0 to cancel): "))
        
        if additional_amount == 0:
            print("Transaction cancelled")
            break
        else:
            amount_received += additional_amount
            if amount_received == product_price:
                total_collected_money += amount_received
                print(f"Dispensing {selected_product}, please collect your change ${amount_received - product_price}")
