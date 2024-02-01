userfirst=False
userOneInput=[]
userTwoInput=[]

matrix = [["X", "2", "3"], ["X", "5", "6"],  ["X", "8", "9"]]

def showRules():
    rules_text = """
    Règles du Morpion (Tic-Tac-Toe) :

    1. Le jeu se joue sur une grille de 3x3.
    2. Deux joueurs s'affrontent, l'un utilisant X et l'autre O.
    3. Le joueur qui parvient à aligner trois de ses symboles horizontalement, verticalement ou en diagonale gagne.
    4. Si la grille est remplie et aucun joueur n'a aligné trois symboles, la partie est déclarée nulle.
    5. Les joueurs alternent les tours en plaçant leur symbole dans une case vide.
    6. Le jeu se termine dès qu'il y a un gagnant ou que la partie est nulle.

    Bonne chance et amusez-vous !
    """
    print(rules_text)

"""
fonction getInputUser:
elle permet à deux joueurs d'utiliser le clavier chacun à leur tour

"""
def getInputUser():
    global userOneInput
    global userTwoInput

    user_first=not user_first

    if user_first :
        userOneInput.append(input("Joueur 1 :"))
    else:
        userTwoInput.append(input("Joueur 2 :"))

def checkRow():
    
    for row in matrix:
        row_as_string = "".join(map(str, matrix[0]))
        if row_as_string in "XXX":
            return True
        if row_as_string in "OOO":
            return True
            
    return False

def checkCol():
    for row in range(3):
        cell=""
        for col in range(3):
            st=str(matrix[col][row])
            cell+=st   
        if cell in  "XXX" or cell in "OOO":
            return True
    return False

def checkDiagonal():
    pass

def checkWinner():
    win=False
    win=checkRow()
    win=checkCol()
    win=checkDiagonal()
    return win


def showMorpion():
    for cell in range(9) :
        if cell%3==0:
            pass


checkWinner()