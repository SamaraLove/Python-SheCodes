
########## Question 1 ##########

sum=0
number = input("Please enter a number")
while number != "":
    sum += int(number)
    number = input("Please enter a number") 
print(sum)

########## Question 2 ##########

mailing_list = [
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Biscuit", "biscuit@whippies.park"],
    ["Rory", "rory@whippies.park"],
]

print(mailing_list)
for contact in mailing_list:
    print(f"{contact[0]}: {contact[1]}")
    
########## Question 3 ##########

names =[]
counter = 0
while counter < 3:
    name = input("Please enter a name\r\n")
    names.append(name)
    counter = counter +1
for name in names:
    print(name)


########## Question 4 ##########

groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]

sum = 0
receipt = "====Izzy's Food Emporium===="
for item in groceries:
    no_purchase = input(f"How many did you purchase of {item[0]}:")
    item[1] = item[1] * float(no_purchase)
    # print(item[1])
    sum += item[1] 
    # receipt.append(item)

print(receipt)
for purchase in groceries:
    print(f"{purchase[0]:<20} ${purchase[1]:.2f}")
print("============================")
print(f"                    ${sum:.2f}")

    
