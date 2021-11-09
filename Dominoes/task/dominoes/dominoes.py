import random

# list all players (script should work for 2 or more players)
players = ["computer",
           "player"]
stock = []  # complete set created and dealt from this
snake = []  # holds snake
next_player = -1  # whose turn is it?
hands = []  # pre-allocated set of hands, 1 for each player
for i in range(0, len(players)):
    hands.append([[]] * 7)


# generate new shuffled set
def get_fresh_stock():
    fresh_stock = []
    for left in range(0, 7):
        for right in range(left, 7):
            fresh_stock.append([left, right])
    random.shuffle(fresh_stock)
    return fresh_stock

def do_ai_move():
    left_end = snake[0][0]
    right_end = snake[-1][1]
    number_qty = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in hands[0] + stock:
        for j in i:
            number_qty[j] = number_qty[j] + 1
    play = 0
    high_count = 0
    for i in range(0, len(hands[0])):
        if left_end in hands[0][i] or right_end in hands[0][i]:
            if (hands[0][i][0] + hands[0][i][1]) > high_count:
                high_count = hands[0][i][0] + hands[0][i][1]
                play = i + 1
                if left_end in hands[0][i]:
                    play = play * -1
    return play



# pre-allocate set of hands for each player

# keep looping till starter is dealt
while not snake:
    stock = get_fresh_stock()
    starter = []  # hold highest double while dealing
    for i in range(0, 7):
        for j in range(0, len(players)):
            hands[j][i] = stock.pop()
            if (hands[j][i][0] == hands[j][i][1]) and \
                    hands[j][i] > starter:
                starter = hands[j][i]
    if starter:
        for i in range(0, len(players)):
            # remove highest double from player's set and ID next player
            if starter in hands[i]:
                hands[i].remove(starter)
                next_player = ((i + 1) % len(players))
                break
        snake.append(starter)

# keep looping till win, lose or draw.
game_over = False
do_print = True
while not game_over:
    # print game status
    if do_print:
        # print output
        print("=" * 70)
        print("Stock size:", len(stock))
        for i in range(0, len(players)):
            if players[i].lower() == "computer":
                print("Computer pieces:", len(hands[i]))
                break
        print("")
        snake_string = ""
        for i in range(0, len(snake)):
            if (i < 3) or (i > len(snake) - 4):
                snake_string += str(snake[i])
            elif i == 3:
                snake_string += "..."
        print(snake_string)
        print()
        print("Your pieces:")
        for i in range(0, len(players)):
            if players[i].lower() == "player":
                for j in range(0, len(hands[i])):
                    print(f"{j + 1}:{hands[i][j]}")
                break
        print()

    # check for end-of-game

    # either player out of tiles??
    for i in range(0, len(players)):
        if len(hands[i]) == 0:
            if players[i].lower() == "computer":
                print("Status: The game is over. The computer won!")
            else:
                print("Status: The game is over. You won!")
            game_over = True
    if game_over:
        break
    # if the ends of snake have same and all of that number are played
    # (there are 8 occurrences of a number) then game is a draw
    if (len(snake) > 6) and (snake[0][0] == (snake[len(snake) - 1][1])):
        number_plays = 0
        for i in range(0, len(snake)):
            for j in range(0, len(snake[i])):
                if snake[0][0] == snake[i][j]:
                    number_plays += 1
        if number_plays == 8:
            print("Status: The game is over. It's a draw!")
            game_over = True
    if game_over:
        break

    # do a move
    move = ""
    move_int = 99
    if players[next_player].lower() == "computer":
        if do_print:
            print("Status: Computer is about to make a move. Press Enter to continue...")
            input()
        move_int = do_ai_move()
        move = str(move_int)
    elif players[next_player].lower() == "player":
        if do_print:
            print("Status: It's your turn to make a move. Enter your command.")
        move = input()
        if (len(move) == 1) and (move.isnumeric()):
            move_int = int(move)
        elif (len(move) == 2) and (move[0] == "-") and (move[1].isnumeric()):
            move_int = int(move)

    # validate move and if valid execute it
    if (abs(move_int) > len(hands[next_player])):
        if players[next_player].lower() == "player":
            print("Invalid input. Please try again.")
        do_print = False
    elif ((move_int < 0) and (snake[0][0] not in hands[next_player][abs(move_int) - 1])) or \
         ((move_int > 0) and (snake[-1][-1] not in hands[next_player][move_int - 1])):
        if players[next_player].lower() == "player":
            print("Illegal move. Please try again.")
        do_print = False
    else:
        if move_int == 0:
            if len(stock) > 0:
                hands[next_player].append(stock.pop())
        elif move_int < 0:
            snake.insert(0, hands[next_player].pop(abs(move_int) - 1))
            if snake[0][1] != snake[1][0]:
                snake[0][0], snake[0][1] = snake[0][1], snake[0][0]
        elif move_int > 0:
            snake.append(hands[next_player].pop(move_int - 1))
            if snake[-1][0] != snake[-2][1]:
                snake[-1][1], snake[-1][0] = snake[-1][0], snake[-1][1]
        next_player = ((next_player + 1) % len(players))
        do_print = True
