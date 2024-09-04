import json
import csv
import os

# Set the directory containing the JSON files
json_dir = 'UserData/extra'

# Set the output CSV file path and name
csv_file = 'rearrange.csv'

intro = []
demographic = []
trend_tutorial =[]
tutorial_page1 = []
tutorial_page2 = []
tutorial_page3 = []
start_exp = []
complete = []

task_cat_1 = {1: [], 2: [], 3 : [], 4: []}
task_cat_2 = {5: [], 6: [], 7 : [], 8: [], 9: [], 10: [], 11 : [], 12: [], 13: [], 14: [], 15: [], 16: []}
task_cat_3 = {17: [], 18: [], 19 : [], 20: []}

complete_counter = 0
# Open the CSV file for writing
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Loop through the JSON files in the directory
    for filename in os.listdir(json_dir):
        if filename.endswith('.json'):
            # Open the JSON file
            with open(os.path.join(json_dir, filename)) as jsonfile:
                # Load the JSON data
                data = json.load(jsonfile)
                # Write the data to the CSV file

                for item in data:
                    if('page' not in item.keys()):
                        complete_counter = complete_counter + 1
                        continue
                    if(item['page'] == 'introduction'):
                        intro.append(item)
                    if(item['page'] == 'demographics'):
                        demographic.append(item)
                    if(item['page'] == 'trend_tutorial'):
                        trend_tutorial.append(item)
                    if(item['page'] ==  'tutorial'):
                        tutorial_page1.append(item)
                    if(item['page'] ==  'tutorial2'):
                        tutorial_page2.append(item)
                    if(item['page'] ==  'tutorial3'):
                        tutorial_page3.append(item)
                    if(item['page'] == 'start_experiment'):
                        start_exp.append(item)
                    if(item['page'] == 'experiment'):
                        var = item['variables']
                        task_id = var['currentTask']
                        task_cat_1[task_id].append(item)
                    if(item['page'] == 'experiment2'):
                        var = item['variables']
                        task_id = var['currentTask']
                        task_cat_2[task_id].append(item)
                    if(item['page'] == 'experiment3'):
                        var = item['variables']
                        task_id = var['currentTask']
                        task_cat_3[task_id].append(item)


for i in range(35):
    json_arr = []
    json_arr.append(intro[i])
    json_arr.append(demographic[i])
    json_arr.append(trend_tutorial[i])
    json_arr.append(tutorial_page1[i])
    json_arr.append(tutorial_page2[i])
    json_arr.append(tutorial_page3[i])
    json_arr.append(start_exp[i])

    for j in range(1,5):
        json_arr.append(task_cat_1[j][i])

    for j in range(5,17):
        print("len")
        print(len(task_cat_2[j]))
        print("index")
        print(i)
        json_arr.append(task_cat_2[j][i])

    for j in range(17,21):
        json_arr.append(task_cat_3[j][i])
    
    # json_arr.append(complete[i])

    with open('UserData' + str(i + 16) + '.json', 'w') as outfile:
        json.dump(json_arr, outfile)

    

