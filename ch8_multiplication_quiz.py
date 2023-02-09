from cmd import PROMPT
import pyinputplus as pyip
import time, random

total_questions = pyip.inputInt('Enter the total number of questions to generate: ')
correct_answer = 0

for question_num in range(1, total_questions + 1):
    
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    
    prompt = f'#{question_num}: {num1} X {num2} = '    
    product = num1 * num2

    try:
        pyip.inputStr(prompt, allowRegexes=[rf'^{product}$'], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=1)
    except pyip.TimeoutException:
        print('You ran out of time')
    except pyip.RetryLimitException:
        continue
    else:
        print('Correct!')
        correct_answer += 1
        
    time.sleep(1)       
print(f'You have a total of {correct_answer} correct answer out of {total_questions} questions')