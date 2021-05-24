import random
print('Let\'s guess a number!.')

num = random.randint(1, 100)
count = 3
sum = 0

while True:
    if count != 0:
        guess = int(input('You only have %d tries. \nGuess a integer number from 1 to 100: ' % count))
        if guess > num:
            count -= 1
            sum += 1
            print('Guess smaller.')
        elif guess < num:
            count -= 1
            sum += 1
            print('Guess bigger.')
        else:
            sum += 1
            print('Congrats! The number is %d.' % num)
            if count == 3:
                print('You took 1 try to reach to the right number.')
            else:
                print('You took %d tries to reach to the number.' % sum)
            break
    else:
        print('BOOM! You failed to guess the right number!')
        print('The number is %d.' % num)
        break