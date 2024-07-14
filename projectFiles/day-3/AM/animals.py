class Animal:
  def __init__(self, species, name, sound):
    self.species = species
    self.name = name
    self.sound = sound
 
  def speak(self):
    print(self.sound + "... my name is " + self.name + ".")
    print("   I am a " + self.species + ".")
 
dog = Animal("dog", "Bingo", "woof")
duck = Animal("duck", "Donald", "quack")
horse = Animal("horse", "Ed", "neigh")
pig = Animal("pig", "Porky", "oink")
 
dog.speak()
duck.speak()
horse.speak()
pig.speak()
 
