########## Question 1 ##########

## Example 1 output 
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


########## Question 3 ##########

    

import csv

# colours = []
i = 0
b =0
g = 0
with open("colours_213.csv") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    ##cycling through first row
    for row in reader:
        # print(row)
        for column in row:
            if column == " English Name":
                print(column)
                print(row)
                # print(row)
                # next(csv_file)
                next(reader)
                print(row)
                if item == "Beige":
                    i = i + 1
                elif column =="blue":
                    b = b + 1
                elif column == "green":
                    g = g + 1
    print(i)
    print(f"Red: {i}\nGreen: {g}\nBlue: {b}")
