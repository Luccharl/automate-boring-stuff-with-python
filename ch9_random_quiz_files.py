#! python3
#random_quiz_files.oy - creates quizzes with questions and answers
#in random order along with the answers key

import random

#The quiz content. Keys for states and values for their capitals
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 
'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 
'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#generates 35 quiz files
for quiz_num in range(35):
    #CREATE THE QUIZ AND ANSWER KEY FILES   
    quiz_file = open(f'capitals_quiz{quiz_num + 1}.txt', 'w')
    answer_file = open(f'capitals_answer{quiz_num + 1}.txt', 'w')
    
    #Write out the header for the quiz.
    quiz_file.write('Name: \n\nDate: \n\nPeriod:\n\n')
    quiz_file.write((' ' * 15)+ f'State Capitals Quiz (Form {quiz_num+1})')
    quiz_file.write('\n\n')
    
    #Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)
    
    #Loop through all 50 states, making a question for each.
    for question_num in range(len(states)):
        
        #get the right and wrong answers
        correct_answer = capitals[states[question_num]]
        wrong_answer = list(capitals.values())
        del wrong_answer[wrong_answer.index(correct_answer)]
        wrong_answer = random.sample(wrong_answer, 3)
        answer_choices = wrong_answer + [correct_answer]
        random.shuffle(answer_choices)
        
        #Write question and answer options to the quiz file
        quiz_file.write(f'{question_num + 1}. What is the capital of {states[question_num]}?\n')
        for i in range(4):
            quiz_file.write(f'\t{"ABCD"[i]}.{ answer_choices[i]}\n\n')
            
        #write answer key to file
        answer_file.write(f'{question_num + 1}. {"ABCD"[answer_choices.index(correct_answer)]}\n')
    quiz_file.close()
    answer_file.close()
    
print('Ok')
        