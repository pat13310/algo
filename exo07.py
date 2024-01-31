import random

class DevineNombreMagique:
    def __init__(self):
        self.limite_inferieure = 1
        self.limite_superieure = 100

    def afficher_instructions(self):
        print("Pensez à un nombre entre 1 et 100 inclus.")
        input("Appuyez sur Entrée lorsque vous êtes prêt...")

    def deviner_nombre(self):
        return random.randint(self.limite_inferieure, self.limite_superieure)

    def afficher_proposition(self, nombre_devine):
        print("Est-ce que votre nombre est", nombre_devine, "?")

    def mettre_a_jour_limites(self, indication, nombre_devine):
        if indication == "+":
            self.limite_superieure = min(self.limite_superieure, nombre_devine - 1)
        elif indication == "-":
            self.limite_inferieure = max(self.limite_inferieure, nombre_devine + 1)

    def jouer(self):
        self.afficher_instructions()
        nombre_trouve = False

        while not nombre_trouve:
            nombre_devine = self.deviner_nombre()
            self.afficher_proposition(nombre_devine)

            
            indication = input("Indiquez si le nombre est trop grand (+), trop petit (-) ou correct (=) : ")

            if indication in ['+', '-', '=']:
                if indication == "=":
                    nombre_trouve = True
                    print("Super ! J'ai trouvé votre nombre magique.")
                else:
                    self.mettre_a_jour_limites(indication, nombre_devine)
            else:
                print("Veuillez entrer une indication valide (+, - ou =).")

if __name__ == "__main__":
    jeu = DevineNombreMagique()
    jeu.jouer()
