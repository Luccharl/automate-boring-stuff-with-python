import random,time

total_correct = 0
tries = 1
       
for problem in range(10):
    
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    
    correct_answer = num1 * num2
    
    while True:
        answer = int(input(f'{num1} X {num2}: '))
        
        if answer == correct_answer:
            print('Correct!')
            time.sleep(1)
            total_correct += 1
            break
        
        elif answer != correct_answer and tries == 3:
            print(f'Incorrect! you ran of out of tries ({tries})')
            break
        
        else:
            print('Incorrect')
            tries += 1
        
print(f'Your total scores is {total_correct}/10')