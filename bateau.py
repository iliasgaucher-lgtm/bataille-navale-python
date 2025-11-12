# bateau.py

class Bateau:
    """Classe de base pour un bateau."""
    
    MARQUE = '⛵' # Marque par défaut
    LONGUEUR = 1  # Longueur par défaut

    def __init__(self, ligne, colonne, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = self.LONGUEUR # Utilise la longueur de la classe
        self.marque = self.MARQUE     # Utilise la marque de la classe
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

    def coule(self, grille):
        """
        Vérifie si le bateau est coulé.
        Un bateau est coulé si toutes ses cases sur la grille sont 'x' ou '💣'.
        """
        from grille import Grille # Importation locale pour éviter boucle
        
        for ligne, colonne in self.positions:
            index = grille._convertir_coords(ligne, colonne)
            # Si une seule case n'est pas touchée, il n'est pas coulé
            if grille.grille[index] not in [Grille.TOUCHE, '💣']:
                return False
        return True
    
    def message_coule(self):
        """Message par défaut si le bateau est coulé."""
        return "Un bateau a été coulé !"

# --- Sous-classes pour chaque type de bateau ---

class PorteAvion(Bateau):
    MARQUE = "🚢"
    LONGUEUR = 4
    def message_coule(self):
        return "Vous avez coulé le Porte-Avion !"

class Croiseur(Bateau):
    MARQUE = "⛴"
    LONGUEUR = 3
    def message_coule(self):
        return "Vous avez coulé le Croiseur !"

class Torpilleur(Bateau):
    MARQUE = "🚣"
    LONGUEUR = 2
    def message_coule(self):
        return "Vous avez coulé le Torpilleur !"

class SousMarin(Bateau):
    MARQUE = "🐟"
    LONGUEUR = 2
    def message_coule(self):
        return "Vous avez coulé le Sous-Marin !"