import random

class Player:
  luck = 0
  
  def __init__(self, name, rank):
    self.name = name
    self.rank = rank
 
  def play_against(self, opponent):
    self.luck = random.randint(0, 100)
    opponent.luck = random.randint(0, 100)
    if self.rank + self.luck > opponent.rank + opponent.luck:
        print(self.name + " is victorious over " + opponent.name + ".")
    elif self.rank + self.luck < opponent.rank + opponent.luck:
        print(self.name + " is defeated by " + opponent.name + ".")
    else:
        print("No clear champion emerges.")

players = [Player("Abe", 10),
           Player("Barb", 80),
           Player("Caleb", 150),
           Player("Daphne", 220)]

challenger = players[random.randrange(len(players))]
print(challenger.name + " challenges all other players!\n")
for player in players:
    if player is not challenger:
        challenger.play_against(player)
        

 
