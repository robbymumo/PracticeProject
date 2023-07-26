import random
# Generating random numbers in a range anf guessing till you get it
# Generate the random number
random_num = random.randint(1, 100)
guess_count = 0
while True:
    guess = int(input('Guess the random Number: '))
    guess_count += 1
    if guess == random_num:
        print(f'You win! the random number is {random_num}')
        print(f'You attempted {guess_count} times')
        break
    elif guess > random_num:
        print('You were above the number')
    elif guess < random_num:
        print('You were below the number')
