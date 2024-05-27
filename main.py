import random
print ('What is your name?')
Myname =input ()
print ('Hello ' + str ( Myname ) + ' Welcome to my guess game, '
                                      'I am thinking of a number between 1 and 15. Take a guess')
secret_num = random.randint(1, 15)
while True:
    # Get player's guess

    for guessesTaken in range(1,7):
        print('Lets start by taking a guess.')
        guess = int(input())
        if guess > secret_num:
            print('guess is too high.')
        elif guess < secret_num:
            print ('guess is too low.')

    if guess == secret_num:
        break  # This condition is for the correct guess
        print('Good job' + str (Myname)  + ' You guessed my number in ' + str ( guessesTaken ) + ' guesses!')
    else:
        print( "Sorry that's not correct," + str (Myname) + " the secret number is " + str (secret_num) + " thank you for playing!")

