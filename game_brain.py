class GameBrain:
    def __init__(self):
        self.n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.p1 = "X"
        self.p2 = "O"

    def display(self):
        tic_tac_toe = f"{self.n[0]} | {self.n[1]} | {self.n[2]}\n" \
                      f"---------\n" \
                      f"{self.n[3]} | {self.n[4]} | {self.n[5]}\n" \
                      f"---------\n" \
                      f"{self.n[6]} | {self.n[7]} | {self.n[8]}"

        return tic_tac_toe

    def update(self, user_input, player):
        if player == 1:
            self.n[user_input - 1] = self.p1
            print(self.display())

        elif player == 2:
            self.n[user_input - 1] = self.p2
            print(self.display())

    def check_input(self, player, user_input):
        if player == 1 and user_input in range(0, 10):
            if user_input in self.n:
                return "Go"
            else:
                if self.n[user_input - 1] == self.p1:
                    return "You have already played this, pick another number!"
                elif self.n[user_input - 1] == self.p2:
                    return "Player 2 has already played this, pick another number!"

        if player == 2 and user_input in range(0, 10):
            if user_input in self.n:
                return "Go"
            else:
                if self.n[user_input - 1] == self.p1:
                    return "Player 1 has already played this, pick another number!"
                elif self.n[user_input - 1] == self.p2:
                    return "You have already played this, pick another number!"

        elif player == 1 or player == 2 and user_input not in range(0, 10):
            return "You can only pick a number from 0-9, try again!"

    def game_status(self):
        return all(isinstance(x, str) for x in self.n)

    def win_lose_or_draw(self):
        if self.n[0] == self.n[1] == self.n[2]:
            return f"Win {self.n[0]}"
        elif self.n[3] == self.n[4] == self.n[5]:
            return f"Win {self.n[3]}"
        elif self.n[6] == self.n[7] == self.n[8]:
            return f"Win {self.n[6]}"
        elif self.n[0] == self.n[3] == self.n[6]:
            return f"Win {self.n[0]}"
        elif self.n[1] == self.n[4] == self.n[7]:
            return f"Win {self.n[1]}"
        elif self.n[2] == self.n[5] == self.n[8]:
            return f"Win {self.n[2]}"
        elif self.n[0] == self.n[4] == self.n[8]:
            return f"Win {self.n[0]}"
        elif self.n[2] == self.n[4] == self.n[6]:
            return f"Win {self.n[2]}"
        else:
            return None

