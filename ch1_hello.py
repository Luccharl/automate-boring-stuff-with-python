#This program say hello and asks for my name

print('Hello, World!')
print('What is your name') #ask user for their name
user_name = input()
print(f'It is nice to meet you {user_name}')
print(f'The length of your name is {len(user_name)}')
print('How old are you?') #ask for age
user_age = input()
print(f'You will be {int(user_age) + 1} in a year')