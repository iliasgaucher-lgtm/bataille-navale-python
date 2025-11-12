# story_grille.py
from grille import Grille

print("User Story: Plouf dans l'eau")
g = Grille(5, 8)

while True:
    print("\n" + str(g))
    try:
        x = int(input("Entrez la ligne (ou 'q' pour quitter): "))
        y = int(input("Entrez la colonne (ou 'q' pour quitter): "))
        g.tirer(x, y)
    except ValueError:
        print("Fin de la story.")
        break