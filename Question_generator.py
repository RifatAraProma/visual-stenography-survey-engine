import json
import random
from pathlib import Path

#define and declare switch
#Switch = True

#Accuracy range
a_l = [65, 66, 67, 68, 69, 70]
a_m = [75, 76, 77, 78, 79, 80]
a_h = [90, 91, 92, 93, 94, 95]

Accuracy_levels = ['High', 'Medium', 'Low']

#About DataSets
Datasets = ['Haberman"s Survival', 'South German Credit', 'Liver Disease']

#models used
models = {'A': 'Random_Forest', 'B': 'KNN', 'C': 'D_tree', 'D': 'SVM' }

#Universal color path
#universal_vis_path = Path("/Survey_engine/survey_engine/docs/images/Decision_Survey_Visualizations")
universal_vis_path = "/images/Decision_Survey_Visualizations"

#color lists
colors = ['BlueRed', 'RedBlue', 'PurpleDogerblue', 'DogerbluePurple']
jumbled_colors = random.sample(colors, len(colors))


#participant bucket for type 2 questions
class_t2 = ['Accuracy', 'Visualization', 'Both']
class_type2 = random.sample(class_t2, len(class_t2))


#Universal list for control type question 1
control_1_list = [['RF', 'KNN'], ['RF', 'DTREE'], ['RF', 'SVM'], ['KNN', 'DTREE'], ['KNN', 'SVM'], ['DTREE', 'SVM']]
control_HS_1_list = random.sample(control_1_list, len(control_1_list))
control_SGC_1_list = random.sample(control_1_list, len(control_1_list))
control_LD_1_list = random. sample(control_1_list, len(control_1_list))

#Universal list for accuracy type question 1
accuracy_1_list = [['RF', random.choice(a_l), 'KNN', random.choice(a_m)], ['RF', random.choice(a_l), 'KNN', random.choice(a_h)], ['RF', random.choice(a_m), 'KNN', random.choice(a_l)], ['RF', random.choice(a_m), 'KNN', random.choice(a_h)], ['RF', random.choice(a_h), 'KNN', random.choice(a_l)], ['RF', random.choice(a_h), 'KNN', random.choice(a_m)],
['RF', random.choice(a_l), 'DTREE', random.choice(a_m)], ['RF', random.choice(a_l), 'DTREE', random.choice(a_h)], ['RF', random.choice(a_m), 'DTREE', random.choice(a_l)], ['RF', random.choice(a_m), 'DTREE', random.choice(a_h)], ['RF', random.choice(a_h), 'DTREE', random.choice(a_l)], ['RF', random.choice(a_h), 'DTREE', random.choice(a_m)],
['RF', random.choice(a_l), 'SVM', random.choice(a_m)], ['RF', random.choice(a_l), 'SVM', random.choice(a_h)], ['RF', random.choice(a_m), 'SVM', random.choice(a_l)], ['RF', random.choice(a_m), 'SVM', random.choice(a_h)], ['RF', random.choice(a_h), 'SVM', random.choice(a_l)], ['RF', random.choice(a_h), 'SVM', random.choice(a_m)],
['KNN', random.choice(a_l), 'DTREE', random.choice(a_m)], ['KNN', random.choice(a_l), 'DTREE', random.choice(a_h)], ['KNN', random.choice(a_m), 'DTREE', random.choice(a_l)], ['KNN', random.choice(a_m), 'SVM', random.choice(a_h)], ['KNN', random.choice(a_h), 'DTREE', random.choice(a_l)], ['KNN', random.choice(a_h), 'DTREE', random.choice(a_m)],
['KNN', random.choice(a_l), 'SVM', random.choice(a_m)], ['KNN', random.choice(a_l), 'SVM', random.choice(a_h)], ['KNN', random.choice(a_m), 'SVM', random.choice(a_l)],['KNN', random.choice(a_m), 'SVM', random.choice(a_h)], ['KNN', random.choice(a_h), 'SVM', random.choice(a_l)], ['KNN', random.choice(a_h), 'SVM', random.choice(a_m)],
['DTREE', random.choice(a_l), 'SVM', random.choice(a_m)], ['DTREE', random.choice(a_l), 'SVM', random.choice(a_h)], ['DTREE', random.choice(a_m), 'SVM', random.choice(a_l)], ['DTREE', random.choice(a_m), 'SVM', random.choice(a_h)], ['DTREE', random.choice(a_h), 'SVM', random.choice(a_l)], ['DTREE', random.choice(a_h), 'SVM', random.choice(a_m)]
]
accuracy_HS_1_list = random.sample(accuracy_1_list, len(accuracy_1_list))
accuracy_SGC_1_list = random.sample(accuracy_1_list, len(accuracy_1_list))
accuracy_LD_1_list = random.sample(accuracy_1_list, len(accuracy_1_list))

#Universal list for accuracy level type question 1
accuracylevel_1_list = [['RF', 'Low', 'KNN', 'Medium'], ['RF', 'Low', 'KNN', 'High'], ['RF', 'Medium', 'KNN', 'Low'], ['RF', 'Medium', 'KNN', 'High'], ['RF', 'High', 'KNN', 'Low'], ['RF', 'High', 'KNN', 'Medium'],
['RF', 'Low', 'DTREE', 'Medium'], ['RF', 'Low', 'DTREE', 'High'], ['RF', 'Medium', 'DTREE', 'Low'], ['RF', 'Medium', 'DTREE', 'High'], ['RF', 'High', 'DTRE', 'Low'], ['RF', 'High', 'DTREE', 'Medium'],
['RF', 'Low', 'SVM', 'Medium'], ['RF', 'Low', 'SVM', 'High'], ['RF', 'Medium', 'SVM', 'Low'], ['RF', 'Medium', 'SVM', 'High'], ['RF', 'High', 'SVM', 'Low'], ['RF', 'High', 'SVM', 'Medium'],
['KNN', 'Low', 'DTREE', 'Medium'], ['KNN', 'Low', 'DTREE', 'High'], ['KNN', 'Medium', 'DTREE', 'Low'], ['KNN', 'Medium', 'DTREE', 'High'], ['KNN', 'High', 'DTREE', 'Low'], ['KNN', 'High', 'DTREE', 'Medium'],
['KNN', 'Low', 'SVM', 'Medium'], ['KNN', 'Low', 'SVM', 'High'], ['KNN', 'Medium', 'SVM','Low'], ['KNN', 'Medium', 'SVM', 'High'], ['KNN', 'High', 'SVM', 'Low'], ['KNN', 'High', 'SVM', 'Medium'],
['DTREE', 'Low', 'SVM', 'Medium'], ['DTREE', 'Low', 'SVM', 'High'], ['DTREE', 'Medium', 'SVM', 'Low'], ['DTREE', 'Medium', 'SVM', 'High'], ['DTREE', 'High', 'SVM', 'Low'], ['DTREE', 'High', 'SVM', 'Medium']
]
accuracylevel_HS_1_list = random.sample(accuracylevel_1_list, len(accuracylevel_1_list))
accuracylevel_SGC_1_list = random.sample(accuracylevel_1_list, len(accuracylevel_1_list))
accuracylevel_LD_1_list = random.sample(accuracylevel_1_list, len(accuracylevel_1_list))

#Universal list for control type question 2 Haberman's survival
control_HS_2_list_origin = [['38', 'RF', 'Survived','original'], ['38', 'KNN', 'Survived','original'], ['38', 'DTREE', 'Survived','original'], ['38', 'SVM', 'Survived','original'],
['110', 'RF', 'Survived','original'], ['110', 'KNN', 'Survived','original'], ['110', 'DTREE', 'Survived','original'], ['110', 'SVM', 'Survived','original'],
['160', 'RF', 'Died','original'], ['160', 'KNN', 'Died','original'], ['160', 'DTREE', 'Died','original'], ['160', 'SVM', 'Died','original'],
['38', 'RF', 'Died','altered'], ['38', 'KNN', 'Died','altered'], ['38', 'DTREE', 'Died','altered'], ['38', 'SVM', 'Died','altered'],
['110', 'RF', 'Died','altered'], ['110', 'KNN', 'Died','altered'], ['110', 'DTREE', 'Died','altered'], ['110', 'SVM', 'Died','altered'],
['160', 'RF', 'Survived','altered'], ['160', 'KNN', 'Survived','altered'], ['160', 'DTREE', 'Survived','altered'], ['160', 'SVM', 'Survived','altered']]
control_HS_2_list_original = random.sample(control_HS_2_list_origin, len(control_HS_2_list_origin))

#Universal lists for control type question 2 South German Credit
control_SGC_2_list_origin = [['997', 'RF', 'Bad Credit','original'], ['997', 'KNN', 'Bad Credit','original'], ['997', 'DTREE', 'Bad Credit','original'], ['997', 'SVM', 'Bad Credit','original'],
['518', 'RF', 'Bad Credit','original'], ['518', 'KNN', 'Bad Credit','original'], ['518', 'DTREE', 'Bad Credit','original'], ['518', 'SVM', 'Bad Credit','original'],
['472', 'RF', 'Good Credit','original'], ['472', 'KNN', 'Good Credit','original'], ['472', 'DTREE', 'Good Credit','original'], ['472', 'SVM', 'Good Credit','original'],
['997', 'RF', 'Good Credit','altered'], ['997', 'KNN', 'Good Credit','altered'], ['997', 'DTREE', 'Good Credit','altered'], ['997', 'SVM', 'Good Credit','altered'],
['518', 'RF', 'Good Credit','altered'], ['518', 'KNN', 'Good Credit','altered'], ['518', 'DTREE', 'Good Credit','altered'], ['518', 'SVM', 'Good Credit','altered'],
['472', 'RF','Bad Credit','altered'], ['472', 'KNN', 'Bad Credit','altered'], ['472', 'DTREE', 'Bad Credit','altered'], ['472', 'SVM', 'Bad Credit','altered']]
control_SGC_2_list_original = random.sample(control_SGC_2_list_origin, len(control_SGC_2_list_origin))

#Universal lists for control type question 2 Liver Disease
control_LD_2_list_origin = [['45', 'RF', 'Healthy Liver','original'], ['45', 'KNN', 'Healthy Liver','original'], ['45', 'DTREE', 'Healthy Liver','original'], ['45','SVM', 'Healthy Liver','original'],
['190', 'RF', 'Liver Disease','original'], ['190', 'KNN', 'Liver Disease','original'], ['190', 'DTREE', 'Liver Disease','original'], ['190', 'SVM', 'Liver Disease','original'],
['555', 'RF', 'Liver Disease','original'], ['555', 'KNN', 'Liver Disease','original'], ['555', 'DTREE', 'Liver Disease','original'], ['555', 'SVM', 'Liver Disease','original'],
['45', 'RF', 'Liver Disease','altered'], ['45', 'KNN', 'Liver Disease','altered'], ['45', 'DTREE', 'Liver Disease','altered'], ['45', 'SVM', 'Liver Disease','altered'],
['190', 'RF', 'Healthy Liver','altered'], ['190', 'KNN', 'Healthy Liver','altered'], ['190', 'DTREE', 'Healthy Liver','altered'], ['190', 'SVM', 'Healthy Liver','altered'],
['555', 'RF', 'Healthy Liver','altered'], ['555', 'KNN', 'Healthy Liver','altered'], ['555', 'DTREE', 'Healthy Liver','altered'], ['555', 'SVM', 'Healthy Liver','altered']]
control_LD_2_list_original = random.sample(control_LD_2_list_origin, len(control_LD_2_list_origin))

#Universal Lists for accuracy question type 2 Haberman's Survival
accuracy_HS_2_list_origin = [['38', 'RF', 'Survived', random.choice(a_l),'original'], ['38', 'RF', 'Survived', random.choice(a_m),'original'], ['38', 'RF', 'Survived', random.choice(a_h),'original'], ['38', 'SVM', 'Survived', random.choice(a_l),'original'], ['38', 'SVM', 'Survived', random.choice(a_m),'original'], ['38', 'SVM', 'Survived', random.choice(a_h),'original'],
['38', 'KNN', 'Survived', random.choice(a_l),'original'], ['38', 'KNN', 'Survived', random.choice(a_m),'original'], ['38', 'KNN', 'Survived', random.choice(a_h),'original'], ['38', 'DTREE', 'Survived', random.choice(a_l),'original'], ['38', 'DTREE', 'Survived', random.choice(a_m),'original'], ['38', 'DTREE', 'Survived', random.choice(a_h),'original'],
['110', 'RF', 'Survived', random.choice(a_l),'original'], ['110', 'RF', 'Survived', random.choice(a_m),'original'], ['110', 'RF', 'Survived', random.choice(a_h),'original'], ['110', 'KNN', 'Survived', random.choice(a_l),'original'], ['110', 'KNN', 'Survived', random.choice(a_m),'original'], ['110', 'KNN', 'Survived', random.choice(a_h),'original'],
['110', 'DTREE', 'Survived', random.choice(a_l),'original'], ['110', 'DTREE', 'Survived', random.choice(a_m),'original'], ['110', 'DTREE', 'Survived', random.choice(a_h),'original'], ['110', 'SVM', 'Survived', random.choice(a_l),'original'], ['110', 'SVM', 'Survived', random.choice(a_m),'original'], ['110', 'SVM', 'Survived', random.choice(a_h),'original'],
['160', 'RF', 'Died', random.choice(a_l),'original'], ['160', 'RF', 'Died', random.choice(a_m),'original'], ['160', 'RF', 'Died', random.choice(a_h),'original'], ['160', 'KNN', 'Died', random.choice(a_l),'original'], ['160', 'KNN', 'Died', random.choice(a_m),'original'], ['160', 'KNN', 'Died', random.choice(a_h),'original'],
['160', 'DTREE', 'Died', random.choice(a_l),'original'], ['160', 'DTREE', 'Died', random.choice(a_m),'original'], ['160', 'DTREE', 'Died', random.choice(a_h),'original'], ['160', 'SVM', 'Died', random.choice(a_l),'original'], ['160', 'SVM', 'Died', random.choice(a_m),'original'],['160', 'SVM', 'Died', random.choice(a_h),'original'],
['38', 'RF', 'Died', random.choice(a_l),'altered'], ['38', 'RF', 'Died', random.choice(a_m),'altered'], ['38', 'RF', 'Died', random.choice(a_h),'altered'], ['38', 'KNN', 'Died', random.choice(a_l),'altered'], ['38', 'KNN', 'Died', random.choice(a_m),'altered'], ['38', 'KNN', 'Died', random.choice(a_h),'altered'],
['38', 'DTREE', 'Died', random.choice(a_l),'altered'], ['38', 'DTREE', 'Died', random.choice(a_m),'altered'], ['38', 'DTREE', 'Died', random.choice(a_h),'altered'], ['38', 'SVM', 'Died', random.choice(a_l),'altered'], ['38', 'SVM', 'Died', random.choice(a_m),'altered'], ['38', 'SVM', 'Died', random.choice(a_h),'altered'],
['110', 'RF', 'Died', random.choice(a_l),'altered'], ['110', 'RF', 'Died', random.choice(a_m),'altered'], ['110', 'RF', 'Died', random.choice(a_h),'altered'], ['110', 'KNN', 'Died', random.choice(a_l),'altered'], ['110', 'KNN', 'Died', random.choice(a_m),'altered'], ['110', 'KNN', 'Died', random.choice(a_h),'altered'],
['110', 'DTREE', 'Died', random.choice(a_l),'altered'], ['110', 'DTREE', 'Died', random.choice(a_m),'altered'], ['110', 'DTREE', 'Died', random.choice(a_h),'altered'], ['110', 'SVM', 'Died', random.choice(a_l),'altered'], ['110','SVM', 'Died', random.choice(a_m),'altered'], ['110', 'SVM', 'Died', random.choice(a_h),'altered'],
['160', 'RF', 'Survived', random.choice(a_l),'altered'], ['160', 'RF', 'Survived', random.choice(a_m),'altered'], ['160', 'RF', 'Survived', random.choice(a_h),'altered'], ['160', 'KNN', 'Survived', random.choice(a_l),'altered'], ['160', 'KNN', 'Survived', random.choice(a_m),'altered'], ['160', 'KNN', 'Survived', random.choice(a_h),'altered'],
['160', 'DTREE', 'Survived', random.choice(a_l),'altered'], ['160', 'DTREE', 'Survived', random.choice(a_m),'altered'], ['160', 'DTREE', 'Survived', random.choice(a_h),'altered'], ['160', 'SVM', 'Survived', random.choice(a_l),'altered'], ['160', 'SVM', 'Survived', random.choice(a_m),'altered'], ['160', 'SVM', 'Survived', random.choice(a_h),'altered']]
accuracy_HS_2_list_original = random.sample(accuracy_HS_2_list_origin, len(accuracy_HS_2_list_origin))

#Universal lists for accuracy question type 2 SGC
accuracy_SGC_2_list_origin = [['997', 'RF', 'Bad Credit', random.choice(a_l),'original'], ['997', 'RF', 'Bad Credit', random.choice(a_m),'original'], ['997', 'RF', 'Bad Credit', random.choice(a_h),'original'], ['997', 'KNN', 'Bad Credit', random.choice(a_l),'original'], ['997', 'KNN', 'Bad Credit', random.choice(a_m),'original'], ['997', 'KNN', 'Bad Credit', random.choice(a_h),'original'],
['997', 'DTREE', 'Bad Credit', random.choice(a_l),'original'], ['997', 'DTREE', 'Bad Credit', random.choice(a_m),'original'], ['997', 'DTREE', 'Bad Credit', random.choice(a_h),'original'], ['997', 'SVM', 'Bad Credit', random.choice(a_l),'original'], ['997', 'SVM', 'Bad Credit', random.choice(a_m),'original'], ['997', 'SVM', 'Bad Credit', random.choice(a_h),'original'],
['58', 'RF', 'Bad Credit', random.choice(a_l),'original'], ['58', 'RF', 'Bad Credit', random.choice(a_m),'original'], ['58', 'RF', 'Bad Credit', random.choice(a_h),'original'], ['58', 'KNN', 'Bad Credit', random.choice(a_l),'original'], ['58', 'KNN', 'Bad Credit', random.choice(a_m),'original'], ['58', 'KNN', 'Bad Credit', random.choice(a_h),'original'],
['58', 'DTREE', 'Bad Credit', random.choice(a_l),'original'], ['58', 'DTREE', 'Bad Credit', random.choice(a_m),'original'], ['58', 'DTREE', 'Bad Credit', random.choice(a_h),'original'], ['58', 'SVM', 'Bad Credit', random.choice(a_l),'original'], ['58', 'SVM', 'Bad Credit', random.choice(a_m),'original'], ['58', 'SVM', 'Bad Credit', random.choice(a_h),'original'],
['472', 'RF', 'Good Credit', random.choice(a_l),'original'], ['472', 'RF', 'Good Credit', random.choice(a_m),'original'], ['472', 'RF', 'Good Credit', random.choice(a_h),'original'], ['472', 'KNN', 'Good Credit', random.choice(a_l),'original'], ['472', 'KNN', 'Good Credit', random.choice(a_m),'original'], ['472', 'KNN', 'Good Credit', random.choice(a_h),'original'],
['472', 'DTREE', 'Good Credit', random.choice(a_l),'original'], ['472', 'DTREE', 'Good Credit', random.choice(a_m),'original'], ['472', 'DTREE', 'Good Credit', random.choice(a_h),'original'], ['472', 'SVM', 'Good Credit', random.choice(a_l),'original'], ['472', 'SVM', 'Good Credit', random.choice(a_m),'original'], ['472', 'SVM', 'Good Credit', random.choice(a_h),'original'],
['997', 'RF', 'Good Credit', random.choice(a_l),'altered'], ['997', 'RF', 'Good Credit', random.choice(a_m),'altered'], ['997', 'RF', 'Good Credit', random.choice(a_h),'altered'], ['997', 'KNN', 'Good Credit', random.choice(a_l),'altered'], ['997', 'KNN', 'Good Credit', random.choice(a_m),'altered'], ['997', 'KNN', 'Good Credit', random.choice(a_h),'altered'],
['997', 'DTREE', 'Good Credit', random.choice(a_l),'altered'], ['997', 'DTREE' 'Good Credit', random.choice(a_m),'altered'], ['997', 'DTREE', 'Good Credit', random.choice(a_h),'altered'], ['997', 'SVM', 'Good Credit', random.choice(a_l),'altered'], ['997', 'SVM', 'Good Credit', random.choice(a_m),'altered'], ['997', 'SVM', 'Good Credit', random.choice(a_h),'altered'],
['58', 'RF', 'Good Credit', random.choice(a_l),'altered'], ['58', 'RF', 'Good Credit', random.choice(a_m),'altered'], ['58', 'RF', 'Good Credit', random.choice(a_h),'altered'], ['58', 'KNN', 'Good Credit', random.choice(a_l),'altered'], ['58', 'KNN', 'Good Credit', random.choice(a_m),'altered'], ['58', 'KNN', 'Good Credit', random.choice(a_h),'altered'],
['58', 'DTREE', 'Good Credit', random.choice(a_l),'altered'], ['58', 'DTREE', 'Good Credit', random.choice(a_m),'altered'], ['58', 'DTREE', 'Good Credit', random.choice(a_h),'altered'], ['58', 'SVM', 'Good Credit', random.choice(a_l),'altered'], ['58', 'SVM', 'Good Credit', random.choice(a_m),'altered'], ['58', 'SVM', 'Good Credit', random.choice(a_h),'altered'],
['472', 'RF', 'Bad Credit', random.choice(a_l),'altered'], ['472', 'RF', 'Bad Credit', random.choice(a_m),'altered'], ['472', 'RF', 'Bad Credit', random.choice(a_h),'altered'], ['472', 'KNN', 'Bad Credit', random.choice(a_l),'altered'], ['472', 'KNN', 'Bad Credit', random.choice(a_m),'altered'], ['472', 'KNN', 'Bad Credit', random.choice(a_h),'altered'],
['472', 'DTREE', 'Bad Credit', random.choice(a_l),'altered'], ['472', 'DTREE', 'Bad Credit', random.choice(a_m),'altered'], ['472', 'DTREE', 'Bad Credit', random.choice(a_h),'altered'], ['472', 'SVM', 'Bad Credit', random.choice(a_l),'altered'], ['472', 'SVM', 'Bad Credit', random.choice(a_m),'altered'], ['472', 'SVM', 'Bad Credit', random.choice(a_h),'altered']]
accuracy_SGC_2_list_original = random.sample(accuracy_SGC_2_list_origin, len(accuracy_SGC_2_list_origin))

#Universal List for accuracy question type 2 LD
accuracy_LD_2_list_origin = [['41', 'RF', 'Healthy Liver', random.choice(a_l),'original'], ['41', 'RF', 'Healthy Liver', random.choice(a_m),'original'], ['41', 'RF', 'Healthy Liver', random.choice(a_h),'original'], ['41', 'KNN', 'Healthy Liver', random.choice(a_l),'original'], ['41', 'KNN', 'Healthy Liver', random.choice(a_m),'original'], ['41', 'KNN', 'Healthy Liver', random.choice(a_h),'original'],
['41', 'DTREE', 'Healthy Liver', random.choice(a_l),'original'], ['41', 'DTREE', 'Healthy Liver', random.choice(a_m),'original'], ['41', 'DTREE', 'Healthy Liver', random.choice(a_h)], ['41', 'SVM', 'Healthy Liver', random.choice(a_l)], ['41', 'SVM', 'Healthy Liver', random.choice(a_m),'original'], ['41', 'SVM', 'Healthy Liver', random.choice(a_h),'original'],
['190', 'RF', 'Liver Disease', random.choice(a_l),'original'], ['190', 'RF', 'Liver Disease', random.choice(a_m),'original'], ['190', 'RF', 'Liver Disease', random.choice(a_h),'original'], ['190', 'KNN', 'Liver Disease', random.choice(a_l),'original'], ['190', 'KNN', 'Liver Disease', random.choice(a_m),'original'], ['190', 'KNN', 'Liver Disease', random.choice(a_h),'original'],
['190', 'DTREE', 'Liver Disease', random.choice(a_l),'original'], ['190', 'DTREE', 'Liver Disease', random.choice(a_m),'original'], ['190', 'DTREE', 'Liver Disease', random.choice(a_h),'original'], ['190', 'SVM', 'Liver Disease', random.choice(a_l),'original'], ['190', 'SVM', 'Liver Disease', random.choice(a_m),'original'], ['190', 'SVM', 'Liver Disease', random.choice(a_h),'original'],
['555', 'RF', 'Liver Disease', random.choice(a_l),'original'], ['555', 'RF', 'Liver Disease', random.choice(a_m),'original'], ['555', 'RF', 'Liver Disease', random.choice(a_h),'original'], ['555', 'KNN', 'Liver Disease', random.choice(a_l),'original'], ['555', 'KNN', 'Liver Disease', random.choice(a_m),'original'], ['555', 'KNN', 'Liver Disease', random.choice(a_h),'original'],
['555', 'DTREE', 'Liver Disease', random.choice(a_l),'original'], ['555', 'DTREE', 'Liver Disease', random.choice(a_m),'original'], ['555', 'DTREE', 'Liver Disease', random.choice(a_h),'original'], ['555', 'SVM', 'Liver Disease', random.choice(a_l),'original'], ['555', 'SVM', 'Liver Disease', random.choice(a_m),'original'], ['555', 'SVM', 'Liver Disease', random.choice(a_h),'original'],
['41', 'RF', 'Liver Disease', random.choice(a_l),'altered'], ['41', 'RF', 'Liver Disease', random.choice(a_m),'altered'], ['41', 'RF', 'Liver Disease', random.choice(a_h),'altered'], ['41', 'KNN', 'Liver Disease', random.choice(a_l),'altered'], ['41', 'KNN', ' Liver Disease', random.choice(a_m),'altered'], ['41', 'KNN', 'Liver Disease', random.choice(a_h)],
['41', 'DTREE', 'Liver Disease', random.choice(a_l),'altered'], ['41', 'DTREE', 'Liver Disease', random.choice(a_m),'altered'], ['41', 'DTREE', 'Liver Disease', random.choice(a_h),'altered'], ['41', 'SVM', 'Liver Disease', random.choice(a_l),'altered'], ['41', 'SVM', 'Liver Disease', random.choice(a_m),'altered'], ['41', 'SVM', 'Liver Disease' , random.choice(a_h),'altered'],
['190', 'RF', 'Healthy Liver', random.choice(a_l),'altered'], ['190', 'RF', ' Healthy Liver', random.choice(a_m),'altered'], ['190', 'RF', 'Healthy Liver ', random.choice(a_h),'altered'], ['190', 'KNN', 'Healthy Liver ', random.choice(a_l),'altered'], ['190', 'KNN', 'Healthy Liver ', random.choice(a_m),'altered'], ['190', 'KNN', 'Healthy Liver ', random.choice(a_h),'altered'],
['190', 'DTREE', 'Healthy Liver ', random.choice(a_l),'altered'], ['190', 'DTREE', 'Healthy Liver ', random.choice(a_m),'altered'], ['190', 'DTREE', 'Healthy Liver ', random.choice(a_h),'altered'], ['190', 'SVM', 'Healthy Liver', random.choice(a_l),'altered'], ['190', 'SVM', 'Healthy Liver ', random.choice(a_m),'altered'], ['190', 'SVM', 'Healthy Liver ', random.choice(a_h),'altered'],
['555', 'RF', 'Healthy Liver ', random.choice(a_l),'altered'], ['555', 'RF', 'Healthy Liver ', random.choice(a_m),'altered'], ['555', 'RF', 'Healthy Liver ', random.choice(a_h),'altered'], ['555', 'KNN', 'Healthy Liver ', random.choice(a_l),'altered'], ['555', 'KNN', 'Healthy Liver ', random.choice(a_m),'altered'], ['555', 'KNN', 'Healthy Liver', random.choice(a_h),'altered'],
['555', 'DTREE', 'Healthy Liver', random.choice(a_l),'altered'], ['555', 'DTREE', 'Healthy Liver', random.choice(a_m),'altered'], ['555', 'DTREE', 'Healthy Liver', random.choice(a_h),'altered'], ['555', 'SVM', 'Healthy Liver ', random.choice(a_l),'altered'], ['555', 'SVM', 'Healthy Liver', random.choice(a_m),'altered'], ['555', 'SVM', ' Healthy Liver ', random.choice(a_h),'altered']]
accuracy_LD_2_list_original = random.sample(accuracy_LD_2_list_origin, len(accuracy_LD_2_list_origin))

#Universal List for accuracy level question type 2 Habermans Survival
accuracylevel_HS_2_list_origin = [['38', 'RF', 'Survived', 'Low','original'], ['38', 'RF', 'Survived', 'Medium','original'], ['38', 'RF', 'Survived', 'High','original'], ['38', 'SVM', 'Survived', 'Low','original'], ['38', 'SVM', 'Survived', 'Medium','original'], ['38', 'SVM', 'Survived', 'High','original'],
['38', 'KNN', 'Survived', 'Low','original'], ['38', 'KNN', 'Survived', 'Medium','original'], ['38', 'KNN', 'Survived', 'High','original'], ['38', 'DTREE', 'Survived', 'Low','original'], ['38', 'DTREE', 'Survived', 'Medium','original'], ['38', 'DTREE', 'Survived', 'High','original'],
['110', 'RF', 'Survived', 'Low','original'], ['110', 'RF', 'Survived', 'Medium','original'], ['110', 'RF', 'Survived', 'High','original'], ['110', 'KNN', 'Survived', 'Low','original'], ['110', 'KNN', 'Survived', 'Medium','original'], ['110', 'KNN', 'Survived', 'High','original'],
['110', 'DTREE', 'Survived', 'Low','original'], ['110', 'DTREE', 'Survived', 'Medium','original'], ['110', 'DTREE', 'Survived', 'High','original'], ['110', 'SVM', 'Survived', 'Low','original'], ['110', 'SVM', 'Survived', 'Medium','original'], ['110', 'SVM', 'Survived', 'High','original'],
['160', 'RF', 'Died', 'Low','original'], ['160', 'RF', 'Died', 'Medium','original'], ['160', 'RF', 'Died', 'High','original'], ['160', 'KNN', 'Died', 'Low','original'], ['160', 'KNN', 'Died', 'Medium','original'], ['160', 'KNN', 'Died', 'High','original'],
['160', 'DTREE', 'Died', 'Low','original'], ['160', 'DTREE', 'Died', 'Medium','original'], ['160', 'DTREE', 'Died', 'High','original'], ['160', 'SVM', 'Died', 'Low','original'], ['160', 'SVM', 'Died', 'Medium','original'], ['160', 'SVM', 'Died', 'High','original'],
['38', 'RF', 'Died', 'Low','altered'], ['38', 'RF', 'Died', 'Medium','altered'], ['38', 'RF', 'Died', 'High','altered'], ['38', 'KNN', 'Died', 'Low','altered'], ['38', 'KNN', 'Died', 'Medium','altered'], ['38', 'KNN', 'Died', 'High','altered'],
['38', 'DTREE', 'Died', 'Low','altered'], ['38', 'DTREE', 'Died', 'Medium','altered'], ['38', 'DTREE', 'Died', 'High','altered'], ['38', 'SVM', 'Died', 'Low','altered'], ['38', 'SVM', 'Died', 'Medium','altered'], ['38', 'SVM', 'Died', 'High','altered'],
['110', 'RF', 'Died', 'Low','altered'], ['110', 'RF', 'Died', 'Medium','altered'], ['110', 'RF', 'Died', 'High','altered'], ['110', 'KNN', 'Died', 'Low','altered'], ['110', 'KNN', 'Died', 'Medium','altered'], ['110', 'KNN', 'Died', 'High','altered'],
['110', 'DTREE', 'Died', 'Low','altered'], ['110', 'DTREE', 'Died', 'Medium','altered'], ['110', 'DTREE', 'Died', 'High','altered'], ['110', 'SVM', 'Died', 'Low','altered'], ['110','SVM', 'Died', 'Medium','altered'], ['110', 'SVM', 'Died', 'High','altered'],
['160', 'RF', 'Survived', 'Low','altered'], ['160', 'RF', 'Survived', 'Medium','altered'], ['160', 'RF', 'Survived', 'High','altered'], ['160', 'KNN', 'Survived', 'Low','altered'], ['160', 'KNN', 'Survived', 'Medium','altered'], ['160', 'KNN', 'Survived', 'High','altered'],
['160', 'DTREE', 'Survived', 'Low','altered'], ['160', 'DTREE', 'Survived', 'Medium','altered'], ['160', 'DTREE', 'Survived', 'High','altered'], ['160', 'SVM', 'Survived','Low','altered'], ['160', 'SVM', 'Survived', 'Medium','altered'], ['160', 'SVM', 'Survived', 'High','altered']]
accuracylevel_HS_2_list_original = random.sample(accuracylevel_HS_2_list_origin, len(accuracylevel_HS_2_list_origin))

#Universal list for accuracy  level type question 2 for South German Credit
accuracylevel_SGC_2_list_origin = [['997', 'RF', 'Bad Credit', 'Low','original'], ['997', 'RF', 'Bad Credit', 'Medium','original'], ['997', 'RF', 'Bad Credit', 'High','original'], ['997', 'KNN', 'Bad Credit', 'Low','original'], ['997', 'KNN', 'Bad Credit', 'Medium','original'], ['997', 'KNN', 'Bad Credit', 'High','original'],
['997', 'DTREE', 'Bad Credit', 'Low','original'], ['997', 'DTREE', 'Bad Credit', 'Medium','original'], ['997', 'DTREE', 'Bad Credit', 'High','original'], ['997', 'SVM', 'Bad Credit', 'Low','original'], ['997', 'SVM', 'Bad Credit', 'Medium','original'], ['997', 'SVM', 'Bad Credit', 'High','original'],
['58', 'RF', 'Bad Credit', 'Low','original'], ['58', 'RF', 'Bad Credit', 'Medium','original'], ['58', 'RF', 'Bad Credit', 'High','original'], ['58', 'KNN', 'Bad Credit', 'Low','original'], ['58', 'KNN', 'Bad Credit', 'Medium','original'], ['58', 'KNN', 'Bad Credit', 'High','original'],
['58', 'DTREE', 'Bad Credit', 'Low','original'], ['58', 'DTREE', 'Bad Credit', 'Medium','original'], ['58', 'DTREE', 'Bad Credit','High','original'], ['58', 'SVM', 'Bad Credit', 'Low','original'], ['58', 'SVM', 'Bad Credit', 'Medium','original'], ['58', 'SVM', 'Bad Credit', 'High','original'],
['472', 'RF', 'Good Credit', 'Low','original'], ['472', 'RF', 'Good Credit', 'Medium','original'], ['472', 'RF', 'Good Credit', 'High','original'], ['472', 'KNN', 'Good Credit', 'Low','original'], ['472', 'KNN', 'Good Credit', 'Medium','original'], ['472', 'KNN', 'Good Credit', 'High','original'],
['472', 'DTREE', 'Good Credit', 'Low','original'], ['472', 'DTREE', 'Good Credit','Medium','original'], ['472', 'DTREE', 'Good Credit', 'High','original'], ['472', 'SVM', 'Good Credit', 'Low','original'], ['472', 'SVM', 'Good Credit', 'Medium','original'], ['472', 'SVM', 'Good Credit', 'High','original'],
['997', 'RF', 'Good Credit', 'Low','altered'], ['997', 'RF', 'Good Credit', 'Medium','altered'], ['997', 'RF', 'Good Credit', 'High','altered'], ['997', 'KNN', 'Good Credit', 'Low','altered'], ['997', 'KNN', 'Good Credit', 'Medium','altered'], ['997', 'KNN', 'Good Credit', 'High','altered'],
['997', 'DTREE', 'Good Credit', 'Low','altered'], ['997', 'DTREE' 'Good Credit', 'Medium','altered'], ['997', 'DTREE', 'Good Credit', 'High','altered'], ['997', 'SVM', 'Good Credit', 'Low','altered'], ['997', 'SVM', 'Good Credit', 'Medium','altered'], ['997', 'SVM', 'Good Credit', 'High','altered'],
['58', 'RF', 'Good Credit', 'Low','altered'], ['58', 'RF', 'Good Credit', 'Medium','altered'], ['58', 'RF', 'Good Credit', 'High','altered'], ['58', 'KNN', 'Good Credit', 'Low','altered'], ['58', 'KNN', 'Good Credit', 'Medium','altered'], ['58', 'KNN', 'Good Credit', 'High','altered'],
['58', 'DTREE', 'Good Credit', 'Low','altered'], ['58', 'DTREE', 'Good Credit', 'Medium','altered'], ['58', 'DTREE', 'Good Credit', 'High','altered'], ['58', 'SVM', 'Good Credit', 'Low','altered'], ['58', 'SVM', 'Good Credit', 'Medium','altered'], ['58', 'SVM', 'Good Credit', 'High','altered'],
['472', 'RF', 'Bad Credit', 'Low','altered'], ['472', 'RF', 'Bad Credit', 'Medium','altered'], ['472', 'RF', 'Bad Credit', 'High','altered'], ['472', 'KNN', 'Bad Credit', 'Low','altered'], ['472', 'KNN', 'Bad Credit', 'Medium','altered'], ['472', 'KNN', 'Bad Credit', 'High','altered'],
['472', 'DTREE', 'Bad Credit', 'Low','altered'], ['472', 'DTREE', 'Bad Credit', 'Medium','altered'], ['472', 'DTREE', 'Bad Credit', 'High','altered'], ['472', 'SVM', 'Bad Credit', 'Low','altered'], ['472', 'SVM', 'Bad Credit', 'Medium','altered'], ['472', 'SVM', 'Bad Credit', 'High','altered']]
accuracylevel_SGC_2_list_original = random.sample(accuracylevel_SGC_2_list_origin, len(accuracylevel_SGC_2_list_origin))

#Universal list for accuracy level type question 2 for Liver disease
accuracylevel_LD_2_list_origin = [['41', 'RF', 'Healthy Liver', 'Low','original'], ['41', 'RF', 'Healthy Liver', 'Medium','original'], ['41', 'RF', 'Healthy Liver', 'High','original'], ['41', 'KNN', 'Healthy Liver', 'Low','original'], ['41', 'KNN', 'Healthy Liver', 'Medium'], ['41', 'KNN', 'Healthy Liver', 'High','original'],
['41', 'DTREE', 'Healthy Liver', 'Low','original'], ['41', 'DTREE', 'Healthy Liver', 'Medium','original'], ['41', 'DTREE', 'Healthy Liver', 'High','original'], ['41', 'SVM', 'Healthy Liver', 'Low','original'], ['41', 'SVM', 'Healthy Liver', 'Medium','original'], ['41', 'SVM', 'Healthy Liver', 'High','original'],
['190', 'RF', 'Liver Disease', 'Low','original'], ['190', 'RF', 'Liver Disease', 'Medium','original'], ['190', 'RF', 'Liver Disease', 'High','original'], ['190', 'KNN', 'Liver Disease', 'Low','original'], ['190', 'KNN', 'Liver Disease', 'Medium','original'], ['190', 'KNN', 'Liver Disease', 'High','original'],
['190', 'DTREE', 'Liver Disease','Low','original'], ['190', 'DTREE', 'Liver Disease','Medium','original'], ['190', 'DTREE', 'Liver Disease', 'High','original'], ['190', 'SVM', 'Liver Disease', 'Low','original'], ['190', 'SVM', 'Liver Disease', 'Medium','original'], ['190', 'SVM', 'Liver Disease', 'High','original'],
['555', 'RF', 'Liver Disease', 'Low','original'], ['555', 'RF', 'Liver Disease', 'Medium','original'], ['555', 'RF', 'Liver Disease', 'High','original'], ['555', 'KNN', 'Liver Disease', 'Low','original'], ['555', 'KNN', 'Liver Disease', 'Medium','original'], ['555', 'KNN', 'Liver Disease', 'High','original'],
['555', 'DTREE', 'Liver Disease', 'Low','original'], ['555', 'DTREE', 'Liver Disease', 'Medium','original'], ['555', 'DTREE', 'Liver Disease','High','original'], ['555', 'SVM', 'Liver Disease', 'Low','original'], ['555', 'SVM', 'Liver Disease', 'Medium','original'], ['555', 'SVM', 'Liver Disease', 'High','original'],
['41', 'RF', 'Liver Disease', 'Low','altered'], ['41', 'RF', 'Liver Disease','Medium','altered'], ['41', 'RF', 'Liver Disease', 'High','altered'], ['41', 'KNN', 'Liver Disease', 'Low','altered'], ['41', 'KNN', ' Liver Disease', 'Medium','altered'], ['41', 'KNN', 'Liver Disease', 'High','altered'],
['41', 'DTREE', 'Liver Disease', 'Low','altered'], ['41', 'DTREE', 'Liver Disease', 'Medium','altered'], ['41', 'DTREE', 'Liver Disease', 'High','altered'], ['41', 'SVM', 'Liver Disease', 'Low','altered'], ['41', 'SVM', 'Liver Disease', 'Medium','altered'], ['41', 'SVM', 'Liver Disease' , 'High','altered'],
['190', 'RF', 'Healthy Liver', 'Low','altered'], ['190', 'RF', ' Healthy Liver', 'Medium','altered'], ['190', 'RF', 'Healthy Liver ','High','altered'], ['190', 'KNN', 'Healthy Liver ', 'Low','altered'], ['190', 'KNN', 'Healthy Liver ', 'Medium','altered'], ['190', 'KNN', 'Healthy Liver ', 'High','altered'],
['190', 'DTREE', 'Healthy Liver ', 'Low','altered'], ['190', 'DTREE', 'Healthy Liver ', 'Medium','altered'], ['190', 'DTREE', 'Healthy Liver ', 'High','altered'], ['190', 'SVM', 'Healthy Liver', 'Low','altered'], ['190', 'SVM', 'Healthy Liver ', 'Medium','altered'], ['190', 'SVM', 'Healthy Liver ', 'High','altered'],
['555', 'RF', 'Healthy Liver ', 'Low','altered'], ['555', 'RF', 'Healthy Liver ', 'Medium','altered'], ['555', 'RF', 'Healthy Liver ', 'High','altered'], ['555', 'KNN', 'Healthy Liver ', 'Low','altered'], ['555', 'KNN', 'Healthy Liver ', 'Medium','altered'], ['555', 'KNN', 'Healthy Liver', 'High','altered'],
['555', 'DTREE', 'Healthy Liver', 'Low','altered'], ['555', 'DTREE', 'Healthy Liver', 'Medium','altered'], ['555', 'DTREE', 'Healthy Liver', 'High','altered'], ['555', 'SVM', 'Healthy Liver ', 'Low','altered'], ['555', 'SVM', 'Healthy Liver', 'Medium','altered'], ['555', 'SVM', ' Healthy Liver ', 'High','altered']]
accuracylevel_LD_2_list_original = random.sample(accuracylevel_LD_2_list_origin, len(accuracylevel_LD_2_list_origin))

#number of participants
counter = 12

Unique_id_list =  random.sample(range(110000000, 999999999), counter)

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

def control_HS_1(participant_path):
    #declare hs_list as global variable and check if has any items n pop; else populate the list and then pop
    global control_HS_1_list
    if len(control_HS_1_list) == 0:
        control_HS_1_list = random.sample(control_1_list, len(control_1_list))
        combo_HS_1 = control_HS_1_list.pop(len(control_HS_1_list)-1)

    else:
        combo_HS_1 = control_HS_1_list.pop(len(control_HS_1_list)-1)

    o1 = combo_HS_1[0].lower() + '1.png'
    o2 = combo_HS_1[1].lower() + '1.png'
    question = 'Based on factors like age of patient, year of surgery and number of cancerous nodes, we predict the survival of the patient 5 years after undergoing surgery for cancer. Based on the reference visualization provided below, which option would you choose as a more accurate prediction of survival of cancer patient? '
    Option1_vis = participant_path + "/HS/" + o1
    Option2_vis = participant_path + "/HS/" + o2
    q_hs1_control = {}
    q_hs1_control['page'] = "experiment"
    q_hs1_control['variables'] = {"page_title": "Experimental Task", "currentTask": 1, "totalTasks": 24, "question" : question}
    q_hs1_control['options'] = []
    q_hs1_control["images"] = {"baseline": {"url": participant_path + "/HS/base1.png", "width": "256"},
    "img1": {"url": Option1_vis, "width": "256"},
    "img2": {"url": Option2_vis, "width": "256" } }
    #q_hs1_control['Option1_vis'] = Option1
    #q_hs1_control['Option2_vis'] = Option2
    #q_hs1_control['Reference_vis'] = participant_path + "HS/base1.png"
    q_hs1_control['meta_data'] = {"control_1_HS": combo_HS_1}

    return q_hs1_control

def control_SGC_1(participant_path):
    #declare global variable, check if has any items and then pop, if not populate the list and then pop an item;
    global control_SGC_1_list
    if len(control_SGC_1_list) != 0:
        combo_SGC_1 = control_SGC_1_list.pop(len(control_SGC_1_list) - 1)
    else:
        control_SGC_1_list = random.sample(control_1_list, len(control_1_list))
        combo_SGC_1 = control_SGC_1_list.pop(len(control_SGC_1_list) - 1)

    o1 = combo_SGC_1[0].lower() + "1.png"
    o2 = combo_SGC_1[1].lower() + "1.png"
    question = 'Based on factors such as income, amount of loan, payment of previous cards etc. we are trying to predict the credit risk of a customer for a requested loan. Based on the reference visualization provided below, which option would you choose as a more accurate prediction of a credit risk of customer? '
    Option1_vis = participant_path + "/SGC/" + o1
    Option2_vis = participant_path + "/SGC/" + o2
    q_sgc1_control = {}
    q_sgc1_control["page"] = "experiment"
    q_sgc1_control["variables"] = {"page_title": "Experimental Task", "currentTask": 2, "totalTasks": 24, "question": question}
    q_sgc1_control['options'] = []
    q_sgc1_control['images'] ={"baseline": {"url":participant_path + "/SGC/base1.png", "width": "256" },
    "img1": {"url": Option1_vis, "width": "256"},
    "img2": {"url": Option2_vis, "width": "256"}}
    #q_sgc1_control['Option1_vis'] = Option1
    #q_sgc1_control['Option2_vis'] = Option2
    #q_sgc1_control['Reference_vis'] = participant_path + "SGC/base1.png"
    q_sgc1_control['meta_data'] = {"combo_SGC_1_control": combo_SGC_1}

    return q_sgc1_control

def control_LD_1(participant_path):
    #declare global variable and then check if has items and pop then, if not populate the list and then pop an item;
    global control_LD_1_list
    if len(control_LD_1_list) != 0:
        combo_LD_1 = control_LD_1_list.pop( len(control_LD_1_list) - 1)
    else:
        control_LD_1_list = random.sample(control_1_list, len(control_1_list))
        combo_LD_1 = control_LD_1_list.pop( len(control_LD_1_list) - 1)

    o1 = combo_LD_1[0].lower() + "1.png"
    o2 = combo_LD_1[1].lower() + "1.png"
    question = 'We predict if a patient is suffering from a liver disease based on factors such as age, gender, total amount of protiens etc. Based on the reference visualization provided below, which option would you choose as a more accurate prediction of liver disease in a patient?  '
    Option1_vis = participant_path + "/LD/" + o1
    Option2_vis = participant_path + "/LD/" + o2
    q_ld1_control = {}
    q_ld1_control['page'] = "experiment"
    q_ld1_control['variables'] = {"page_title": "Experimental Task", "currentTask": 3, "totalTasks": 24, "question": question}
    q_ld1_control['options'] = []
    q_ld1_control['images'] = {"baseline": {"url":participant_path + "/LD/base1.png", "width": "256" },
    "img1": {"url": Option1_vis, "width": "256"},
    "img2": {"url": Option2_vis, "width": "256"}}
    #q_ld1_control['Option1_vis'] = Option1
    #q_ld1_control['Option2_vis'] = Option2
    #q_ld1_control['Reference_vis'] = participant_path + "LD/base1.png"
    q_ld1_control['meta_data'] = {"combo_LD_1_control": combo_LD_1 }

    return q_ld1_control

def control_likert_1():
    question = 'How much would you trust a visualization in choosing a model?'
    Option1 = 'Strongly Trust'
    Option2 = 'Trust'
    Option3 = 'Neither Trust nor Distrust'
    Option4 = 'Does not Trust'
    Option5 = 'Strongly does not Trust'
    control_likert_1 = {}
    control_likert_1['page'] = "experiment"
    control_likert_1['variables'] = {"page_title": "Experimental Task", "currentTask": 4, "totalTasks": 24, "question": question}
    control_likert_1['options'] = [Option1, Option2, Option3, Option4, Option5]

    return control_likert_1

def accuracy_HS_1(participant_path):
    global accuracy_HS_1_list
    if len(accuracy_HS_1_list) !=0:
        combo_HS_1 = accuracy_HS_1_list.pop(len(accuracy_HS_1_list) - 1)
    else:
        accuracy_HS_1_list = random.sample(accuracy_1_list, len(accuracy_1_list))
        combo_HS_1 = accuracy_HS_1_list.pop(len(accuracy_HS_1_list) - 1)

    o1 = combo_HS_1[0].lower() + "1.png"
    o2 = combo_HS_1[2].lower() + "1.png"
    question = 'Based on factors like age of patient, year of surgery and number of cancerous nodes, we predict the survival of patient 5 years after undergoing surgery for cancer. Based on visualizations and accuracies provided, which option would you choose as a better prediction of survival in Cancer patients? '
    Option1 = 'Accuracy of prediction is {}%'.format(combo_HS_1[1])
    Option2 = 'Accuracy of prediction is {}%'.format(combo_HS_1[3])
    q_hs1_accu = {}
    q_hs1_accu['page'] = "experiment"
    q_hs1_accu['variables'] = {"page_tite": "Experimental Task", "currentTask": 5, "totalTasks":24, "question": question}
    q_hs1_accu['options'] = [Option1, Option2]
    q_hs1_accu['images'] = {"baseline": {"url": participant_path + "/HS/base1.png", "width": "256"},
    "img1": {"url": participant_path + "/HS/" + o1, "width": "256"},
    "img2": {"url": participant_path + "/HS/" + o2, "width": "256"}}
    #q_hs1_accu['Reference_vis'] = participant_path + "HS/base1.png"
    #q_hs1_accu['Option1_vis'] = participant_path + "HS" + o1
    #q_hs1_accu['Option2_vis'] = participant_path + "HS" + o2
    q_hs1_accu['meta_data'] = {"combo_HS_1_accuracy": combo_HS_1}

    return q_hs1_accu

def accuracy_SGC_1(participant_path):
    global accuracy_SGC_1_list
    if len(accuracy_SGC_1_list) != 0:
        combo_SGC_1 = accuracy_SGC_1_list.pop(len(accuracy_SGC_1_list) -1)
    else:
        accuracy_SGC_1_list = random.sample(acccuracy_1_list, len(accuracy_1_list))
        combo_SGC_1 = accuracy_SGC_1_list.pop(len(accuracy_SGC_1_list) - 1)

    o1 = combo_SGC_1[0].lower() + "1.png"
    o2 = combo_SGC_1[2].lower() + "1.png"
    question = 'Based on factors such as inclome, amount of loan, payment of previous cards etc. we are trying to predict the credit risk of bank customer for a requested loan. Based on the visualizations and accuracies provided, which option would you choose as a better prediction of ccredit risk of customers? '
    Option1 = 'Accuracy of prediction is {}%'.format(combo_SGC_1[1])
    Option2 = 'Accuracy of prediction is {}%'.format(combo_SGC_1[3])
    q_sgc1_accu = {}
    q_sgc1_accu['page'] = "experiment"
    q_sgc1_accu['variables'] = {"page_title": "Experimental Task", "currentTask": 6, "totalTasks": 24, "question": question}
    q_sgc1_accu['options'] = [Option1, Option2]
    q_sgc1_accu['images'] = {"baseline": {"url": participant_path + "/SGC/base1.png" , "width": "256"},
    "img1": {"url": participant_path + "/SGC/" + o1, "width": "256"},
    "img2": {"url": participant_path + "/SGC/" + o2, "width": "256"}}
    #q_sgc1_accu['Reference_vis'] = participant_path + "SGC/base1.png"
    #q_sgc1_accu['Option1_vis'] = participant_path + "SGC" + o1
    #q_sgc1_accu['Option2_vis'] = participant_path + "SGC" + o2
    q_sgc1_accu['meta_data'] = {"combo_SGC_1_accuracy": combo_SGC_1}

    return q_sgc1_accu;

def accuracy_LD_1(participant_path):
    global accuracy_LD_1_list
    if len(accuracy_LD_1_list) != 0:
        combo_LD_1 = accuracy_LD_1_list.pop(len(accuracy_LD_1_list) -1)
    else:
        accuracy_LD_1_list = random.sample(accuracy_1_list, len(accuracy_1_list))
        combo_LD_1 = accuracy_LD_1_list.pop(len(accuracy_LD_1_list) - 1)

    o1 = combo_LD_1[0].lower() + "1.png"
    o2 = combo_LD_1[2].lower() + "1.png"
    question = 'We predict if the patient is suffering from a liver disease based on factors such as age, gender, total amount of protiens etc. Based on visualizations and accuracies provided, which option would you choose as a better prediction of liver disease in patient? '
    Option1 = 'Accuracy of prediction is {}%'.format(combo_LD_1[1])
    Option2 = 'Accuracy of prediction is {}%'.format(combo_LD_1[3])
    q_ld1_accu = {}
    q_ld1_accu['page'] = "experiment"
    q_ld1_accu['variables'] = {"page_title": "Experimental Task", "currentTask": 7, "totalTasks": 24, "question": question}
    q_ld1_accu['options'] = [Option1, Option2]
    q_ld1_accu['images'] = {"baseline": {"url": participant_path + "/LD/base1.png", "width": "256"},
    "img1": {"url": participant_path + "/LD/" + o1, "width": "256"},
    "img2": {"url": participant_path + "/LD/" + o2, "width": "256"}}
    #q_ld1_accu['Reference_vis'] = participant_path + "LD/base1.png"
    #q_ld1_accu['Option1_vis'] = participant_path + "LD" + o1
    #q_ld1_accu['option2_vis'] = participant_path + "LD" + o2
    q_ld1_accu['meta_data'] = {"combo_LD_1_accuracy": combo_LD_1}

    return q_ld1_accu

def accuracy_likert_1():
    question = 'Among visualizations and accuracies, how much would you trust visualizations to choose a model?'
    Option1 = 'Strongly Trust'
    Option2 = 'Trust'
    Option3 = 'Neighter Trust nor Distrust'
    Option4 = 'Does not Trust'
    Option5 = 'Strongly Does not Trust'
    accuracy_likert_1 = {}
    accuracy_likert_1['page'] = "experiment"
    accuracy_likert_1['variables'] = {"page_title": "Experimental Task", "currentTask": 8, "totalTasks": 24, "question": question}
    accuracy_likert_1['options'] = [Option1, Option2, Option3, Option4, Option5]

    return accuracy_likert_1

def accuracylevel_HS_1(participant_path):
    #definne global varibale
    global accuracylevel_HS_1_list
    if len(accuracylevel_HS_1_list) != 0:
        combo_HS_1 = accuracylevel_HS_1_list.pop(len(accuracylevel_HS_1_list) - 1)
    else:
        accuracylevel_HS_1_list = random.sample(accuracylevel_1_list, len(accuracylevel_1_list))
        combo_HS_1 = accuracylevel_HS_1_list.pop(len(accuracylevel_HS_1_list) - 1)

    o1 = combo_HS_1[0].lower() + "1.png"
    o2 = combo_HS_1[2].lower() + "1.png"
    question = 'Based on factors like age of patient, year of surgery, number of cancerous nodes, we predict the survival of patient five years after undergoing surgery for cancer. Based on visualizations and estimation of accuracy levels provided, which option would you choose as a better prediction of survival in cancer patients? '
    Option1 = 'Accuracy of prediction is {}%'.format(combo_HS_1[1])
    Option2 = 'Accuracy of prediction is {}%'.format(combo_HS_1[3])
    q_hs1_alevel = {}
    q_hs1_alevel['page'] = "experiment"
    q_hs1_alevel['variables'] = {"page_title": "Experimental Task", "currentTask": 9, "totalTasks":24, "question": question}
    q_hs1_alevel['options'] = [Option1, Option2]
    q_hs1_alevel['images'] = {"baseline": {"url": participant_path + "/HS/base1.png", "width": "256" },
    "img1": {"url": participant_path + "/HS/" + o1, "width": "256"},
    "img2": {"url": participant_path + "/HS/" + o2, "width": "256"}}
    #q_hs1_alevel['Reference_vis'] = participant_path + "HS/base1.png"
    #q_hs1_alevel['Option1_vis'] = participant_path + "HS" + o1
    #q_hs1_alevel['Option2_vis'] = participant_path + "HS" + o2
    q_hs1_alevel['meta_data'] = {"combo_HS_1_alevel":combo_HS_1}

    return q_hs1_alevel

def accuracylevel_SGC_1(participant_path):
    #define universal liver_variable
    global accuracylevel_SGC_1_list
    if len(accuracylevel_SGC_1_list) != 0:
        combo_SGC_1 = accuracylevel_SGC_1_list.pop(len(accuracylevel_SGC_1_list) - 1)
    else:
        accuracylevel_SGC_1_list = random.sample(accuracylevel_1_list, len(accuracylevel_1_list))
        combo_SGC_1 = accuracylevel_SGC_1_list.pop(len(accuracylevel_SGC_1_list) - 1)

    o1 = combo_SGC_1[0].lower() + "1.png"
    o2 = combo_SGC_1[2].lower() + "1.png"
    question = 'Based on factors such as income, amount of loan, payment of previous cards etc. we are trying to predict the credit risk of customer for a requested loan. Based on visualizations and estimation of accuracy levels provided, which option would you choose as a better prediction of credit risk of customers? '
    Option1 = 'Accuracy of prediction is {}%'.format(combo_SGC_1[1])
    Option2 = 'Accuracy of prediction is {}%'.format(combo_SGC_1[3])
    q_sgc1_alevel = {}
    q_sgc1_alevel['page'] = "experiment"
    q_sgc1_alevel['variables'] = {"page_title": "Experimental Task", "currentTask": 10, "totalTasks": 24, "question": question}
    q_sgc1_alevel['options'] = [Option1, Option2]
    q_sgc1_alevel['images'] = {"baseline": {"url": participant_path + "/SGC/base1.png", "width": "256"},
    "img1": {"url": participant_path + "/SGC/" + o1, "width": "256"},
    "img2": {"url": participant_path + "/SGC/" + o2, "width": "256"}}
    #q_sgc1_alevel['Reference_vis'] = participant_path + "SGC/base1.png"
    #q_sgc1_alevel['Option1_vis'] = participant_path + "SGC" + o1
    #q_sgc1_alevel['Option2_vis'] = participant_path + "SGC" + o2
    q_sgc1_alevel['meta_data'] = {"combo_SGC_1_alevel":combo_SGC_1}

    return q_sgc1_alevel

def accuracylevel_LD_1(participant_path):
    #define global credit_variables
    global accuracylevel_LD_1_list
    if len(accuracylevel_LD_1_list) != 0:
        combo_LD_1 = accuracylevel_LD_1_list.pop(len(accuracylevel_LD_1_list) -1)
    else:
        accuracylevel_LD_1_list = random.sample(accuracylevel_1_list, len(accuracylevel_1_list))
        combo_LD_1 = accuracylevel_LD_1_list.pop(len(accuracylevel_LD_1_list) - 1)

    o1 = combo_LD_1[0].lower() + "1.png"
    o2 = combo_LD_1[2].lower() + "1.png"
    question = 'We predict if the patient is suffering from a liver disease based on factors such as age, gender, total amount of protiens etc. Based on Visualizations and estimation of accuracy levels provided, which option would you choose as a better prediction of liver disease in a patient. '
    Option1 = 'Accuracy of prediction is {}%'.format(combo_LD_1[1])
    Option2 = 'Accuracy of prediction is {}%'.format(combo_LD_1[3])
    q_ld1_alevel = {}
    q_ld1_alevel['page'] = "experiment"
    q_ld1_alevel['variables'] = {"page_title": "Exerimental Task", "currentTask": 11, "totalTasks": 24, "question": question}
    q_ld1_alevel['options'] = [Option1, Option2]
    q_ld1_alevel['images'] = {"baseline": {"url": participant_path + "/LD/base1.png", "width": "256" },
    "img1": {"url": participant_path + "/LD/" + o1, "width": "256"},
    "img2": {"url": participant_path + "/LD/" + o2, "width": "256"}}
    #q_ld1_alevel['Reference_vis'] = participant_path + "LD/base1.png"
    #q_ld1_alevel['Option1_vis'] = participant_path + "LD" + o1
    #q_ld1_alevel['Option2_vis'] = participant_path + "LD" + o2
    q_ld1_alevel['meta_data'] = {"combo_LD_1_alevel":combo_LD_1}

    return q_ld1_alevel

def accuracylevel_likert_1():
    question = 'Among visualizations and level of accuracies, how much would you trust visualizations in choosing a model?'
    Option1 = 'Strongly Trust'
    Option2 = 'Trust'
    Option3 = 'Neither trust nor distrust '
    Option4 = 'Does not Trust'
    Option5 = 'Strongly does not trust'
    accuracylevel_likert_1 = {}
    accuracylevel_likert_1['page'] = "experiment"
    accuracylevel_likert_1['variables'] = {"page_title": "Experimental Task", "currentTask": 12, "totalTasks": 24, "question": question}
    accuracylevel_likert_1['options'] = [Option1, Option2, Option3, Option4, Option5]

    return accuracylevel_likert_1

def control_HS_2( participant_path):
    #define the global variables, if switch is true then original values are choosen for this participant else, they will see the altered ones
    global control_HS_2_list_original

    if len(control_HS_2_list_original) != 0:
        combo_HS_2 = control_HS_2_list_original.pop(len(control_HS_2_list_original) - 1)
    else:
        control_HS_2_list_original = random.sample(control_HS_2_list_origin, len(control_HS_2_list_origin))
        combo_HS_2 = control_HS_2_list_original.pop(len(control_HS_2_list_original) - 1 )

    o1 = combo_HS_2[1].lower() + "_" + combo_HS_2[0]+".png"
    question = 'Based on factors like age of patient, year of surgery and number of cancerous nodes, we predict the survival of patient 5 years after undergoing surgery for cancer. The prediction visualization is shown below and the black point represent the single data point predicted. The algorithm predicted the patient {}% after undergoing surgery. Do you agree with the prediction?'.format(combo_HS_2[2])
    Option1 = 'Yes'
    Option2 = 'No'
    q_hs2_control = {}
    q_hs2_control['page'] = "experiment"
    q_hs2_control['variables'] = {"page_title": "Experimental Task", "currentTask": 13, "totalTasks": 24, "question": question}
    q_hs2_control['options'] = [Option1, Option2]
    q_hs2_control['images'] ={"baseline": {"url": participant_path + "/HS/" + o1, "width": "256"}}
    #q_hs2_control['Reference_vis'] = participant_path + "HS" + o1
    q_hs2_control['meta_data'] = {"combo_HS_2_control":combo_HS_2}

    return q_hs2_control

def control_SGC_2( participant_path):
    #define the global variables, if switch is true choose from original list, else choose from altered list

    global control_SGC_2_list_original

    if len(control_SGC_2_list_original) != 0:
        combo_SGC_2 = control_SGC_2_list_original.pop(len(control_SGC_2_list_original) - 1)
    else:
        control_SGC_2_list_original = random.sample(control_SGC_2_list_origin, len(control_SGC_2_list_origin))
        combo_SGC_2 = control_SGC_2_list_original.pop(len(control_SGC_2_list_original) - 1)

    o1 = combo_SGC_2[1].lower() + "_" + combo_SGC_2[0] + ".png"
    question = 'Based on factors like income, amount of loan, payment of previous cards etc. we are trying to predict the credit risk of a bank customer for a requested loan. The predicted visualization is shown below and the black point represents single data prediction. The algorithm predicted the customer has {}%. Do you agree with the prediction?'.format(combo_SGC_2[2])
    Option1 = 'Yes'
    Option2 = 'No'
    q_sgc2_control = {}
    q_sgc2_control['page'] = "experiment"
    q_sgc2_control['variables'] = {"page_title": "Experimental Task", "currentTask": 14, "totalTasks": 24, "question": question}
    q_sgc2_control['options'] = [Option1, Option2]
    q_sgc2_control['images'] = {"baseline": {"url": participant_path + "/SGC/" + o1, "width": "256"}}
    #q_sgc2_control['Reference_vis'] = participant_path + "SGC" + o1
    q_sgc2_control['meta_data'] = {"combo_SGC_2_control":combo_SGC_2}
    #even though it says referencdec vis, we will be showing predicted visualization

    return q_sgc2_control

def control_LD_2( participant_path):
    global control_LD_2_list_original
    #define global variables, if the switch is true use the original list and if not use the altered lists

    if len(control_LD_2_list_original) != 0:
        combo_LD_2 = control_LD_2_list_original.pop(len(control_LD_2_list_original) - 1)
    else:
        control_LD_2_list_original = random.sample(control_LD_2_list_origin, len(control_LD_2_list_origin))
        combo_LD_2 = control_LD_2_list_original.pop(len(control_LD_2_list_original) - 1)

    o1 = combo_LD_2[1].lower() + "_" + combo_LD_2[0] + ".png"
    question = 'We predict if the patient is suffering from a liver disease based on factors like age, gender, total amount of protiens etc. The predicted visualization is below and the black point represents the single data point predicted. The algorithm predicts the patient has {}%. Do you agree with the prediction?'.format(combo_LD_2[2])
    Option1 = 'No'
    Option2 = 'Yes'
    q_ld2_control = {}
    q_ld2_control['page'] = "experiment"
    q_ld2_control['variables'] = {"page_title": "Experimental Task", "currentTask": 15, "totalTasks": 24, "question": question}
    q_ld2_control['options'] = [Option1, Option2]
    q_ld2_control['images'] = {"baseline": {"url": participant_path + "/LD/" + o1, "width": "256"}}
    #q_ld2_control['Reference_vis'] = participant_path + "LD" + o1
    q_ld2_control['meta_data'] = {"combo_LD_2_control":combo_LD_2}
    #eventhough we say reference visualization, we provide predicted visualization
    return q_ld2_control

def control_likert_2():
    question = 'How much does visualizations help in trusting the prediction? '
    Option1 = 'Strongly Trust'
    Option2 = 'Trust'
    Option3 = 'Neither Trust nor distrust'
    Option4 = 'Does not Trust'
    Option5 = 'Strongly does not trust'
    control_likert_2 = {}
    control_likert_2['page'] = "experiment"
    control_likert_2['variables'] = {"page_title": "Experimental Task", "currentTask": 16, "totalTasks": 24, "question": question}
    control_likert_2['options'] = [Option1, Option2, Option3, Option4, Option5]

    return control_likert_2

def accuracy_HS_2( participant_class_type, participant_path):
    #define the global variables
    global accuracy_HS_2_list_original

    if len(accuracy_HS_2_list_original) != 0:
        combo_HS_2 = accuracy_HS_2_list_original.pop(len(accuracy_HS_2_list_original) - 1)
    else:
        accuracy_HS_2_list_original = random.sample(accuracy_HS_2_list_origin, len(accuracy_HS_2_list_origin))
        combo_HS_2 = accuracy_HS_2_list_original.pop(len(accuracy_HS_2_list_original) - 1)


    o1 = combo_HS_2[1].lower() + "_" + combo_HS_2[0] + ".png"
    q_hs2_accu = {}
    q_hs2_accu['page'] = "experiment"
    q_hs2_accu['meta_data'] = {"combo_HS_2_accu":combo_HS_2}
    if participant_class_type == 'Both':
        question_part1 = 'Based on factors like age of the patient, year of surgery and number of cancerous nodes etc, we predict the survival of patient 5 years after undergoing surgery for cancer. The predicted visualization is shown and black point represents the single data point predicted. The algorithm predicted the patient {}% 5 years after undergoing the surgery. The accuracy of the model is {}% %. That means the model made {}% correct predictions out of 100. Do you trust the prediction is correct? '.format(combo_HS_2[2], combo_HS_2[3], combo_HS_2[3])
        Option1 = 'Yes'
        Option2 = 'No'
        q_hs2_accu['options'] = [Option1, Option2]
        q_hs2_accu['images'] = {"baseline": {"url": participant_path + "/HS/" + o1, "width": "256"}}
        q_hs2_accu['variables'] = {"page_title": "Experimental Task", "currentTask": 17, "totalTasks": 24, "question": question_part1}
        #q_hs2_accu['Reference_vis_part1'] = participant_path + "HS" + o1
    if participant_class_type == 'Visualization':
        question_part1 = 'Based on factors like age of the patient, year of surgery and number of cancerous nodes etc, we predict the survival of patient 5 years after undergoing surgery for cancer. The predicted visualization is shown and the black point represents the single data point predicted. The algorithm predicted the patient {}% 5 years after undergoing the surgery. Do you trust the prediction is correct?  '.format(combo_HS_2[2])
        Option1_part1 = 'Yes'
        Option2_part1 = 'No'
        question_part2 = 'The accuracy of the model is {}% %. That means the model made {}% correct predictions out of 100. Do you still trust the prediction? '.format(combo_HS_2[3], combo_HS_2[3])
        Option1_part2 = 'Yes'
        Option2_part2 = 'No'
        q_hs2_accu['options'] = [Option1_part1, Option2_part1]
        q_hs2_accu['options_part2'] = [Option1_part2, Option2_part2]
        q_hs2_accu['images'] = {"baseline": {"url": participant_path + "/HS/" + o1, "width": "256"}}
        q_hs2_accu['variables'] = {"page_title": "Experimental Task", "currentTask": 17, "totalTasks": 24, "question": question_part1, "question2": question_part2}
        #q_hs2_accu['Reference_vis_part1'] = participant_path + "HS" + o1
    if participant_class_type == 'Accuracy':
        question_part1 = 'Based on factors like age of the patient, year of surgery and number of cancerous nodes etc, we predict the survival of patient 5 years after undergoing surgery for cancer. The algorithm predicted the patient {}% 5 years after undergoing surgery. The accuracy of the model is {}% %. That means the model made {}% correct predictions out of 100. Do you trust the prediction is correct? '.format(combo_HS_2[2], combo_HS_2[3], combo_HS_2[3])
        Option1_part1 = 'Yes'
        Option2_part1 ='No'
        question_part2 = 'The predicted visualization is now shown and the black point represents the single data point predicted. After looking at the visualization, do you trust the prediction is correct?'
        Option1_part2 = 'Yes'
        Option2_part2 = 'No'
        q_hs2_accu['options'] = [Option1_part1, Option2_part1]
        q_hs2_accu['options_part2'] = [Option1_part2, Option2_part2]
        q_hs2_accu['images'] = {"baseline_part2": {"url": participant_path + "/HS/" + o1, "width": "256"}}
        q_hs2_accu['variables'] = {"page_title": "Experimental Task", "currentTask": 17, "totalTasks": 24, "question": question_part1, "question2": question_part2}
        #q_hs2_accu['Reference_vis_part2'] = participant_path + "HS" + o1


    return q_hs2_accu

def accuracy_SGC_2( participant_class_type, participant_path):
    #define the global variables
    global accuracy_SGC_2_list_original

    if len(accuracy_SGC_2_list_original) != 0:
        combo_SGC_2 = accuracy_SGC_2_list_original.pop(len(accuracy_SGC_2_list_original) - 1)
    else:
        accuracy_SGC_2_list_original = random.sample(accuracy_SGC_2_list_origin, len(accuracy_SGC_2_list_origin))
        combo_SGC_2 = accuracy_SGC_2_list_original.pop(len(accuracy_SGC_2_list_original) - 1)

    o1 = combo_SGC_2[1].lower() + "_" + combo_SGC_2[0] + ".png"
    q_sgc2_accu = {}
    q_sgc2_accu['page'] = "experiment"
    q_sgc2_accu['meta_data'] = {"combo_SGC_2_accu": combo_SGC_2}
    if participant_class_type == 'Both':
        question_part1 = 'Based on factors such as income, age, amount of loan, previous payments etc, we are trying to predict the credit risk of a bank customer for a requested loan. The predicted visualization is shown and the black point represents the single data point to be predicted. The algorithm predicted the customer has {}% . The accuracy of the model is {}% %. That means the model made {}% correct predictions out of 100. Do you trust the prediction is correct? '.format(combo_SGC_2[2], combo_SGC_2[3], combo_SGC_2[3])
        Option1_part1 = 'Yes'
        Option2_part1 = 'No'
        q_sgc2_accu['options'] = [Option1_part1, Option2_part1]
        q_sgc2_accu['images'] = {"baseline": {"url": participant_path + "/SGC/" + o1, "width": "256"}}
        q_sgc2_accu['variables'] = {"page_title": "Experimental Task", "currentTask": 18, "totalTasks": 24, "question": question_part1 }
        #q_sgc2_accu['Reference_vis_part1'] = participant_path + "SGC" + o1
    if participant_class_type == 'Visualization':
        question_part1 = 'Based on factors such as income, age, amount of loan, previous payments etc, we are trying to predict the credit risk of a bank customer for a requested loan. The predicted visualization is shown and the black point represents the single data point to be predicted. The algorithm predicted the customer has {}%. Do you trust the prediction is correct? '.format(combo_SGC_2[2])
        Option1_part1 = 'Yes'
        Option2_part1 = 'No'
        question_part2 = 'The accuracy of the model is {}% %. That means the model made {}% correct predictions out of 100. Now after looking at the accuracy, do you trust the prediction is correct?'.format(combo_SGC_2[3], combo_SGC_2[3])
        Option1_part2 = 'Yes'
        Option2_part2 = 'No'
        q_sgc2_accu['options'] = [Option1_part1, Option2_part1]
        q_sgc2_accu['options_part2'] = [Option1_part2, Option2_part2]
        q_sgc2_accu['images'] = {"baseline": {"url": participant_path + "/SGC/" + o1, "width": "256"}}
        q_sgc2_accu['variables'] = {"page_title": "Experimental Task", "currentTask": 18, "totalTasks": 24, "question": question_part1, "question2": question_part2}
        #q_sgc2_accu['Reference_vis_part1'] = participant_path + "SGC" + o1
    if participant_class_type == 'Accuracy':
        question_part1 = 'Based on factors such as income, age, amount of loan, previous payments etc, we are trying to predict the credit risk of a bank customer for a requested loan. The algorithm predicted the customer has {}% . The accuracy of the model is {}% %. That means the model made {}% correct predictions out of 100. Do you trust the prediction is correct? '.format(combo_SGC_2[2], combo_SGC_2[3], combo_SGC_2[3])
        Option1_part1 = 'Yes'
        Option2_part1 = 'No'
        question_part2 = 'The predicted visualization is shown and the black point represents the single data point to be predicted. After looking at the visualization, do you trust the prediction is correct? '
        Option1_part2 = 'Yes'
        Option2_part2 = 'No'
        q_sgc2_accu['options'] = [Option1_part1, Option2_part1]
        q_sgc2_accu['options_part2'] = [Option1_part2, Option2_part2]
        q_sgc2_accu['images'] = {"baseline_part2": {"url": participant_path + "/SGC/" + o1, "width": "256"}}
        q_sgc2_accu['variables'] = {"page_title": "Experimental Task", "currentTask": 18, "totalTasks": 24, "question": question_part1, "question2": question_part2}
        #q_sgc2_accu['Reference_vis_part2'] = participant_path + "SGC" + o1

    return q_sgc2_accu

def accuracy_LD_2( participant_class_type, participant_path):
    #define global variables
    global accuracy_LD_2_list_original

    if len(accuracy_LD_2_list_original) != 0:
        combo_LD_2 = accuracy_LD_2_list_original.pop(len(accuracy_LD_2_list_original) - 1)
    else:
        accuracy_LD_2_list_original = random.sample(accuracy_LD_2_list_origin, len(accuracy_LD_2_list_origin))
        combo_LD_2 = accuracy_LD_2_list_original.pop( len(accuracy_LD_2_list_original) - 1)

    o1 = combo_LD_2[1].lower() + "_" + combo_LD_2[0] + ".png"
    q_ld2_accu = {}
    q_ld2_accu['page'] = "experiment"
    q_ld2_accu['meta_data'] = {"combo_LD_2_accu":combo_LD_2}
    if participant_class_type == 'Both':
        question_part1 = 'We predict if the patient is suffering from a liver disease or not, based on factors like age, gender, total amount of proteins etc. The predicted visualization is shown and the black point represents the single data point to be predicted. The algorithm predicted the patient has {}% . The accuracy of the model is {}% %. That means the model made {}% correct predictions out of 100. Do you trust the prediction is correct ?'.format(combo_LD_2[2], combo_LD_2[3], combo_LD_2[3])
        Option1_part1 = 'Yes'
        Option2_part1 = 'No'
        q_ld2_accu['options'] = [Option1_part1, Option2_part1]
        q_ld2_accu['images'] = {"baseline": {"url": participant_path + "/LD/" + o1, "width": "256"}}
        q_ld2_accu['variables'] = {"page_title": "Experimental Task", "currentTask": 19, "totalTasks": 24, "question": question_part1}
        #q_ld2_accu['Reference_vis_part1'] = participant_path + "LD" + o1
    if participant_class_type == 'Visualization':
        question_part1 = 'We predict if the patient is suffering from a liver disease or not, based on factors like age, gender, total amount of proteins etc. The predicted visualization is shown and the black point represents the single data point to be predicted. The algorithm predicted the patient has {}% . Do you trust the prediction is correct? '.format(combo_LD_2[2])
        Option1_part1 = 'Yes'
        Option2_part1 = 'No'
        question_part2 = 'The accuracy of the model is {}% %. That means the model made {}% correct predictions out of 100. Now after looking at the accuracy, do you trust the prediction is correct ? '.format(combo_LD_2[3], combo_LD_2[3])
        Option1_part2 = 'Yes'
        Option2_part2 = 'No'
        q_ld2_accu['options'] = [Option1_part1, Option2_part1]
        q_ld2_accu['options_part2'] = [Option1_part2, Option2_part2]
        q_ld2_accu['images'] = {"baseline": {"url": participant_path + "/LD/" + o1, "width": "256"}}
        q_ld2_accu['variables'] = {"page_title": "Experimental Task", "currentTask": 19, "totalTasks": 24, "question": question_part1, "question2": question_part2}
        #q_ld2_accu['Reference_vis_part1'] = participant_path + "LD" + o1
    if participant_class_type == 'Accuracy':
        question_part1 = 'We predict if the patient is suffering from a liver disease or not, based on factors like age, gender, total amount of proteins etc. The model predicted that a patient has {}% . The accuracy of the model is {}% %. That means the model made {}% correct predictions out of 100. Do you trust the prediction is correct? '.format(combo_LD_2[2], combo_LD_2[3], combo_LD_2[3])
        Option1_part1 = 'Yes'
        Option2_part1 = 'No'
        question_part2 = 'The predicted visualization is shown and the black point represents the data point to be predicted. After looking at the visualization do you trust the prediction is correct? '
        Option1_part2 = 'Yes'
        Option2_part2 = 'No'
        q_ld2_accu['options'] = [Option1_part1, Option2_part1]
        q_ld2_accu['options_part2'] = [Option1_part2, Option2_part2]
        q_ld2_accu['images'] = {"baseline_part2": {"url": participant_path + "/LD/" + o1, "width": "256"}}
        q_ld2_accu['variables'] = {"page_title": "Experimental Task", "currentTask": 19, "totalTasks": 24, "question": question_part1, "question2": question_part2}
        #q_ld2_accu['Reference_vis_part2'] = participant_path + "LD" + o1

    return q_ld2_accu

def accuracy_likert_2():
    question = 'Among visualization and accuracies, how much would you depend on visualizations to trust the model prediction?'
    Option1 = 'Strongly Trust'
    Option2 = 'Trust'
    Option3 = 'Neither Trust nor Distrust'
    Option4 = 'Does not Trust'
    Option5 = 'Strongly does not trust'
    accuracy_likert_2 = {}
    accuracy_likert_2['page'] = "experiment"
    accuracy_likert_2['variables'] = {"page_title": "Experimental Task", "currentTask": 20, "totalTasks": 24, "question": question}
    accuracy_likert_2['options'] = [Option1, Option2, Option3, Option4, Option5]

    return accuracy_likert_2

def accuracylevel_HS_2( participant_class_type, participant_path):
    #golbal variable definition
    global accuracylevel_HS_2_list_original

    if len(accuracylevel_HS_2_list_original) != 0:
        combo_HS_2 = accuracylevel_HS_2_list_original.pop(len(accuracylevel_HS_2_list_original) - 1)
    else:
        accuracylevel_HS_2_list_original = random.sample(accuracylevel_HS_2_list_origin, len(accuracylevel_HS_2_list_origin))
        combo_HS_2 = accuracylevel_HS_2_list_original.pop(len(accuracylevel_HS_2_list_original) - 1)

    o1 = combo_HS_2[1].lower() + "_" + combo_HS_2[0] + ".png"
    q_hs2_alevel = {}
    q_hs2_alevel['page'] = "experiment"
    q_hs2_alevel['meta_data'] = {"combo_HS_2_alevel":combo_HS_2}
    if participant_class_type == 'Both':
        question_part1 = 'Based on factors like age of patient, year of surgery, number of cancerous nodes, etc, we predict the survival of patient 5 years after undergoing surgery for cancer. The predicted visualization is shown and the black point represents the single data point to be predicted. The algorithm predicted the patient {}% 5 years after undergoing surgery. The accuracy level of the model is {}% . Do you trust the prediction is correct? '.format(combo_HS_2[2], combo_HS_2[3])
        Option1_part1 = 'Yes'
        Option2_part1 = 'No'
        q_hs2_alevel['options'] = [Option1_part1, Option2_part1]
        q_hs2_alevel['images'] = {"baseline": {"url": participant_path + "/HS/" + o1, "width": "256"}}
        q_hs2_alevel['variables'] = {"page_title": "Experimental Task", "currentTask": 21, "totalTasks": 24, "question": question_part1}
        #q_hs2_alevel['Reference_vis_part1'] = participant_path + "HS" + o1
    if participant_class_type == 'Visualization':
        question_part1 = 'Based on factors like age of patient, year of surgery, number of cancerous nodes etc, we predict the survival of the patient 5 years after undergoing surgery for cancer. The predicted visualization is showwn and the black point represents the single data point to be predicted. The algorithm predicted the patient {}% 5 years after undergoing surgery. Do you trust the prediction is correct? '.format(combo_HS_2[2])
        Option1_part1 = 'Yes'
        Option2_part1 = 'No'
        question_part2 = 'The accuracy level of the model is {}% . After looking at the accuracy level, do you trust the prediction is correct? '.format(combo_HS_2[3])
        Option1_part2 = 'Yes'
        Option2_part2 = 'No'
        q_hs2_alevel['options'] = [Option1_part1, Option2_part1]
        q_hs2_alevel['options_part2'] = [Option1_part2, Option2_part2]
        q_hs2_alevel['images'] = {"baseline": {"url": participant_path + "/HS/" + o1, "width": "256"}}
        q_hs2_alevel['variables'] = {"page_title": "Experimental Task", "currentTask": 21, "totalTasks": 24, "question":question_part1, "question2": question_part2}
        #q_hs2_alevel['Reference_vis_part1'] = participant_path + "HS" + o1
    if participant_class_type == 'Accuracy':
        question_part1 = 'Based on factors like age of patient, year of surgery, number of cancerous nodes etc, we predict the survival of patient 5 years after undergoing surgery for cancer. The algorithm predicted the patient {}% 5 years after under going surgery. The accuracy level of the model is {}%.'.format(combo_HS_2[2], combo_HS_2[3])
        Option1_part1 = 'Yes'
        Option2_part1 = 'No'
        question_part2 = 'The predicted visualization is shown and the black point represents the single data point to be predicted. After looking at the visualization, do you trust the prediction is correct? '
        Option1_part2 = 'Yes'
        Option2_part2 = 'No'
        q_hs2_alevel['options'] = [Option1_part1, Option2_part1]
        q_hs2_alevel['options_part2'] = [Option1_part2, Option2_part2]
        q_hs2_alevel['images'] = {"baseline_part2": {"url": participant_path + "/HS/" + o1, "width": "256"}}
        q_hs2_alevel['variables'] = {"page_title": "Experimental Task", "currentTask": 21, "totalTasks": 24, "question": question_part1, "question2": question_part2}
        #q_hs2_alevel['Reference_vis_part2'] = participant_path + "HS" + o1

    return q_hs2_alevel

def accuracylevel_SGC_2( participant_class_type, participant_path):
    #define global credit_variables
    global accuracylevel_SGC_2_list_original

    if len(accuracylevel_SGC_2_list_original) != 0:
        combo_SGC_2 = accuracylevel_SGC_2_list_original.pop(len(accuracylevel_SGC_2_list_original) - 1)
    else:
        accuracylevel_SGC_2_list_original = random.sample(accuracylevel_SGC_2_list_origin, len(accuracylevel_SGC_2_list_origin))
        combo_SGC_2 = accuracylevel_SGC_2_list_original.pop(len(accuracylevel_SGC_2_list_original) - 1)

    o1 = combo_SGC_2[1].lower() + "_" + combo_SGC_2[0] + ".png"
    q_sgc2_alevel = {}
    q_sgc2_alevel['page'] = "experiment"
    q_sgc2_alevel['meta_data'] = {"combo_SGC_2_alevel":combo_SGC_2}
    if participant_class_type == 'Both':
        question_part1 = 'Based on factors such as income, age, amount of loan, payment of previous cards etc, we are trying to predict the credit risk of a bank customer. The predicted visualization is shown and the black point represents the single data point to be predicted. The algorithm predicted the customer has {}% . The accuracye level of the model is {}%. Do you trust the prediction is correct? '.format(combo_SGC_2[2], combo_SGC_2[3])
        Option1_part1 = 'Yes'
        Option2_part1 = 'No'
        q_sgc2_alevel = {}
        q_sgc2_alevel['options'] = ['Yes', 'No']
        q_sgc2_alevel['images'] = {"baseline": {"url": participant_path + "/SGC/" + o1, "width": "256"}}
        q_sgc2_alevel['variables'] = {"page_title": "Experimental Task", "currentTask": 22, "totalTasks": 24, "question": question_part1}
        #q_sgc2_alevel['Reference_vis_part1'] = participant_path + "SGC" + o1
    if participant_class_type == 'Visualization':
        question_part1 = 'Based on factors such as income, age, amount of loan, payment of previous cards etc, we are trying to predict the credit risk of a bank customer. The predicted visualization is shown and black point represents the single data point to be predicted. The algorithm predicted the customer has {}% . Do you trust the prediction is correct? '.format(combo_SGC_2[2])
        Option1_part1 = 'Yes'
        Option2_part1 = 'No'
        question_part2 = 'The accuracy level of the model is {}% . After looking at the accuracy level, do you trust the prediction is correct? '.format(combo_SGC_2[3])
        Option1_part2 = 'Yes'
        Option2_part2 = 'No'
        q_sgc2_alevel['options'] = ["Yes", "No"]
        q_sgc2_alevel['options_part2'] = ["Yes", "No"]
        q_sgc2_alevel['images'] = {"baseline": {"url": participant_path + "/SGC/" + o1, "width": "256"}}
        q_sgc2_alevel['variables'] = {"page_title": "Experimental Task", "currentTask": 22, "totalTasks": 24, "question": question_part1, "question2": question_part2}
        #q_sgc2_alevel['Reference_vis_part1'] = participant_path + "SGC" + o1
    if participant_class_type == 'Accuracy':
        question_part1 = 'Based on factors such as income, age, amount of loan, payment of previous cards etc, we are trying to predict the credit risk of a bank customer. The algorithm predicted the customer has {}% . The accuracy level of the model is {}% . Do you trust the prediction is correct? '.format(combo_SGC_2[2], combo_SGC_2[3])
        Option1_part1 = 'Yes'
        Option2_part1 = 'No'
        question_part2 = 'The predicted visualization is shown and the black point represents the single data point to be predicted. After looking at the visualization, do you trust the prediction is correct? '
        Option1_part2 = 'Yes'
        Option2_part2 = 'No'
        q_sgc2_alevel['options'] = ['Yes', 'No']
        q_sgc2_alevel['options_part2'] = ['yes','No']
        q_sgc2_alevel['images'] = {"baseline_part2": {"url": participant_path + "/SGC/" + o1, "width": "256"}}
        q_sgc2_alevel['variables'] = {"page_title": "Experimental Task", "currentTask": 22, "totalTasks": 24, "question": question_part1, "question2": question_part2}
        #q_sgc2_alevel['Reference_vis_part2'] = participant_path + "SGC" + o1

    return q_sgc2_alevel

def accuracylevel_LD_2( participant_class_type, participant_path):
    #define global variables
    global accuracylevel_LD_2_list_original

    if len(accuracylevel_LD_2_list_original) != 0:
        combo_LD_2 = accuracylevel_LD_2_list_original.pop( len(accuracylevel_LD_2_list_original) - 1)
    else:
        accuracylevel_LD_2_list_original = random.sample(accuracylevel_LD_2_list_origin, len(accuracylevel_LD_2_list_origin))
        combo_LD_2 = accuracylevel_LD_2_list_original.pop( len(accuracylevel_LD_2_list_original) - 1)

    o1 = combo_LD_2[1].lower() + "_" + combo_LD_2[0] + ".png"
    q_ld2_alevel = {}
    q_ld2_alevel['page'] = 'experiment'
    q_ld2_alevel['meta_data'] = {"combo_LD_2_alevel":combo_LD_2}
    if participant_class_type == 'Both':
        question_part1 = 'We predict if the patient is suffering from a liver disease based on factors such as gender, age, total amount of proteins etc. The predicted visualization is shown and the black point represents the single data point to be predicted. The algorithm predicted the patient has {}% . The accuracy level of the model is {}% . Do you trust the prediction is correct? '.format(combo_LD_2[2], combo_LD_2[3])
        Option1_part1 = 'Yes'
        Option2_part1 = 'No'
        q_ld2_alevel['options'] = ['Yes', 'No']
        q_ld2_alevel['images'] = {"baseline": {"url": participant_path + "/LD/" + o1, "width": "256"}}
        q_ld2_alevel['variables'] = {'page_title': "Experimental Task", "currentTask": 23, "totalTasks":24, "question": question_part1}
        #q_ld2_alevel['Reference_vis_part1'] = participant_path + "LD" + o1
    if participant_class_type == 'Visualization':
        question_part1 = 'We predict if the patient is suffering from a liver disease based on factors such as gender, age, total amount of proteins etc. The predicted visualization is shown, and the black point represents the single data point to be predicted. The algorithm predicted the patient has {}% . Do you trust the prediction is correct? '.format(combo_LD_2[2])
        Option1_part1 = 'Yes'
        Option2_part1 = 'No'
        question_part2 = 'The accuracy level of model is {}% . After looking at the accyracy level do you trust the prediction is correct? '.format(combo_LD_2[3])
        Option1_part2 = 'Yes'
        Option2_part2 = 'No'
        q_ld2_alevel['options'] = ['Yes', 'No']
        q_ld2_alevel['options_part2'] = ['Yes', 'No']
        q_ld2_alevel['images'] = {"baseline": {"url": participant_path + "/LD/" + o1, "width": "256"}}
        q_ld2_alevel['variables'] = {'page_title': "Experimental Task", "currentTask": 23, "totalTasks": 24, "question": question_part1, "question2": question_part2}
        #q_ld2_alevel['Reference_vis_part1'] = participant_path + "LD" + o1
    if participant_class_type == 'Accuracy':
        question_part1 = 'We predict if the patient is suffering from a liver disease based on factors such as gender, age, total amount of proteins etc. The algorithm predicted the patient has {}% . The accuracy level of the model is {}% . Do you trust the prediction is correct? '.format(combo_LD_2[2], combo_LD_2[3])
        Option1_part1 = 'Yes'
        Option2_part1 = 'No'
        question_part2 = 'The predicted visualization is shown and the black point represents the single data point to be predicted. After looking at the visualization, do you trust the prediction is correct? '
        Option1_part2 = 'Yes'
        Option2_part2 = 'No'
        q_ld2_alevel['options'] = [Option1_part1, Option2_part1]
        q_ld2_alevel['options_part2'] = [Option1_part2, Option2_part2]
        q_ld2_alevel['images'] = {"baseline_part2": {"url": participant_path + "/LD/" + o1, "width": "256"}}
        q_ld2_alevel['variables'] = {'page_title': "Experimental Task", "currentTask": 23, "totalTasks": 24, "question": question_part1, "question2": question_part2}
        #q_ld2_alevel['Reference_vis_part2'] = participant_path + "LD" + o1

    return q_ld2_alevel

def accuracylevel_likert_2():
    question = 'Among visualizations and level of accuracies, how much would you depend on visualizations to trust the model prediction?'
    Option1 = 'Strongly Trust'
    Option2 = 'Trust'
    Option3 = 'Neither Trust nor distrust'
    Option4 = 'Does not Trust'
    Option5 = 'Strongly does not Trust'
    accuracylevel_likert_2 = {}
    accuracylevel_likert_2['page'] = "experiment"
    accuracylevel_likert_2['variables'] = {"page_title": "Experimental Task", "currentTask": 24, "totalTasks": 24, "question": question}
    accuracylevel_likert_2['options'] = [Option1, Option2, Option3, Option4, Option5]

    return accuracylevel_likert_2

def prequestions_setup(unique_id_list, counter):
    survey = {}
    survey['title'] = 'Periodic Temporal Data Visualization User Evaluation'
    survey['subject_id'] = 'subject{:04d}'.format(counter)
    survey['completion_code'] = unique_id_list.pop(0)

    survey['Consent'] = {'Option1': 'I am freely consenting to take part in the survey and by that I am agreeing that I am 18 years or older',
                         'Option2': 'I do not consent and wish to exit'}

    return survey

#def unique_id_generator():
#    unique_id_list =  random.sample(range(110000000, 999999999), counter)
#    return unique_id_list



def questions_generator(unique_id_list, counter):
    #select a class or bucket for type 2 questions; jumbled_colors and universal path to vis
    global universal_vis_path
    global jumbled_colors
    global class_type2
    if len(class_type2) != 0:
        participant_class_type = class_type2.pop(len(class_type2) - 1)
    else:
        class_type2 = random.sample(class_t2, len(class_t2))
        participant_class_type = class_type2.pop(len(class_type2) - 1)

    #select a random color set for this participant
    if len(jumbled_colors) != 0:
        participant_color = jumbled_colors.pop(len(jumbled_colors) - 1)
    else:
        jumbled_colors = random.sample(colors, len(colors))
        participant_color = jumbled_colors.pop(len(jumbled_colors) - 1)

    #Once participant color is chosen, set the participant path, which will the same path to look for visualizatons for that participant
    participant_path = universal_vis_path + "/" +participant_color
    #print(participant_path)

    survey_setup = prequestions_setup(unique_id_list, counter)

    ########introduction page_title
    intro_page = {}
    intro_page["page"]= "introduction"
    intro_page["variables"] = {"page_title": "Welcome!"}

    ############tutorial page
    tutorial_page = {}
    tutorial_page["page"] = "tutorial"
    tutorial_page["variables"] = {"page_title": "Tutorial"}

    #############tutorial page 2
    tutorial_page2 = {}
    tutorial_page2["page"] = "tutorial2"
    tutorial_page2["variables"] = {"page_title": "Tutorial"}


    tasks = []

    tasks.append(intro_page)
    tasks.append(demographic_questions())
    tasks.append(tutorial_page)
    tasks.append(tutorial_page2)

    #tasks.append(demographic_questions())

    tasks.append(control_HS_1(participant_path))
    tasks.append(control_SGC_1(participant_path))
    tasks.append(control_LD_1(participant_path))

    tasks.append(control_likert_1())

    tasks.append(accuracy_HS_1(participant_path))
    tasks.append(accuracy_SGC_1(participant_path))
    tasks.append(accuracy_LD_1(participant_path))

    tasks.append(accuracy_likert_1())

    tasks.append(accuracylevel_HS_1(participant_path))
    tasks.append(accuracylevel_SGC_1(participant_path))
    tasks.append(accuracylevel_LD_1(participant_path))

    tasks.append(accuracylevel_likert_1())

    tasks.append(control_HS_2( participant_path))
    tasks.append(control_SGC_2( participant_path))
    tasks.append(control_LD_2( participant_path))

    tasks.append(control_likert_2())

    tasks.append(accuracy_HS_2( participant_class_type, participant_path))
    tasks.append(accuracy_SGC_2( participant_class_type, participant_path))
    tasks.append(accuracy_LD_2( participant_class_type, participant_path))

    tasks.append(accuracy_likert_2())

    tasks.append(accuracylevel_HS_2( participant_class_type, participant_path))
    tasks.append(accuracylevel_SGC_2( participant_class_type, participant_path))
    tasks.append(accuracylevel_LD_2( participant_class_type, participant_path))

    tasks.append(accuracylevel_likert_2())


    ###########completion pages
    complete_page = {}
    complete_page['page'] = "complete"
    complete_page['variables'] = {"page_title": "Thank you!", "completionCode": survey_setup['completion_code']}

    tasks.append(complete_page)


    survey_setup['tasks'] = tasks
    survey_setup['participant_color'] = participant_color
    #survey_setup['switch'] = switch
    survey_setup['question2_class_type'] = participant_class_type

    #flip the switch for type 2 ; if this participant got all true predictions for type 2 questions then by flipping this switch , the next participant will get all false predictions

    return survey_setup

counter = counter
while counter > 0:

    q = questions_generator(unique_id_list=Unique_id_list, counter =counter)

    #Serializing json object
    #json_object = json.dumps(q, ensure_ascii=False, indent = 4)

    #Writing to json file
    with open('experiment/subjects/subject{:04d}.json'.format(counter), 'w' ) as outfile:
        json.dump(q, outfile, indent = 4, ensure_ascii=False)
        #json.dumps(json_object)

    counter = counter-1
