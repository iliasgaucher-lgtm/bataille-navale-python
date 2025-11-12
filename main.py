# main.py

import random
from grille import Grille
# On importe toutes nos classes de bateaux
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin

# --- Constantes du jeu ---
LIGNES = 4  # Modifié pour les tests
COLONNES = 5 # Modifié pour les tests
# On importe la classe Bateau de base (longueur 1) et Torpilleur (longueur 2)
from bateau import Bateau, Torpilleur 
BATEAUX_A_PLACER = [Bateau, Bateau, Torpilleur] # 2 bateaux de 1 case, 1 de 2 cases
SYMBOLE_TOUCHE_BATEAU = "💣"

def placer_bateaux_aleatoirement(grille, liste_classes_bateaux):
    """
    Place les bateaux sur la grille.
    Gère les placements aléatoires et les non-chevauchements.
    """
    bateaux_places = []
    
    for classe_bateau in liste_classes_bateaux:
        place = False
        tentatives = 0
        
        # Tente de placer le bateau 100 fois
        while not place and tentatives < 100:
            ligne = random.randint(0, grille.lignes - 1)
            colonne = random.randint(0, grille.colonnes - 1)
            vertical = random.choice([True, False])
            
            bateau = classe_bateau(ligne, colonne, vertical)
            
            if grille.ajoute(bateau):
                bateaux_places.append(bateau)
                place = True
            
            tentatives += 1
            
        if not place:
            print(f"Attention: Impossible de placer un {classe_bateau.__name__}")
            
    return bateaux_places


def jeu():
    """Fonction principale du jeu."""
    
    # 1. Initialisation
    # grille_solution contient les VRAIS bateaux
    grille_solution = Grille(LIGNES, COLONNES) 
    # grille_tirs_joueur est ce que le joueur voit (ses 'x' et '💣')
    grille_tirs_joueur = Grille(LIGNES, COLONNES) 
    
    liste_bateaux_actifs = placer_bateaux_aleatoirement(grille_solution, BATEAUX_A_PLACER)
    nombre_total_bateaux = len(liste_bateaux_actifs)
    
    if nombre_total_bateaux != len(BATEAUX_A_PLACER):
        print("Erreur lors du placement des bateaux. Relancez le jeu.")
        return

    # 2. Boucle de jeu
    nombre_coups = 0
    bateaux_coules_count = 0
    
    print("=== BATAILLE NAVALE ===")

    while bateaux_coules_count < nombre_total_bateaux:
        print("\n" + "="*20)
        print(grille_tirs_joueur)
        print(f"Bateaux restants: {nombre_total_bateaux - bateaux_coules_count}")
        
        try:
            ligne_str = input(f"Entrez la ligne (0-{LIGNES-1}): ")
            colonne_str = input(f"Entrez la colonne (0-{COLONNES-1}): ")
            
            # Permet de quitter proprement
            if ligne_str == 'q' or colonne_str == 'q':
                print("Partie abandonnée.")
                break
                
            ligne = int(ligne_str)
            colonne = int(colonne_str)

            # 3. Vérifier la validité du tir
            if not grille_tirs_joueur._index_valide(ligne, colonne):
                 print("Tir hors de la grille. Essayez encore.")
                 continue
            
            # Vérifier si on a déjà tiré ici (sur la GRILLE JOUEUR)
            case_joueur = grille_tirs_joueur.obtenir_valeur(ligne, colonne)
            if case_joueur != Grille.VIDE:
                print("Vous avez déjà tiré ici. Essayez encore.")
                continue

            # 4. Le tir est valide, on compte le coup
            nombre_coups += 1
            
            # 5. Analyser le résultat (sur la GRILLE SOLUTION)
            case_solution = grille_solution.obtenir_valeur(ligne, colonne)

            if case_solution == Grille.VIDE:
                print("Raté ! (Plouf)")
                grille_tirs_joueur.placer_valeur(ligne, colonne, Grille.TOUCHE)
                
            else: # On a touché un bateau (n'importe quel symbole '🚢', '🐟', etc.)
                print(f"Touché ! Vous avez touché un {case_solution} !")
                
                # Mettre à jour les DEUX grilles
                grille_tirs_joueur.placer_valeur(ligne, colonne, SYMBOLE_TOUCHE_BATEAU)
                grille_solution.placer_valeur(ligne, colonne, SYMBOLE_TOUCHE_BATEAU) # Important pour la func 'coule'

                # 6. Vérifier si ce tir a coulé un bateau
                bateau_touche = None
                for b in liste_bateaux_actifs:
                    if (ligne, colonne) in b.positions:
                        bateau_touche = b
                        break
                
                # On vérifie si le bateau est bien coulé
                if bateau_touche and bateau_touche.coule(grille_solution, SYMBOLE_TOUCHE_BATEAU):
                    print(bateau_touche.message_coule())
                    bateaux_coules_count += 1
                    
                    # Révéler le bateau sur la grille du joueur
                    for l, c in bateau_touche.positions:
                        grille_tirs_joueur.placer_valeur(l, c, bateau_touche.marque)
                    
                    # On le retire de la liste pour ne pas le re-vérifier
                    liste_bateaux_actifs.remove(bateau_touche)

        except ValueError:
            print("Entrée invalide. Veuillez entrer des nombres.")
        except Exception as e:
            print(f"Une erreur est survenue: {e}")
            
    # 6. Fin du jeu
    if bateaux_coules_count == nombre_total_bateaux:
        print("\n" + "="*20)
        print("Bravo ! Vous avez coulé tous les navires !")
        print(f"Vous avez gagné en {nombre_coups} coups.")
        print("Voici la grille finale des tirs :")
        print(grille_tirs_joueur)


# Lancement du jeu principal
if __name__ == "__main__":
    jeu()