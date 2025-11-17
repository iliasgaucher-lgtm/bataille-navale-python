from grille import Grille 

class Bateau:
    
    
    MARQUE = '⛵'
    LONGUEUR = 1 

    def __init__(self, ligne, colonne, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        
        
        self.longueur = self.LONGUEUR
        self.marque = self.MARQUE
        self.vertical = vertical

    @property
    def positions(self):
       
        pos = []
        for i in range(self.longueur):
            if self.vertical:
                pos.append((self.ligne + i, self.colonne))
            else:
                pos.append((self.ligne, self.colonne + i))
        return pos

    def coule(self, grille_solution, symbole_touche):
       
        for ligne, colonne in self.positions:
            valeur_case = grille_solution.obtenir_valeur(ligne, colonne)
            if valeur_case != symbole_touche:
                return False
        return True
    
    def message_coule(self):
        """Message par défaut si le bateau est coulé."""
        return "Un bateau a été coulé !"



class PorteAvion(Bateau):
    MARQUE = "🚢"
    LONGUEUR = 4 
    def message_coule(self):
        return "Vous avez coulé le Porte-Avion (4 cases) !"

class Croiseur(Bateau):
    MARQUE = "⛴"
    LONGUEUR = 3
    def message_coule(self):
        return "Vous avez coulé le Croiseur (3 cases) !"

class Torpilleur(Bateau):
    MARQUE = "🚣"
    LONGUEUR = 2
    def message_coule(self):
        return "Vous avez coulé le Torpilleur (2 cases) !"

class SousMarin(Bateau):
    MARQUE = "🐟"
    LONGUEUR = 2
    def message_coule(self):
        return "Vous avez coulé le Sous-Marin (2 cases) !"