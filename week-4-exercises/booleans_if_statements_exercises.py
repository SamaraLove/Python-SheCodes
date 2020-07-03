# Boolean and if Statement Exercises

########## Question 1 #########
# # moths_in_house = True 
# moths_in_house = False

# if moths_in_house:
#      print("Get the moths!")
# else: 
#     print("No threats detected")
# print()

########## Question 2 #########
# moths_in_house = True
# mitch_is_home = False

# if moths_in_house and mitch_is_home:
#     print("Hoooman! Help me get the moths!")
# elif moths_in_house and not mitch_is_home:
#     print("Meooooooooooooow! Hissssss!")
# elif not moths_in_house and not mitch_is_home:
#     print("No threats detected")
# elif not moths_in_house and mitch_is_home:
#     print("Climb on Mitch.")

# print()


########## Question 3 #########
light_colour = "Amber"
car_detected = True

if light_colour =="Red" and not car_detected:
    print("Do nothing.") 
elif light_colour =="Red" and  car_detected:
    print("Flash!")
elif light_colour =="Green" and not car_detected:
    print("Do nothing.") 
elif light_colour =="Green" and  car_detected:
    print("Do nothing.") 
elif light_colour =="Amber" and not car_detected:
    print("Do nothing.") 
elif light_colour =="Amber" and car_detected:
    print("Do nothing.") 

# print()

########## Question 4 #########
height = input("Hello, please enter your height in cm")
height_no = int(height)
if height_no == 120:
    print("Hop on!")
elif height_no ==50:
    print("Sorry, not today :(")
elif height_no == 191:
    print("Hop on!")
# elif height_no < 120:
#     print("Sorry, you're not tall enough")
# elif height_no >= 120:
#     print("Yay you are tall enough to go on the rollercoaster")