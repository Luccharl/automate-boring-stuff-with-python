# Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is
# stored in spam, and prints Greetings! if anything else is stored in spam

import numbers


spam = int(input())

if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings')
    

# Write a short program that prints the numbers 1 to 10 using a for loop.
# Then write an equivalent program that prints the numbers 1 to 10 using
# a while loop.

for num in range(1, 11):
    print(num)
    
numbers = 1
while numbers < 11:
    print(numbers)
    numbers += 1