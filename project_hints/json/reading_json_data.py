import json
import ast

file = "data/quiz.json"

questions = {}

with open(file) as json_file:
    json_data = json.load(json_file)
    # print(json_data)
    
    # testing location levels 
    # print(json_data['quiz']['One']['question'])
    # print(json_data['quiz']['One']['options'])
    # print(json_data['quiz']['One']['answer'])
    # for i in json_data['quiz']['One']:
    #     print(i)

    for q_no in json_data['quiz']:
        question = json_data['quiz'][q_no]['question']
        options = json_data['quiz'][q_no]['options']
        answer = json_data['quiz'][q_no]['answer']

        print(f"\nQuestion {q_no}: {question}")

        for item in options:
            print(f"\t{item}")
            # {'':<7}
        
        print(f"Answer: {answer}\n")