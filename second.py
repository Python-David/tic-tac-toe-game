from game_brain import GameBrain

game = GameBrain()
game_on = True
clear_player_one = False
clear_player_two = False

print("Welcome to TIC-TAC-TOE!\n")
print(f"{game.display()}\n")

while game_on:
    while not clear_player_one:
        p1_input = int(input("Player 1 is 'X', pick a number to play: "))
        if game.check_input(1, p1_input) == "Go":
            game.update(p1_input, 1)
            clear_player_two = False

            if game.win_lose_or_draw() == "Win X":
                print("Player 1 wins!")

                # END OR RESTART GAME
                game_end_or_restart = input("Will you like to play again? y/n: ")
                if game_end_or_restart == "n":
                    clear_player_one = True
                    clear_player_two = True
                    game_on = False
                    print("GAME OVER.")

            elif game.win_lose_or_draw() == "Win O":
                print("Player 2 wins!")

                # END OR RESTART GAME
                game_end_or_restart = input("Will you like to play again? y/n: ")
                if game_end_or_restart == "n":
                    clear_player_one = True
                    clear_player_two = True
                    game_on = False
                    print("GAME OVER.")

            else:
                pass

            if game.game_status():
                if game.win_lose_or_draw() is None:
                    print("It's a draw")

                    # END OR RESTART GAME
                    game_end_or_restart = input("Will you like to play again? y/n: ")
                    if game_end_or_restart == "n":
                        clear_player_one = True
                        clear_player_two = True
                        game_on = False
                        print("GAME OVER.")

            clear_player_one = True
        else:
            print(f"{game.check_input(1, p1_input)}")

    while not clear_player_two:
        p2_input = int(input("\nPlayer 2 it's your turn, pick a number to play: "))
        if game.check_input(2, p2_input) == "Go":
            game.update(p2_input, 2)
            clear_player_one = False

            if game.win_lose_or_draw() == "Win X":
                print("Player 1 wins!")

                # END OR RESTART GAME
                game_end_or_restart = input("Will you like to play again? y/n: ")
                if game_end_or_restart == "n":
                    clear_player_one = True
                    clear_player_two = True
                    game_on = False
                    print("GAME OVER.")

            elif game.win_lose_or_draw() == "Win O":
                print("Player 2 wins!")

                # END OR RESTART GAME
                game_end_or_restart = input("Will you like to play again? y/n: ")
                if game_end_or_restart == "n":
                    clear_player_one = True
                    clear_player_two = True
                    game_on = False
                    print("GAME OVER.")

            else:
                pass

            if game.game_status():
                if game.win_lose_or_draw() is None:
                    print("It's a draw")

                    # END OR RESTART GAME
                    game_end_or_restart = input("Will you like to play again? y/n: ")
                    if game_end_or_restart == "n":
                        clear_player_one = True
                        clear_player_two = True
                        game_on = False
                        print("GAME OVER.")

            clear_player_two = True

        else:
            print(f"{game.check_input(2, p2_input)}")