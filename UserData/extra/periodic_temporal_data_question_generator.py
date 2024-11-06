import json
import random
from pathlib import Path

#define and declare switch
#Switch = True

#Universal Path
universal_vis_path = "/images/Periodic_Temporal_Data_Viz"
#type one task groups
trend_group =[['Bit/Daily', 'Balt/Aggregated', 'App/Trellis', 'Cli/Spiral'],
              ['App/Aggregated', 'Cli/Trellis', 'Bit/Spiral', 'Balt/Daily'],
              ['Bit/Trellis', 'Balt/Spiral', 'App/Daily', 'Cli/Aggregated'],
              ['App/Spiral', 'Cli/Daily', 'Bit/Aggregated', 'Balt/Trellis'],
              ['Bit/Daily', 'Balt/Aggregated', 'App/Trellis', 'Cli/Spiral'],
              ['App/Aggregated', 'Cli/Trellis', 'Bit/Spiral', 'Balt/Daily'],
              ['Bit/Trellis', 'Balt/Spiral', 'App/Daily', 'Cli/Aggregated'],
              ['App/Spiral', 'Cli/Daily', 'Bit/Aggregated', 'Balt/Trellis']]

prediction_group = [['Bit/Aggregated', 'Balt/Trellis', 'App/Spiral', 'Cli/Daily'],
                    ['App/Daily', 'Cli/Aggregated', 'Bit/Trellis', 'Balt/Spiral'],
                    ['Bit/Spiral', 'Balt/Daily', 'App/Aggregated', 'Cli/Trellis'],
                    ['App/Trellis', 'Cli/Spiral', 'Bit/Daily', 'Balt/Aggregated'],
                    ['Bit/Aggregated', 'Balt/Trellis', 'App/Spiral', 'Cli/Daily'],
                    ['App/Daily', 'Cli/Aggregated', 'Bit/Trellis', 'Balt/Spiral'],
                    ['Bit/Spiral', 'Balt/Daily', 'App/Aggregated', 'Cli/Trellis'],
                    ['App/Trellis', 'Cli/Spiral', 'Bit/Daily', 'Balt/Aggregated']]


attention_check_questions = [
    {"question": "Is the sky blue or green?", "options": {"A": "Blue", "B": "Green"}},
    {"question": "Is the sun hot or cold?", "options": {"A": "Hot", "B": "Cold"}},
    {"question": "Does 1+1 equal 2 or 3?", "options": {"A": "2", "B": "3"}},
    {"question": "Is an elephant bigger than a mouse?", "options": {"A": "Yes", "B": "No"}},
    {"question": "Is the letter \"A\" before or after the letter \"B\" in the alphabet?", "options": {"A": "Before", "B": "After"}},
    {"question": "Is water wet or dry?", "options": {"A": "Wet", "B": "Dry"}},
    {"question": "Does a circle have four sides or no sides?", "options": {"A": "No sides", "B": "Four sides"}},
    {"question": "Does a dog bark or meow?", "options": {"A": "Bark", "B": "Meow"}},
    {"question": "Is a bicycle a mode of transportation or a type of fruit?", "options": {"A": "Mode of transportation", "B": "Type of fruit"}},
    {"question": "Does a tree grow up or down?", "options": {"A": "Up", "B": "Down"}},
    {"question": "Is a square a shape with four sides or five sides?", "options": {"A": "Four sides", "B": "Five sides"}},
    {"question": "Does a whale live in the water or in the sky?", "options": {"A": "Water", "B": "Sky"}},
    {"question": "Is a book read from left to right or right to left?", "options": {"A": "Left to right", "B": "Right to left"}},
    {"question": "Is the moon bigger than the earth or smaller?", "options": {"A": "Smaller", "B": "Bigger"}},
    {"question": "Is a carrot a type of vegetable or a type of animal?", "options": {"A": "Vegetable", "B": "Animal"}},
    {"question": "Does a snake have legs or no legs?", "options": {"A": "No legs", "B": "Legs"}},
    {"question": "Is a pencil a writing tool or a type of fruit?", "options": {"A": "Writing tool", "B": "Type of fruit"}},
    {"question": "Is a piano a musical instrument or a type of vehicle?", "options": {"A": "Musical instrument", "B": "Type of vehicle"}},
    {"question": "Does a cow give milk or eggs?", "options": {"A": "Milk", "B": "Eggs"}},
    {"question": "Is a hammer a tool used for cooking or for building?", "options": {"A": "For building", "B": "For cooking"}}
]

daily_trend_story_dict = {
    "Apple": "The following chart shows daily price of BestTech company stock from January 2016 to December 2019. The height of the blue line from the bottom black axis indicates price. From this chart, you need to answer the following questions.",
    "Baltimore": "The following chart shows number of daily crime incidents occurred in a city named Metropolis from January 2012 to December 2016. The height of the blue line from the bottom black axis indicates number of incidents. From this chart, you need to answer the following questions.",
    "Bitcoin": "The following chart shows daily price of a product named PowerCoin from January 2017 to December 2019. The height of the blue line from the bottom black axis indicates price. From this chart, you need to answer the following questions.",
    "Climate": "The following chart shows daily humidity value of a city named Eudaemonia from January 2013 to December 2016. The height of the blue line from the bottom black axis indicates humidity value. From this chart, you need to answer the following questions."
}

monthly_trend_story_dict = {
    "Apple": "The following chart shows the monthly average price of BestTech company stock from January 2016 to December 2019. The height of the blue line from the bottom black axis indicates the price. From this chart, you need to answer the following questions.",
    "Baltimore": "The following chart shows the monthly average number of crime incidents in a city named Metropolis from January 2012 to December 2016. The height of the blue line from the bottom black axis indicates the number of incidents. From this chart, you need to answer the following questions.",
    "Bitcoin": "The following chart shows the monthly average price of a product named PowerCoin from January 2017 to December 2019. The height of the blue line from the bottom black axis indicates the price. From this chart, you need to answer the following questions.",
    "Climate": "The following chart shows the monthly average humidity value of a city named Eudaemonia from January 2013 to December 2016. The height of the blue line from the bottom black axis indicates the humidity value. From this chart, you need to answer the following questions."
}


prediction_question_dict = {
    "Apple": "What is your prediction regarding the price in January, 2020 ?",
    "Baltimore": "What is your prediction regarding the number of incidents in January, 2017 ?",
    "Bitcoin": "What is your prediction regarding the price in January, 2020 ?",
    "Climate": "What is your prediction regarding the humidity in January, 2017 ?"
}

prediction_question_arr = [[prediction_question_dict["Bitcoin"], prediction_question_dict['Baltimore'], prediction_question_dict['Apple'], prediction_question_dict['Climate']],
                       [prediction_question_dict['Apple'], prediction_question_dict['Climate'], prediction_question_dict["Bitcoin"], prediction_question_dict['Baltimore']],
                       [prediction_question_dict["Bitcoin"], prediction_question_dict['Baltimore'], prediction_question_dict['Apple'], prediction_question_dict['Climate']],
                       [prediction_question_dict['Apple'], prediction_question_dict['Climate'], prediction_question_dict["Bitcoin"], prediction_question_dict['Baltimore']],
                       [prediction_question_dict["Bitcoin"], prediction_question_dict['Baltimore'], prediction_question_dict['Apple'], prediction_question_dict['Climate']],
                       [prediction_question_dict['Apple'], prediction_question_dict['Climate'], prediction_question_dict["Bitcoin"], prediction_question_dict['Baltimore']],
                       [prediction_question_dict["Bitcoin"], prediction_question_dict['Baltimore'], prediction_question_dict['Apple'], prediction_question_dict['Climate']],
                       [prediction_question_dict['Apple'], prediction_question_dict['Climate'], prediction_question_dict["Bitcoin"], prediction_question_dict['Baltimore']]
                    ]

trend_story = [[daily_trend_story_dict['Bitcoin'], monthly_trend_story_dict['Baltimore'], daily_trend_story_dict['Apple'], daily_trend_story_dict['Climate']],
               [monthly_trend_story_dict['Apple'], daily_trend_story_dict['Climate'], daily_trend_story_dict['Bitcoin'], daily_trend_story_dict['Baltimore']],
               [daily_trend_story_dict['Bitcoin'], daily_trend_story_dict['Baltimore'], daily_trend_story_dict['Apple'], monthly_trend_story_dict['Climate']],
               [daily_trend_story_dict['Apple'], daily_trend_story_dict['Climate'], monthly_trend_story_dict['Bitcoin'], daily_trend_story_dict['Baltimore']],
               [daily_trend_story_dict['Bitcoin'], monthly_trend_story_dict['Baltimore'], daily_trend_story_dict['Apple'], daily_trend_story_dict['Climate']],
               [monthly_trend_story_dict['Apple'], daily_trend_story_dict['Climate'], daily_trend_story_dict['Bitcoin'], daily_trend_story_dict['Baltimore']],
               [daily_trend_story_dict['Bitcoin'], daily_trend_story_dict['Baltimore'], daily_trend_story_dict['Apple'], monthly_trend_story_dict['Climate']],
               [daily_trend_story_dict['Apple'], daily_trend_story_dict['Climate'], monthly_trend_story_dict['Bitcoin'], daily_trend_story_dict['Baltimore']]
            ]

prediction_story = [[monthly_trend_story_dict['Bitcoin'], daily_trend_story_dict['Baltimore'], daily_trend_story_dict['Apple'], daily_trend_story_dict['Climate']],
                    [daily_trend_story_dict['Apple'], monthly_trend_story_dict['Climate'], daily_trend_story_dict['Bitcoin'], daily_trend_story_dict['Baltimore']],
                    [daily_trend_story_dict['Bitcoin'], daily_trend_story_dict['Baltimore'], monthly_trend_story_dict['Apple'], daily_trend_story_dict['Climate']],
                    [daily_trend_story_dict['Apple'], daily_trend_story_dict['Climate'], daily_trend_story_dict['Bitcoin'], monthly_trend_story_dict['Baltimore']],
                    [monthly_trend_story_dict['Bitcoin'], daily_trend_story_dict['Baltimore'], daily_trend_story_dict['Apple'], daily_trend_story_dict['Climate']],
                    [daily_trend_story_dict['Apple'], monthly_trend_story_dict['Climate'], daily_trend_story_dict['Bitcoin'], daily_trend_story_dict['Baltimore']],
                    [daily_trend_story_dict['Bitcoin'], daily_trend_story_dict['Baltimore'], monthly_trend_story_dict['Apple'], daily_trend_story_dict['Climate']],
                    [daily_trend_story_dict['Apple'], daily_trend_story_dict['Climate'], daily_trend_story_dict['Bitcoin'], monthly_trend_story_dict['Baltimore']]]


trust_game_group = [['D_N_U/T_N_U', 'D_N_D/S_N_D', 'D_N_U/A_N_U', 'D_M_U/T_N_U', 'D_N_U/S_M_U', 'D_M_U/A_N_U', 'D_N_U/T_M_D', 'D_M_D/S_N_U', 'D_N_U/A_M_D', 'D_N_D/T_N_U', 'D_N_U/S_N_D', 'D_N_D/A_N_U'],
                    ['D_N_U/T_N_U', 'D_N_D/S_N_D', 'D_N_D/A_N_D', 'D_M_U/T_N_U', 'D_N_U/S_M_U', 'D_N_U/A_M_U', 'D_N_U/T_M_D', 'D_M_D/S_N_U', 'D_M_U/A_N_D', 'D_N_D/T_N_U', 'D_N_U/S_N_D', 'D_N_U/A_N_D'],
                    ['D_N_U/T_N_U', 'D_N_U/S_N_U', 'D_N_U/A_N_U', 'D_M_U/T_N_U', 'D_M_U/S_N_U', 'D_M_U/A_N_U', 'D_N_U/T_M_D', 'D_N_U/S_M_D', 'D_N_U/A_M_D', 'D_N_D/T_N_U', 'D_N_D/S_N_U', 'D_N_D/A_N_U'],
                    ['D_N_U/T_N_U', 'D_N_U/S_N_U', 'D_N_D/A_N_D', 'D_M_U/T_N_U', 'D_M_U/S_N_U', 'D_N_U/A_M_U', 'D_N_U/T_M_D', 'D_N_U/S_M_D', 'D_M_U/A_N_D', 'D_N_D/T_N_U', 'D_N_D/S_N_U', 'D_N_U/A_N_D'],
                    ['D_N_D/T_N_D', 'D_N_D/S_N_D', 'D_N_U/A_N_U', 'D_N_U/T_M_U', 'D_N_U/S_M_U', 'D_M_U/A_N_U', 'D_M_D/T_N_U', 'D_M_D/S_N_U', 'D_N_U/A_M_D', 'D_N_U/T_N_D', 'D_N_U/S_N_D', 'D_N_D/A_N_U'],
                    ['D_N_D/T_N_D', 'D_N_D/S_N_D', 'D_N_D/A_N_D', 'D_N_U/T_M_U', 'D_N_U/S_M_U', 'D_N_U/A_M_U', 'D_M_D/T_N_U', 'D_M_D/S_N_U', 'D_M_U/A_N_D', 'D_N_U/T_N_D', 'D_N_U/S_N_D', 'D_N_U/A_N_D'],
                    ['D_N_D/T_N_D', 'D_N_U/S_N_U', 'D_N_U/A_N_U', 'D_N_U/T_M_U', 'D_M_U/S_N_U', 'D_M_U/A_N_U', 'D_M_D/T_N_U', 'D_N_U/S_M_D', 'D_N_U/A_M_D', 'D_N_U/T_N_D', 'D_N_D/S_N_U', 'D_N_D/A_N_U'],
                    ['D_N_D/T_N_D', 'D_N_U/S_N_U', 'D_N_D/A_N_D', 'D_N_U/T_M_U', 'D_M_U/S_N_U', 'D_N_U/A_M_U', 'D_M_D/T_N_U', 'D_N_U/S_M_D', 'D_M_U/A_N_D', 'D_N_U/T_N_D', 'D_N_D/S_N_U', 'D_N_U/A_N_D']]






#number of participants
counter = 8

# Demographic questions
def demographic_questions():

    ###########demographics pages
    demo_question = []
    age = {}
    age["id"] = "age"
    age["question"] = "What is your age group?"
    age["options"] = [
    "18-24 years old",
    "25-34 years old",
    "35-44 years old",
    "45-54 years old",
    "55-64 years old"]
    demo_question.append(age)
    gender = {}
    gender["id"] = "gender"
    gender["question"] = "What gender do you identify as ?"
    gender["options"] = ["Male",
    "Female",
    "Non-Binary / third gender",
    "Prefer not to say" ]
    demo_question.append(gender)
    education = {}
    education["id"] = "education"
    education["question"] = "What is the highest level of education you have completed ?"
    education["options"] = ["HighSchool",
    "Bachelor's Degree",
    "Master's Degree",
    "PhD or Higher"]
    demo_question.append(education)
    vis={}
    vis["id"] = "visualization_experience"
    vis["question"] = "How familiar are you with Data Visualization and it's concepts ?"
    vis["options"] = ["Have no idea",
    "Have some idea",
    "Beginner",
    "Experienced User",
    "Expert" ]
    demo_question.append(vis)
    demographics_page = {}
    demographics_page["page"] = "demographics"
    demographics_page["variables"] = {"page_title": "Demographic Information"}
    demographics_page["questions"] = demo_question

    return demographics_page

#for each question write a function and the function should randomly choose the visualizations, accuracies and other options

def experiment(participant_path, taskId, grpId):
    img_url = participant_path + '/img'+ str(taskId) +'.svg'

    question = trend_story[grpId][taskId - 1]
    experiment_json = {}
    experiment_json['page'] = "experiment"
    experiment_json['variables'] = {"page_title": "", "currentTask": taskId, "totalTasks": 20, "question" : question}
    experiment_json['questions'] = [{
        "id": taskId,
        "question": attention_check_questions[taskId - 1]["question"],
        "options": [
            attention_check_questions[taskId - 1]["options"]["A"],
            attention_check_questions[taskId - 1]["options"]["B"]
        ]
    }]
    experiment_json['options'] = []
    experiment_json["images"] = {"refviz": {"url": img_url}}

    experiment_json['meta_data'] = {"type": trend_group[grpId][taskId - 1]}

    return experiment_json

def experiment2(participant_path, taskId, grpId):
    img1_url = participant_path + '/Pair' + str(taskId - 5) +'/img1.svg'
    img2_url = participant_path + '/Pair' + str(taskId - 5) +'/img2.svg'
    question = "Trust game"
    experiment_json = {}
    experiment_json['page'] = "experiment2"
    experiment_json['variables'] = {"page_title": "", "currentTask": taskId, "totalTasks": 20, "question" : question}
    experiment_json['questions'] = [{
        "id": taskId,
        "question": attention_check_questions[taskId - 1]["question"],
        "options": [
            attention_check_questions[taskId - 1]["options"]["A"],
            attention_check_questions[taskId - 1]["options"]["B"]
        ]
    }]
    experiment_json['options'] = []
    experiment_json["images"] = {"img1": {"url": img1_url}, "img2": {"url": img2_url}}

    experiment_json['meta_data'] = {"type": trust_game_group[grpId][taskId - 5]}

    return experiment_json

def experiment3(participant_path, taskId, grpId):
    img_url =  participant_path + '/img'+ str(taskId - 16) +'.svg'
    question = prediction_story[grpId][taskId - 17]
    prediction_question = prediction_question_arr[grpId][taskId - 17]
    experiment_json = {}
    experiment_json['page'] = "experiment3"
    experiment_json['variables'] = {"page_title": "", "currentTask": taskId, "totalTasks": 20, "question" : question, "prediction_question": prediction_question}
    experiment_json['questions'] = [{
        "id": taskId,
        "question": attention_check_questions[taskId - 1]["question"],
        "options": [
            attention_check_questions[taskId - 1]["options"]["A"],
            attention_check_questions[taskId - 1]["options"]["B"]
        ]
    }]
    experiment_json['options'] = []
    experiment_json["images"] = {"refviz": {"url": img_url}}

    experiment_json['meta_data'] = {"type": prediction_group[grpId][taskId - 17]}

    return experiment_json


def prequestions_setup(counter):
    survey = {}
    survey['title'] = 'Periodic Temporal Data Visualization User Evaluation'
    survey['subject_id'] = 'subject{:04d}'.format(counter)
    survey['completion_code'] = 340976745

    survey['Consent'] = {'Option1': 'I am freely consenting to take part in the survey and by that I am agreeing that I am 18 years or older',
                         'Option2': 'I do not consent and wish to exit'}

    return survey



def questions_generator(counter):
    global universal_vis_path


    participant_trend_path = universal_vis_path + "/Trend/Grp" + str(counter)
    participant_trust_game_path = universal_vis_path + "/Trust Game Groups/Grp" + str(counter)
    participant_prediction_path = universal_vis_path + "/Prediction/Grp" + str(counter)


    survey_setup = prequestions_setup(counter)

    ########introduction page_title
    intro_page = {}
    intro_page["page"]= "introduction"
    intro_page["variables"] = {"page_title": "Welcome!"}

    ############trend tutorial page
    trend_tutorial_page = {}
    trend_tutorial_page["page"] = "trend_tutorial"
    trend_tutorial_page["variables"] = {"page_title": "Getting familiar with trends"}


    ############tutorial page
    tutorial_page = {}
    tutorial_page["page"] = "tutorial"
    tutorial_page["variables"] = {"page_title": "Tutorial"}

    #############tutorial page 2
    tutorial_page2 = {}
    tutorial_page2["page"] = "tutorial2"
    tutorial_page2["variables"] = {"page_title": "Tutorial"}

    #############tutorial page 3
    tutorial_page3 = {}
    tutorial_page3["page"] = "tutorial3"
    tutorial_page3["variables"] = {"page_title": "Tutorial"}

    #############tutorial page 3
    tutorial_page3 = {}
    tutorial_page3["page"] = "tutorial3"
    tutorial_page3["variables"] = {"page_title": "Tutorial"}

    #############tutorial page 3
    start_experiment = {}
    start_experiment["page"] = "start_experiment"
    start_experiment["variables"] = {"page_title": "Done with tutorial!"}


    tasks = []

    tasks.append(intro_page)
    tasks.append(demographic_questions())
    tasks.append(trend_tutorial_page)
    tasks.append(tutorial_page)
    tasks.append(tutorial_page2)
    tasks.append(tutorial_page3)
    tasks.append(start_experiment)

    #Add trend tasks
    tasks.append(experiment(participant_trend_path, 1, subjectId))
    tasks.append(experiment(participant_trend_path, 2, subjectId))
    tasks.append(experiment(participant_trend_path, 3, subjectId))
    tasks.append(experiment(participant_trend_path, 4, subjectId))

    #Add trust game
    tasks.append(experiment2(participant_trust_game_path, 5, subjectId))
    tasks.append(experiment2(participant_trust_game_path, 6, subjectId))
    tasks.append(experiment2(participant_trust_game_path, 7, subjectId))
    tasks.append(experiment2(participant_trust_game_path, 8, subjectId))
    tasks.append(experiment2(participant_trust_game_path, 9, subjectId))
    tasks.append(experiment2(participant_trust_game_path, 10, subjectId))
    tasks.append(experiment2(participant_trust_game_path, 11, subjectId))
    tasks.append(experiment2(participant_trust_game_path, 12, subjectId))
    tasks.append(experiment2(participant_trust_game_path, 13, subjectId))
    tasks.append(experiment2(participant_trust_game_path, 14, subjectId))
    tasks.append(experiment2(participant_trust_game_path, 15, subjectId))
    tasks.append(experiment2(participant_trust_game_path, 16, subjectId))

    #Add prediction tasks
    tasks.append(experiment3(participant_prediction_path, 17, subjectId))
    tasks.append(experiment3(participant_prediction_path, 18, subjectId))
    tasks.append(experiment3(participant_prediction_path, 19, subjectId))
    tasks.append(experiment3(participant_prediction_path, 20, subjectId))
   
    ###########completion pages
    complete_page = {}
    complete_page['page'] = "complete"
    complete_page['variables'] = {"page_title": "Thank you!", "completionCode": survey_setup['completion_code']}

    tasks.append(complete_page)


    survey_setup['tasks'] = tasks
    # survey_setup['participant_color'] = participant_color
    # #survey_setup['switch'] = switch
    # survey_setup['question2_class_type'] = participant_class_type

    #flip the switch for type 2 ; if this participant got all true predictions for type 2 questions then by flipping this switch , the next participant will get all false predictions

    return survey_setup

subjectId = 0
while subjectId != counter:

    q = questions_generator(counter =subjectId)

    #Serializing json object
    #json_object = json.dumps(q, ensure_ascii=False, indent = 4)

    #Writing to json file
    with open('experiment/subjects/subject{:04d}.json'.format(subjectId), 'w' ) as outfile:
        json.dump(q, outfile, indent = 4, ensure_ascii=False)
        #json.dumps(json_object)

    subjectId = subjectId + 1
