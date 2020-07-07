########## Question 1 ##########
def format_grocery_item(item_name, item_cost):

    return f"{item_name:<20} ${item_cost:.2f}"

def calculate_cost(unit_price, number_purchase):
    total = unit_price * number_purchase

    return total

groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08
}

sum = 0
# printing receipt
purchases = []
for item, price in groceries. items():
    print(price)
    number_purchase = input(f"How many did you purchase of {item}:")
    number_purchase = float(number_purchase)
    item_cost = calculate_cost(price, number_purchase)
    purchases.append(item_cost)

print("\n====Izzy's Food Emporium====")
i = 0
for item, price in groceries. items():
    print(format_grocery_item(item,purchases[i]))
    sum += purchases[i] 
    i= i +1

print("============================")
print(f"                     ${sum:.2f}")


########## Question 2 ##########

names = [
    "Maddy", "Bel", "Elnaz", "Gia", "Izzy",
    "Joy", "Katie", "Maddie", "Tash", "Nic",
    "Rachael", "Bec", "Bec", "Tabitha", "Teagen",
    "Viv", "Anna", "Catherine", "Catherine", "Debby",
    "Gab", "Megan", "Michelle", "Nic", "Roxy",
    "Samara", "Sasha", "Sophie", "Teagen", "Viv"
]

# use set() to get all unique elements of the list. 
# Then loop over the set to count elements from the list
number = []
unique = set(names)
for item in unique:
    no = (names.count(item))
    # print(item, no)
    number.append(no)

# Create a zip object from two lists 
zipbObj = zip(names, number) 
# Create a dictionary from zip object 
names_dict = dict(zipbObj)
print(names_dict)

# new_dict = {k: v for k, v in zip(names, number)}
# print(new_dict)

for name, no in names_dict.items():
    print(f"{name} {no}")

########## Question 3 ##########
# list of colours where each item in the list is a
# dictionary containing the different representations for each colour.

import csv

colours = []

with open("colours_20.csv") as csv_file:
# with open("colours_213.csv") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        colours.append(row)

print(colours)

