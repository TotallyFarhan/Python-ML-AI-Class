from Fighter import *

class Arena:
    def __init__ (self):
        self.winner = "No Winner Yet"

    

    
    def Fight(self, fighterA, fighterB):
        print("Welcome to the Arena!")
        print("Fighting today, we have:")
        
        print(fighterA.name)
        print("vs")
        print(fighterB.name)

        fightOver = False

        while fightOver is not True:
            print("====================================")
            print("------------------------------------")
            print(fighterA.ToString())
            print("------------------------------------")
            print(fighterB.ToString())
            print("------------------------------------")


            damageDealt = fighterA.attack()
            print(fighterA.name, "attacks", fighterB.name)
            print(fighterA.name, "hits", fighterB.name, "for", damageDealt, "damage!")
            fighterB.takeDamage(damageDealt)


            damageDealt = fighterB.attack()
            print(fighterB.name, "attacks", fighterA.name)
            print(fighterB.name, "hits", fighterA.name, "for", damageDealt, "damage!")
            fighterA.takeDamage(damageDealt)

            print("====================================")

            if fighterA.isDead() is True or fighterB.isDead() is True:
                fightOver = True
                

            

            
#class
    #function
        #insideFunction
        if fighterA.isDead() and fighterB.isDead():
            print("A Tie! They Both Died!")
            print(fighterA.ToString())
            print(fighterB.ToString())

        
        elif fighterA.isDead():
            print(fighterB.name, "has won!")
            print(fighterB.ToString())
            self.winner = fighterB.name

        elif fighterB.isDead():
            print(fighterA.name, "has won!")
            print(fighterA.ToString())
            self.winner = fighterA.name

        else:
            print("They are both alive. Why'd they stop fighting?")
    











            
        
    
