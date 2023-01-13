from random import randint
from exo1 import Robot
from exo2_human import Human

class Cyborg(Robot, Human):   
    def __init__(self, name, sexe):   
        Robot.__init__(self, name)
        Human.__init__(self, sexe)
        self.name = name
        self.sexe = sexe
            
    def charge(self):
        Robot.chargeBattery(self)

    def status(self):
        print(Robot.__str__(self))
        print(Human.__str__(self))
    
    def eat(self,aliment):
        print(self.name + " mange " + aliment)

    def digest(self,):
        print(self.name, " a digéré ")


# Main

if __name__ =='__main__':
    cyborg = Cyborg('Deux Ex Machina', 'M')

    print(cyborg.name, 'sexe', cyborg.sexe)
    print('Charging battery...')
    cyborg.charging()
    cyborg.status()
    cyborg.eat('banana')
    cyborg.digest()
    cyborg.eat(['coca', 'chips'])
    cyborg.digest()