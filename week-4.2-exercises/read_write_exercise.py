########## Question 1 ##########

## Example 1 output to only the terminal
# names = []
# with open("names.txt") as txt_file:
#     for no,name in enumerate(txt_file, 1):
#         print(f"{no}. {name}")


# for c, value in enumerate(my_list, 1):
#     print(c, value)


## Outputs to file

names = []
with open("names.txt") as txt_file:
    # for line in txt_file:
    # for no,line in enumerate(txt_file, 1):

    for no,name in enumerate(txt_file, 1):
        output = f"{no}. {name}"
        # print(output)
        output = output.strip()
        names.append(output)

print(names)

with open("names_output.txt", "w" ) as txt_file:
    for name in names:
        # print(f"{no}. {name}")
        txt_file.write(name + "\n")


########## Question 2 ##########
import csv

colours = []

with open("colours_20.csv") as csv_file:
# with open("colours_213.csv") as csv_file:

    reader = csv.reader(csv_file)
    # header = next(reader)
    for row in reader:
        # For each row it fetched the contents of that row as a list and printed that list.
        output = row[1], row[2], row[4]
        colours.append(output)
print(colours)
with open("colours_20_output.csv", "w", newline='') as csv_file:
# with open("colours_213_output.csv", "w", newline='') as csv_file:
# newline='' removes the empty line after every line

    csv_writer = csv.writer(csv_file, delimiter=",")
    for item in colours:
        csv_writer.writerow(item)


########## Question 3 ##########
import csv

colours_English = []
i = 0
g = 0
b = 0
# with open("colours_20.csv") as csv_file:
with open("colours_213.csv") as csv_file:

    reader = csv.reader(csv_file)
    # header = next(reader)
    for row in reader:
        output = row[4]
        colours_English.append(output)
        print(output)

# print(colours_English)
        if "red" in output:
            i = i + 1     
        elif "green" in output:
            g = g + 1   
        elif "blue" in output:
            b = b + 1
#     ic = colours_English.count("red")
#     gc = colours_English.count("green")
#     bc = colours_English.count("blue")
# print(f"\nRed: {i}\nGreen: {g}\nBlue: {b}\n")
# print(f"\nRed: {ic}\nGreen: {gc}\nBlue: {bc}\n")

print(len(colours_English))
# with open("colours_20_output.csv", "w", newline='') as csv_file:
with open("colours_213_output.csv", "w", newline='') as csv_file:
# newline='' removes the empty line after every line

    csv_writer = csv.writer(csv_file, delimiter=",")
    for item in colours_English:
        # print(item)
        csv_writer.writerow([item])