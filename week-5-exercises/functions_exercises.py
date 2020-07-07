########## Question 1 ##########

def temperature(fahrenheit):
    degrees = (fahrenheit - 32) * 5/9 

    return degrees

deg = temperature(0)
print(deg)

########## Question 2 ##########

def calculate_mean(total_sum, num_items):
    mean = total_sum/num_items

    return mean

numberList = []
num_items = 0
total_sum = 0

number = input("Please enter a number")
numberList.append(number)

while number != "":
    number = input("Please enter a number")
    num_items = num_items +1
    numberList.append(number)

print("Original user input numbers:", numberList)
del numberList[-1]
print("Modified user input numbers:", numberList)
print("Number of entries:", num_items)

for num in numberList:
    total_sum += float(num)

mean = calculate_mean(total_sum, num_items)
print(f"mean in {mean:.2f}")

########## Question 3 ##########
import csv

def read_csv_file(filepath):
    # returns contents as a list

    with open(filepath) as csv_file:

        reader = csv.reader(csv_file)
        # header = next(reader)
        for row in reader:
            output = row[1], row[2], row[4]
            colours.append(output)

    return colours

def format_colour_line(colour_data):
    # Takes the list of data pecific colour, the formats and returns the relevant fields.
    with open("output_"+ filepath, "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        for item in colours:
            # print(item)
            data = csv_writer.writerow(item)

    return data

colours = []

filepath = "colours_213.csv"
# filepath = "colours_20.csv"

read_csv_file(filepath)
# print(colours)

format_colour_line(colours)

########## Question 4 ##########

def format_grocery_item(item_name, item_cost):

    return f"{item_name:<20} ${item_cost:.2f}"

def calculate_cost(unit_price, number_purchase):
    total = unit_price * number_purchase

    return total

groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]

sum = 0
# printing receipt
purchases = []
for item in groceries:
    number_purchase = input(f"How many did you purchase of {item[0]}:")
    number_purchase = float(number_purchase)
    item_cost = calculate_cost(item[1], number_purchase)
    purchases.append(item_cost)

print("\n====Izzy's Food Emporium====")
i = 0
for item in groceries:
    print(format_grocery_item(item[0],purchases[i]))
    sum += purchases[i] 
    i= i +1

print("============================")
print(f"                     ${sum:.2f}")
