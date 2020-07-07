import json
file = "json/data/quiz.json"

with open(file) as json_file:
    json_data = json.load(json_file)
    print(json_data)
    # for line, stuff in json_data.items():
    #     print(line, stuff)
    #     print()
        # print(json_data['question'])





# print("Question One: Our goal at She Codes is to get x women in tech by y.")