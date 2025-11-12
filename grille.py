# grille.py

class Grille:
    """
    Simule la grille de jeu en utilisant une liste 1D.
    """
    VIDE = '∿'
    TOUCHE = 'x'
    BATEAU = '⛵' # Marque par défaut, sera remplacée par les sous-classes

    def __init__(self, lignes, colonnes):
        self.lignes = lignes
        self.colonnes = colonnes
        self.grille = [self.VIDE] * (lignes * colonnes)

    def _index_valide(self, ligne, colonne):
        """Vérifie si les coordonnées sont dans la grille."""
        return 0 <= ligne < self.lignes and 0 <= colonne < self.colonnes

    def _convertir_coords(self, ligne, colonne):
        """Convertit (ligne, colonne) en index 1D."""
        return ligne * self.colonnes + colonne

    def ajoute(self, bateau):
        """
        Place un bateau sur la grille.
        Vérifie si le bateau rentre entièrement.
        """
        # 1. Vérifier si toutes les positions sont valides
        for ligne, colonne in bateau.positions:
            if not self._index_valide(ligne, colonne):
                return False # Le bateau dépasse
        
        # 2. (Bonus consigne : vérifier chevauchement)
        for ligne, colonne in bateau.positions:
            index = self._convertir_coords(ligne, colonne)
            if self.grille[index] != self.VIDE:
                return False # Il y a déjà un bateau
        
        # 3. Si tout est bon, placer le bateau
        for ligne, colonne in bateau.positions:
            index = self._convertir_coords(ligne, colonne)
            # Utilise la marque spécifique du bateau (ex: "🚢")
            self.grille[index] = bateau.marque
        
        return True

    def tirer(self, ligne, colonne, touche=TOUCHE):
        """
        Marque un tir sur la grille.
        Renvoie la valeur de la case *avant* le tir.
        """
        if not self._index_valide(ligne, colonne):
            return None # Tir hors grille

        index = self._convertir_coords(ligne, colonne)
        valeur_case = self.grille[index]
        
        # On ne marque "touché" que si c'est de l'eau ou un bateau
        if valeur_case != self.TOUCHE:
            self.grille[index] = touche
            
        return valeur_case

    def __str__(self):
        """Crée une représentation textuelle de la grille."""
        affichage = []
        for l in range(self.lignes):
            debut = l * self.colonnes
            fin = debut + self.colonnes
            # Ajoute les numéros de ligne pour l'affichage
            ligne_str = f"{l} " + " ".join(self.grille[debut:fin])
            affichage.append(ligne_str)
        
        # Ajoute les numéros de colonne
        colonnes_str = "  " + " ".join(str(c) for c in range(self.colonnes))
        affichage.insert(0, colonnes_str)
        
        return "\n".join(affichage)