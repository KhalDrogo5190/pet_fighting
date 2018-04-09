import random

class Pet:

    def __init__(self, name):
        self.name = name
        self.is_alive = True
        self.health = 10
        self.skip = False

    
    def bite(self, other):
        if self.is_alive and not self.skip:
            print("Who wants some munchies!")
            other.health -= 1
            num = random.randint(1, 5)
            if num >= 4:
                other.skip = True
                print(other.name + " is now paralyzed for uno turn")
        elif self.skip:
            print("Can toad  dude that my bro beans")
            self.skip = False
        else:
            print("No munchies for the dead :(")
            self.skip = False


    def slap(self, other):
        if self.is_alive and not self.skip:
            print("NO MORE BANANAS YOU FOOL")
            other.health -=2
        elif self.skip:
            print("MY BANANAS ARE ALL FROZEN")
            self.skip = False
        else:
            print("SNOOORRRRRRRRRRRRRE")
            self.skip = False
    
            
            
    def thow(self, other):
        if self.is_alive and not self.skip:
            print("See ya on the flippty flop!")
            other.health -=3
            self.health -= 1
        elif self.skip:
            print("No flippty flops on the beach")
            self.skip = False
        else:
            print("I can no do that señor")
            self.skip = False


    
    
pet1 = Pet("Saleem ")
pet2 = Pet("Awesome Man")

