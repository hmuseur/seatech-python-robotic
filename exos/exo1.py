import time

class Robot():
    name = "named"
    power = False
    current_speed = 0
    battery_level = 0
    states = ['shutown', 'running']
    
    ####Affichage du nom######
    def __init__(self, name):
        if name:
            self.name = name
            self.power = True

    ####Affichage pour l'état du robot######
    def off(self):
            self.power = False

    ####Affichage du chargement du robot######
    def charging(self):
        while self.battery_level < 100:
            time.sleep(0.1)
            self.battery_level = self.battery_level +1
            print(self.battery_level)

    ####Affichage du mouvement du robot######
    def movement(self,speed):
        if type(speed) == int:
            self.current_speed = speed

    ####Affichage pour arrêter le robot######
    def stop(self):
        self.current_speed = 0

    ####Affichage de la vitesse du robot######
    def speed(self):
        return self.current_speed

    ####Affichage du résumé des actions du robot######
    def resume(self):
        print("Le nom du robot est %s"%(r.name))
        print("Bobby power is %s"%(r.power))
        print("Le pourcentage de la batterie est de " + f'{r.battery_level}'+ "%")
        print ("La vitesse de déplacement est de "+str(r.speed()) + "km/s")


#####MAIN#####

""" r = Robot(name='Bobby')
print("Le nom du robot est %s"%(r.name))
print("Bobby power is %s"%(r.power))
print("Le pourcentage de la batterie est de " + f'{r.battery_level}' + "%")
r.charging()
print("\n")
print("Le pourcentage de la batterie est de " + f'{r.battery_level}')
print("Bobby power is %s"%(r.power))
r.stop()
print("La vitesse de déplacement est de " + f'{r.speed()}'+"m/s")
r.movement(80)
print ("La vitesse de déplacement est de "+ f'{r.speed()}'+"m/s")
print("\n")
print("Résumé du robot")
print("\n")
r.resume()
r.off()	
 """