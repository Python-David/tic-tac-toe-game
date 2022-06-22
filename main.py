from game_brain import GameBrain

game = GameBrain()
game_on = True

print("Welcome to TIC-TAC-TOE!\n")
print(f"{game.display()}\n")

while game_on:
    clear_1 = False

    while not clear_1:
        p1_input = int(input("Player 1 is 'X', pick a number to play: "))
        if game.check_input(1, p1_input) == "Go":
            game.update(p1_input, 1)

            if game.win_lose_or_draw() == "Win X":
                print("Player 1 wins!")
                # end or restart game
                end_or_restart = input("Will you like to play again? y/n: ")
                if end_or_restart.lower() == "n":
                    game_on = False
            elif game.win_lose_or_draw() == "Win O":
                print("Player 2 wins!")
                # end or restart game
                end_or_restart = input("Will you like to play again? y/n: ")
                if end_or_restart.lower() == "n":
                    game_on = False
            else:
                pass

            if game.game_status():
                if game.win_lose_or_draw() is None:
                    print("It's a draw")
                    # end or restart game
                    end_or_restart = input("Will you like to play again? y/n: ")
                    if end_or_restart.lower() == "n":
                        game_on = False

            clear_1 = True
        else:
            print(f"{game.check_input(1, p1_input)}")

    clear_2 = False

    while not clear_2:
        p2_input = int(input("\nPlayer 2 it's your turn, pick a number to play: "))
        if game.check_input(2, p2_input) == "Go":
            game.update(p2_input, 2)

            if game.win_lose_or_draw() == "Win X":
                print("Player 1 wins!")
                # end or restart game
                end_or_restart = input("Will you like to play again? y/n: ")
                if end_or_restart.lower() == "n":
                    game_on = False
            elif game.win_lose_or_draw() == "Win O":
                print("Player 2 wins!")
                # end or restart game
                end_or_restart = input("Will you like to play again? y/n: ")
                if end_or_restart.lower() == "n":
                    game_on = False
            else:
                pass

            if game.game_status():
                if game.win_lose_or_draw() is None:
                    print("It's a draw")
                    # end or restart game
                    end_or_restart = input("Will you like to play again? y/n: ")
                    if end_or_restart.lower() == "n":
                        game_on = False
            clear_2 = True
        else:
            print(f"{game.check_input(2, p2_input)}")
