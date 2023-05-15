rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random

x = int(input("How many times would you like to play?"))
player1_wins = []
player2_wins = []
ties = []

for i in range(x):

    prs = [paper, rock, scissors]

    player1 = random.choice(prs)
    player2 = random.choice(prs)
    print(f"You chose:\n{player1}")
    print("\n")
    print(f"Computer chose:\n{player2}")

    if player1 == player2:
        print("\nIt's a tie!")
        ties.append("1")

    elif (player1 == prs[0] and player2 == prs[2]) or (player1 == prs[1] and player2 == prs[0]) or (
            player1 == prs[2] and player2 == prs[1]):
        print("\nPlayer 2 Wins!")
        player2_wins.append("1")

    else:
        print("\nPlayer 1 Win!")
        player1_wins.append("1")

    print("\n")

    player1_score = len(player1_wins)
    player2_score = len(player2_wins)
    tiescore = len(ties)

print(f"Player 1 won {player1_score} times, Player 2 won {player2_score} times, and they tied {tiescore} times..")



