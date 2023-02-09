import random

def flips():
    
    choices = ['H','T']
    outcomes = list()
    
    for _ in range(attempts):
        moves = random.choice(choices)      
        outcomes.append(moves)
        
    return outcomes
        
def streak(attempts):
    
    result = flips()
    strk = 0
    seq = 0
    num_streak = 0
    
    for i in range(len(result)):
        if seq == result[i]:
            strk += 1 
        else:
            seq = result[i]
            strk = 1
            
        if strk >= 6:
            num_streak += 1
            strk = 0
            
    # print(result)
    # print(strk)
    print(num_streak)
    
    probability = (num_streak/attempts)*100
           
    print(f'Chance of streak: {probability:.2f}%')

attempts = 10000        
streak(attempts)