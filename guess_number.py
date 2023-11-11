import random

print("This game generates a random number within a range, then asks you to guess the number.")

play = input('Do you want to play?  Yes or No: ').lower()

if play != "yes":
    if play != 'y':
        quit()

print('Enter "finis" to quit the game at any time...')

while True:
    top_of_range = input('How big of a set of numbers to you want to generate (i.e.,10?, 20?, 100?): ')

    if top_of_range == "finis":
        quit()

    try:
        top_of_range = int(top_of_range)
        if top_of_range < 0:
            print('Enter a number greater than zero')
            continue

    except ValueError:
        print("Enter a whole number only")
        continue

    random_number = random.randint(0, top_of_range)
    guesses = 0

    while True:
        guesses += 1
        user_guess = input("Guess a number: ")

        if user_guess == "finis":
            quit()

        if user_guess.isdigit():
            user_guess = int(user_guess)

        else:
            print('Please type a whole number only, greater than zero')
            continue

        if user_guess == random_number:
            print('You guessed the number!')
            break

        elif user_guess > top_of_range:
            print('Your guess it outside the range')
        elif user_guess > random_number:
            print('Your guess is greater than the number')
        else:
            print('Your guess is less than the number')

    print("You got it in", guesses, "guesses")
