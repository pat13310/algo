import random
import keyboard
import time
import os

MIN_VALUE=1
MAX_VALUE=100


class DevineNombreMagique:
    def __init__(self):
        self.limite_inferieure = MIN_VALUE
        self.limite_superieure = MAX_VALUE
        self.nombre_essais=0
        self.nombre_trouve=False

    def afficher_instructions(self):
        print("Pensez à un nombre entre ",MIN_VALUE," et ", MAX_VALUE," inclus.")
        input("Appuyez sur Entrée lorsque vous êtes prêt...")

    def deviner_nombre(self):
        if  self.limite_inferieure > self.limite_superieure:
            self.limite_superieure,self.limite_inferieure=self.limite_inferieure,self.limite_superieure 

        if self.limite_inferieure == self.limite_superieure:  
            self.nombre_trouve=True          
            return self.limite_superieure
        
        return random.randint(self.limite_inferieure, self.limite_superieure)

    def afficher_proposition(self, nombre_devine):
        print("[Tentative n°",self.nombre_essais+1,"] Est-ce que votre nombre est", nombre_devine, "?")

    def mettre_a_jour_limites(self, indication, nombre_devine):
        if indication == "+":
            if self.limite_superieure >=MAX_VALUE:
                self.limite_superieure=MAX_VALUE
            self.limite_inferieure = max(self.limite_inferieure, (nombre_devine + 1))
        elif indication == "-":
            self.limite_superieure = min(self.limite_superieure, (nombre_devine - 1))

    def jouer(self):
        self.afficher_instructions()
        self.nombre_trouve = False
        
        while not self.nombre_trouve and self.nombre_essais<6 :
            nombre_devine = self.deviner_nombre()
            self.afficher_proposition(nombre_devine)
            self.nombre_essais+=1
            indication = self.attendre_indication()

            if indication in ['+', '-', 'o']:
                if indication == "o":
                    self.nombre_trouve = True                    
                else:
                    self.mettre_a_jour_limites(indication, nombre_devine)
            else:
                print("Veuillez entrer une indication valide (+, - ou o).")

            if self.nombre_trouve:
                print("Super ! J'ai trouvé votre nombre magique.")

            if not self.nombre_trouve and self.nombre_essais==6 :
                print("Dommage!")    

    def attendre_indication(self):
        indication = None
        while indication not in ['+', '-', 'o']:
            if keyboard.is_pressed('+'):
                indication = '+'
            elif keyboard.is_pressed('-'):
                indication = '-'
            elif keyboard.is_pressed('o'):
                indication = 'o'
            time.sleep(0.21)
        return indication


if __name__ == "__main__":
    jeu = DevineNombreMagique()
    jeu.jouer()
    
    

