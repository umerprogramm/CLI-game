
import json

print('\t\t\t\tWellcome to my game😊\t\t\t\t\t')

with open('data.json') as json_file:
    data = json.load(json_file)
    print(data['ques_1']['explanation'])
    print(data["ques_1"]["option_1"])
    print(data["ques_1"]["option_2"])
    print(data["ques_1"]["option_3"])
    inp = input('eneter the correct option')
    if inp =="2" or inp== "3":
        print('you lose the game 😪')
    
    elif inp=="1":
        print('Nice try 👏')
        print(data['ques_2']['explanation'])
        print(data["ques_2"]["option_1"])
        
        inp1 = input('')
        if inp1 =="t.count(2)":
             print('Nice try 👏')
             print(data['ques_3']['explanation'])
             print(data["ques_3"]["option_1"])
             print(data["ques_3"]["option_2"])
             inp2 = input('chioce the correct option')
             if inp2=="2":
                 print('You are the winner of this Gmae please take your crown 👑')
    
        else:
             print('you lose the game 😪')
