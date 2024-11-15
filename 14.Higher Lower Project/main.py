from art import logo
from art import vs
from game_data import data
import random
print(logo)


current_score=0
Final_score=0
Game_over=False

def get_random_data_indices():
    return random.sample(range(len(data)), 2)  # Get two unique random indices

while not Game_over:
    (random_number_1, random_number_2) = get_random_data_indices()
    print(
        f"Compare A: {data[random_number_1]['name']}, {data[random_number_1]['description']}, from {data[random_number_1]['country']}")
    print(vs)
    print(
        f"Against B: {data[random_number_2]['name']}, {data[random_number_2]['description']}, from {data[random_number_2]['country']}")
    A = data[random_number_1]['follower_count']
    B = data[random_number_2]['follower_count']


    answer = input("Who has more followers? Type 'A' or 'B':")
    answer = answer.upper()

    higher_follower_count = max(data[random_number_1]['follower_count'], data[random_number_2]['follower_count'])

    if answer == 'A' and A == higher_follower_count:
        current_score += 1

        print("\n" * 20)
        print(f"You're right! Current score: {current_score}")
        print(logo)
    elif answer == 'B' and B == higher_follower_count:
        current_score += 1

        print("\n" * 20)
        print(f"You're right! Current score: {current_score}")
        print(logo)
    else:

        Game_over = True
        print(f"Sorry, that's wrong. Final score: {current_score}")

