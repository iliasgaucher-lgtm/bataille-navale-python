# main.py

import random
from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin

# --- Constantes du jeu ---
LIGNES = 8
COLONNES = 10
BATEAUX_A_PLACER = [PorteAvion, Croiseur, Torpilleur, SousMarin]
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
            # Ne devrait pas arriver avec une grille assez grande
            print(f"Attention: Impossible de placer un {classe_bateau.__name__}")
            
    return bateaux_places


def jeu():
    """Fonction principale du jeu."""
    
    # 1. Initialisation
    grille = Grille(LIGNES, COLONNES)
    grille_tirs_joueur = Grille(LIGNES, COLONNES) # Grille que le joueur voit
    
    liste_bateaux = placer_bateaux_aleatoirement(grille, BATEAUX_A_PLACER)
    
    if len(liste_bateaux) != len(BATEAUX_A_PLACER):
        print("Erreur lors du placement des bateaux. Relancez le jeu.")
        return

    # 2. Boucle de jeu
    nombre_coups = 0
    bateaux_coules = 0
    
    print("=== BATAILLE NAVALE ===")

    while bateaux_coules < len(liste_bateaux):
        print("\n" + "="*20)
        print(grille_tirs_joueur)
        print(f"Bateaux restants: {len(liste_bateaux) - bateaux_coules}")
        
        try:
            ligne = int(input(f"Entrez la ligne (0-{LIGNES-1}): "))
            colonne = int(input(f"Entrez la colonne (0-{COLONNES-1}): "))

            # 3. Gérer le tir
            case_touchee = grille.tirer(ligne, colonne, SYMBOLE_TOUCHE_BATEAU)
            
            if case_touchee is None:
                print("Tir hors de la grille. Essayez encore.")
                continue
            
            nombre_coups += 1
            
            # 4. Analyser le résultat du tir
            if case_touchee == Grille.VIDE:
                print("Raté ! (Plouf)")
                grille_tirs_joueur.tirer(ligne, colonne, Grille.TOUCHE)
                
            elif case_touchee in [Grille.TOUCHE, SYMBOLE_TOUCHE_BATEAU]:
                print("Vous avez déjà tiré ici...")
            
            else: # On a touché un bateau (ex: '🚢', '⛴', ...)
                print(f"Touché ! Vous avez touché un {case_touchee}")
                grille_tirs_joueur.tirer(ligne, colonne, SYMBOLE_TOUCHE_BATEAU)
                
                # 5. Vérifier si un bateau est coulé
                for bateau in liste_bateaux:
                    # On vérifie si ce bateau est sur la case touchée
                    if (ligne, colonne) in bateau.positions:
                        if bateau.coule(grille):
                            print(bateau.message_coule())
                            bateaux_coules += 1
                            # Révéler le bateau sur la grille du joueur
                            for l, c in bateau.positions:
                                grille_tirs_joueur.grille[grille_tirs_joueur._convertir_coords(l, c)] = bateau.marque
                            # On retire le bateau de la liste pour ne pas le revérifier
                            liste_bateaux.remove(bateau) 
                            
        except ValueError:
            print("Entrée invalide. Veuillez entrer des nombres.")
        except Exception as e:
            print(f"Une erreur est survenue: {e}")

    # 6. Fin du jeu
    print("\n" + "="*20)
    print("Bravo ! Vous avez coulé tous les navires !")
    print(f"Vous avez gagné en {nombre_coups} coups.")
    print("Voici la grille finale des tirs :")
    print(grille_tirs_joueur)


if __name__ == "__main__":
    jeu()