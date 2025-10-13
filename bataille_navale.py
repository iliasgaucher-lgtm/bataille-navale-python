# bataille_navale.py

import random

TAILLE_GRILLE = 5
SYMBOLE_EAU = "~"
SYMBOLE_BATEAU = "B"
SYMBOLE_TOUCHE = "X"
SYMBOLE_RATE = "O"

def creer_grille(taille):
    """Crée une grille vide (remplie d'eau)."""
    return [[SYMBOLE_EAU for _ in range(taille)] for _ in range(taille)]

def afficher_grille(grille, pour_joueur=False):
    """Affiche la grille de jeu."""
    print("  " + " ".join(str(i) for i in range(len(grille))))
    for i, ligne in enumerate(grille):
        ligne_affichee = ligne[:] # Copie de la ligne
        if pour_joueur:
            # Cache les bateaux non touchés
            ligne_affichee = [SYMBOLE_EAU if c == SYMBOLE_BATEAU else c for c in ligne_affichee]
        print(f"{i} {' '.join(ligne_affichee)}")

# Section principale pour tester
if __name__ == "__main__":
    grille_jeu = creer_grille(TAILLE_GRILLE)
    print("--- Grille de l'ordinateur (solution) ---")
    afficher_grille(grille_jeu)
    print("\n--- Grille du joueur ---")
    afficher_grille(grille_jeu, pour_joueur=True)


# bataille_navale.py (version mise à jour)

import random

TAILLE_GRILLE = 5
NOMBRE_BATEAUX = 3
SYMBOLE_EAU = "~"
SYMBOLE_BATEAU = "B"
SYMBOLE_TOUCHE = "X"
SYMBOLE_RATE = "O"

def creer_grille(taille):
    """Crée une grille vide (remplie d'eau)."""
    return [[SYMBOLE_EAU for _ in range(taille)] for _ in range(taille)]

def placer_bateaux(grille, nombre):
    """Place un certain nombre de bateaux aléatoirement sur la grille."""
    for _ in range(nombre):
        x, y = random.randint(0, len(grille)-1), random.randint(0, len(grille)-1)
        # Assure qu'on ne place pas un bateau sur un autre
        while grille[x][y] == SYMBOLE_BATEAU:
            x, y = random.randint(0, len(grille)-1), random.randint(0, len(grille)-1)
        grille[x][y] = SYMBOLE_BATEAU
    return grille

def afficher_grille(grille, pour_joueur=False):
    """Affiche la grille de jeu."""
    print("  " + " ".join(str(i) for i in range(len(grille))))
    for i, ligne in enumerate(grille):
        ligne_affichee = ligne[:]
        if pour_joueur:
            ligne_affichee = [c if c in [SYMBOLE_TOUCHE, SYMBOLE_RATE] else SYMBOLE_EAU for c in ligne_affichee]
        print(f"{i} {' '.join(ligne_affichee)}")

def jeu():
    """Fonction principale du jeu."""
    grille_solution = creer_grille(TAILLE_GRILLE)
    placer_bateaux(grille_solution, NOMBRE_BATEAUX)

    grille_joueur = creer_grille(TAILLE_GRILLE)

    bateaux_touches = 0
    tours = 0

    print("=== BATAILLE NAVALE ===")

    while bateaux_touches < NOMBRE_BATEAUX:
        print("\n" + "="*20)
        afficher_grille(grille_joueur, pour_joueur=True)

        try:
            tir_x = int(input(f"Entrez la ligne (0-{TAILLE_GRILLE-1}): "))
            tir_y = int(input(f"Entrez la colonne (0-{TAILLE_GRILLE-1}): "))

            if not (0 <= tir_x < TAILLE_GRILLE and 0 <= tir_y < TAILLE_GRILLE):
                print("Coordonnées hors de la grille. Essayez encore.")
                continue

            if grille_joueur[tir_x][tir_y] in [SYMBOLE_TOUCHE, SYMBOLE_RATE]:
                print("Vous avez déjà tiré ici. Essayez encore.")
                continue

            tours += 1
            if grille_solution[tir_x][tir_y] == SYMBOLE_BATEAU:
                print("Touché !")
                grille_joueur[tir_x][tir_y] = SYMBOLE_TOUCHE
                bateaux_touches += 1
            else:
                print("Raté !")
                grille_joueur[tir_x][tir_y] = SYMBOLE_RATE

        except ValueError:
            print("Entrée invalide. Veuillez entrer des nombres.")

    print(f"\nBravo ! Vous avez coulé tous les navires en {tours} tours.")
    print("--- Grille solution ---")
    afficher_grille(grille_solution)

if __name__ == "__main__":
    jeu()