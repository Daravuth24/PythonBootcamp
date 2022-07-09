import random

intro_message = "Welcome to the dices games!"


def dice_roll():

    while True:
        # Reference for sum at the end of code
        sum_all = 0

        try:

            while True:

                # User input the number of dice they want to roll
                number_of_rolled_dice = input("Enter the number of dices you want to roll:")

                # Checking for correct usage
                if int(number_of_rolled_dice) <= 0 or int(number_of_rolled_dice) > 8:
                    print("USAGE: The number must be between 1 and 8")

                    continue

                # Correct usage
                elif int(number_of_rolled_dice) >= 1 or int(number_of_rolled_dice) <= 8:

                    # Generating random rolled dice number
                    for dice_number in range(int(number_of_rolled_dice)):

                        # Condition and statement for 1 dice
                        if int(number_of_rolled_dice) == 1:
                            rolled_number = random.randint(1, 6)
                            print(f"RESULT: {rolled_number}")

                        # Condition and statement for multiple dices
                        elif int(number_of_rolled_dice) != 1:
                            rolled_number = random.randint(1, 6)
                            sum_all += rolled_number
                            print(f"Dice {dice_number+1}: {rolled_number}")

                    # Print the sum for multiple dices
                    if int(number_of_rolled_dice) != 1:
                        print(f"{'=' * 10} \nRESULT: {sum_all}\n{'=' * 10}")

                # Break out of second loop
                break

        # Checking for anything other than integer between 1 and 8
        except ValueError:
            print("USAGE: The number must be between 1 and 8")

            continue

        # Break out of first loop
        break


dice_roll()
