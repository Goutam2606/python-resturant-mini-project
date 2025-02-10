menu ={
    'pizza': 500,
    'burger': 200,
    'coke': 50,
    'fries': 150,
    'coffee': 100,
    'noodles': 150,
    'ice-cream': 100,
    'cake': 200,
    'sandwich': 150,
}
#Greeting
print("Welcome to the restaurant")

# Menu of the resturant
def items_menu():
    print("-----------------Menu-----------------")
    for item in menu:
      print( "*", item, ":", menu[item])
    print("--------------------------------------")
items_menu()

# Order the items
ordered_items = []
dish = input("Enter the items you want to order : ").lower()
ordered_items.append(dish)

# Order more items
more_items = input("Do you want to order more items? (y/n):").lower()
while more_items == 'y':
    more_item_dish = input("Enter the items you want to order : ")
    ordered_items.append(more_item_dish)
    more_items = input("Do you want to order more items? (y/n):").lower()

# Calculate total amount
def calculate_total(ordered_items):
    total = 0
    for item in ordered_items:
        if item in menu:
            total += menu[item]
    return total

# Display the bill
total_amount = calculate_total(ordered_items)
print("-----------------Bill-----------------")
print("Your total bill is: ₹", total_amount)
print("--------------------------------------")
print("Thank you for ordering!")