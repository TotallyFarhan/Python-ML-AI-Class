import random

class Player:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank
    def display_player(self):
            print(str(self.name) + ", " + str(self.rank))
    def play_against(self, player):
        if random.randint(self.rank - 10, self.rank + 10) < random.randint(player.rank - 10, player.rank + 10):
            print(self.name + " beats " + player.name + "!")
            
        else:
            print(player.name + " beats " + self.name + "!")

p1 = Player("Player 1", random.randint(1, 100))
p1.display_player()

p2 = Player("Player 2", random.randint(1, 100))
p2.display_player()

p3 = Player("Player 3", random.randint(1, 100))
p3.display_player()

p4 = Player("Player 4", random.randint(1, 100))
p4.display_player()

p5 = Player("Player 5", random.randint(1, 100))
p5.display_player()

p6 = Player("Player 6", random.randint(1, 100))
p6.display_player()

p7 = Player("Player 7", random.randint(1, 100))
p7.display_player()

p8 = Player("Player 8", random.randint(1, 100))
p8.display_player()

print()

players = [p1, p2, p3, p4, p5, p6, p7, p8]

print("Tournament")
print()

for player in players:
    if (player != p1):
        p1.play_against(player)
