# Variables and User input Exercises

########## Question 1 #########

# number_1 = 3
# number_2 = 9

# output_1 = 3+9
# print("output1 is: ", output_1)

# number_3 = -3
# number_4 = 9

# output_2 = number_3 + number_4
# print("output2 is: ", output_2)

# number_5 = 3.0
# number_6 = -9
# output_3 = number_5 + number_6
# print("output3 is: ", output_3)
# print()


########## Question 2 #########

# number_1_prompt = input("Please insert one number")
# number_1 = input(number_1_prompt)
# print("Thank you, ",number_1, "is received")
# print(type(number_1))

# number_1 = input("Please insert a number")
# print("Thank you, ",number_1, "is received")

# number_2 = input("Please insert a second number")
# print("Thank you, ",number_2, "is received")

# # use int for Q2a, 2b
# # output_1 = int(number_1) * int(number_2)
# output_1 = float(number_1) * float(number_2)

# print(f"output1 is: {number_1} * {number_2} = {output_1}")


########## Question 3 #########
number_1 = input("Please insert a distance in km")
print("Thank you, ",number_1, "is received")

# # use int for Q3a
# output_m = int(number_1) * 1000
# output_cm = int(number_1) * 100000
output_m = float(number_1) * 1000
output_cm = float(number_1) * 100000

print(f"{number_1}km = {int(output_m)}m")
print(f"{number_1}km = {int(output_cm)}cm")
print()

name = input("What is your name?")
age_prompt = (f"Thank you {name}, what is your height in cm")
age = input(age_prompt)
print(f"{name} is {age}cms tall")