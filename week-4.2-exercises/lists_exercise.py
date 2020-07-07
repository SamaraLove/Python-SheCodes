########## Question 1 ##########

foods = [
    "orange",
    "apple",
    "banana",
    "strawberry",
    "grape",
    "blueberry",
    ["carrot", "cauliflower", "pumpkin"],
    "passionfruit",
    "mango",
    "kiwifruit"
]

# print(foods)

print(foods[0])
print(foods[2])
print(foods[-1])
print(foods[0:3])
print(foods[-3:])
print(foods[6][2])

########## Question 2 ##########


mailing_list = [
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Biscuit", "biscuit@whippies.park"],
    ["Rory", "rory@whippies.park"],
]

# print(mailing_list)
for name, email in mailing_list:
    # for index in mailing_list:
    print(f"{name}: {email}")


########## Question 3 ##########

name1 = input("Please enter a name")
name2 = input("Please enter a name")
name3 =  input("Please enter a name")

output = [name1, name2, name3]
print(output)


########## Question 3 ##########

random_string = input("Please enter string")
length = len(random_string)
string_1 = random_string.split()
print(length,string_1)

string_2  = list(random_string)
length_2 = len(string_2)
print(length_2, string_2)