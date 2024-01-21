import random

print("This is a game of luck. Every time you are presented with a magic number, and you have\n"
      "an option to play the game or not. If you decide to play the game you can rely only on\n"
      "luck nothing else because when you roll the dices if your number is closest to\n the magic number "
      "you win, otherwise you lose.")

dice = [1, 2, 3, 4, 5, 6]
wining_number = random.choice(dice) + random.choice(dice)
print(f"\033[1m~~~~~THE MAGIC NUMBER IS: {wining_number}!~~~~~\033[0m")


def player_roll():
    player = input("Do you want to roll the dices? 'Y' or 'N': ").lower()
    if player == "y":
        player_dices = random.choice(dice) + random.choice(dice)
        return player_dices
    else:
        raise SystemExit("You exited the game. Have a nice day!")


def computer_roll():
    computer = random.choice(dice) + random.choice(dice)
    return computer


def comparing_the_dice(player_move, computer_move):
    player_luck = abs(wining_number - player_move)
    computer_luck = abs(wining_number - computer_move)
    if player_luck < computer_luck or player_move == wining_number:
        return f"Player rolled {player_move}, Computer rolled {computer_move}.\nYou win."
    elif player_luck == computer_luck:
        return f"Both rolled {computer_move}. It's a draw."
    else:
        return f"Player rolled {player_move}, Computer rolled {computer_move}.\nYou lose."


def game_on():
    result = comparing_the_dice(player_roll(), computer_roll())
    print(result)


game_on()
