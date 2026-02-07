"""
This program generated random cards from two lists based on the user inputs.
author: A Farah
date: 02/06/2025
"""
import random

#create a list of values and suits to generate random cards
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = [ "c", "h", "s", "d"]

while True:
    try:
        #ask the user for the number of cards they want in their hand
        number_cards=int(input("Please enter the number of cards you want in your hand: "))
        #generating random cards based on the user input and display the cards and the total number of cards in the user's hand
        if number_cards > 0:
            hand = [random.choice(values) + random.choice(suits) for _ in range(number_cards)]
            print("The cards on the hand are:", hand)
            print("The total number of cards in user's hand is:", len(hand))
        #if the user enters a number less than or equal to 0, display an error message and prompt the user to enter a valid number of cards   
        elif number_cards <= 0:
            print("Please enter a number greater than 0.")
            continue
    #if the user enters an invalid input (e.g., a non-integer), display an error message and prompt the user to enter a valid number of cards   
    except ValueError:
        print("Invalid input. Please enter a valid number of cards.")
        continue
    #ask the user if they want to play again, if the user enters 'y', the program will continue, otherwise it will end and displays a goodbye message
    play_again = input("Do you want to play again? (y/n): ")
    
    if play_again.lower() != 'y':
        print("Thank you for playing, see you later!")
        break