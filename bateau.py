# bateau.py

# On importe Grille ici pour la vérification "coule"
from grille import Grille

class Bateau:
    """Classe de base pour un bateau."""
    
    # Valeurs par défaut pour la classe de base
    MARQUE = 'B'
    LONGUEUR = 1

    def __init__(self, ligne, colonne, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        # self.LONGUEUR et self.MARQUE seront pris 
        # de la sous-classe (ex: PorteAvion)
        self.longueur = self.LONGUEUR
        self.marque = self.MARQUE
        self.vertical = vertical

    @property
    def positions(self):
        """
        Renvoie la liste des (ligne, colonne) occupées par le bateau.
        """
        pos = []
        for i in range(self.longueur):
            if self.vertical:
                pos.append((self.ligne + i, self.colonne))
            else:
                pos.append((self.ligne, self.colonne + i))
        return pos

    def coule(self, grille_solution):
        """
        Vérifie si le bateau est coulé.
        Un bateau est coulé si toutes ses cases sur la grille 
        solution sont 'x' ou '💣'.
        """
        # On vérifie la grille solution (pas la grille du joueur)
        for ligne, colonne in self.positions:
            index = grille_solution._convertir_coords(ligne, colonne)
            case_actuelle = grille_solution.grille[index]
            
            # Si une seule case n'EST PAS un symbole de tir,
            # alors le bateau n'est pas coulé.
            if case_actuelle not in [Grille.TOUCHE, '💣']:
                return False
        
        # Si on sort de la boucle, c'est que toutes les cases
        # ont été touchées.
        return True
    
    def message_coule(self):
        """Message par défaut si le bateau est coulé."""
        return "Un bateau a été coulé !"

# --- Sous-classes pour chaque type de bateau ---
# Chaque classe DOIT définir sa propre LONGUEUR et MARQUE.

class PorteAvion(Bateau):
    MARQUE = "P"
    LONGUEUR = 4
    def message_coule(self):
        return "Vous avez coulé le Porte-Avion (4 cases) !"

class Croiseur(Bateau):
    MARQUE = "C"
    LONGUEUR = 3
    def message_coule(self):
        return "Vous avez coulé le Croiseur (3 cases) !"

class Torpilleur(Bateau):
    MARQUE = "T"
    LONGUEUR = 2
    def message_coule(self):
        return "Vous avez coulé le Torpilleur (2 cases) !"

class SousMarin(Bateau):
    MARQUE = "🐟"
    LONGUEUR = 2
    def message_coule(self):
        return "Vous avez coulé le Sous-Marin (2 cases) !"