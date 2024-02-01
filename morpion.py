userfirst=False
userOneInput=[]
userTwoInput=[]
PICT_X="XXX"
PICT_O="OOO"
matrix = [["O", "O", "O"], ["4", "X", "6"],  ["X", "8", "9"]]

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
    for i in range(3):
        row_as_string = "".join(map(str, matrix[i]))
        if row_as_string in (PICT_X + PICT_O):
            return True     
    return False

def checkCol():
    for row in range(3):
        car=""
        for col in range(3):
            car+=str(matrix[col][row])
        if car in ( PICT_X + PICT_O):
            return True
    return False

def verifyScheme(pattern):
    car=""
    for cell in pattern:        
        car+=str(matrix[cell[0]][cell[1]])
    
    if car in ( PICT_X + PICT_O):
        return True
    
    return False

def checkDiagonal():
    pattern1=[[0,0],[1,1],[2,2]]
    pattern2=[[0,2],[1,1],[2,0]]
            
    if verifyScheme(pattern1):
        return True
    elif verifyScheme(pattern2):
        return True
    
    return False

def checkWinner():
    
    if checkRow():
        return True
    elif checkCol():
        return True
    elif checkDiagonal():
        return True
    return False


def showMorpion():
    for cell in range(9) :
        if cell%3==0:
            pass

print(checkWinner())

