# test_grille.py

from grille import Grille
from bateau import Bateau, Torpilleur

def test_init_grille():
    g = Grille(5, 8)
    assert g.lignes == 5
    assert g.colonnes == 8
    assert len(g.grille) == 40
    assert g.grille[0] == Grille.VIDE

def test_tirer_dans_grille():
    g = Grille(5, 8)
    g.tirer(2, 3)
    index = 2 * 8 + 3
    assert g.grille[index] == Grille.TOUCHE
    
    # Tirer à nouveau au même endroit
    g.tirer(2, 3)
    assert g.grille[index] == Grille.TOUCHE

def test_str_grille():
    g = Grille(2, 3)
    g.tirer(0, 1)
    # On attend les numéros de ligne/colonne
    attendu = "  0 1 2\n0 ∿ x ∿\n1 ∿ ∿ ∿"
    assert str(g) == attendu

def test_ajoute_bateau():
    g = Grille(2, 3)
    b = Bateau(1, 0)
    b.longueur = 2
    
    assert g.ajoute(b) == True
    # Teste si la grille a été modifiée
    # Grille 1D: [∿, ∿, ∿, ⛵, ⛵, ∿]
    assert g.grille[3] == Bateau.MARQUE
    assert g.grille[4] == Bateau.MARQUE
    assert g.grille[5] == Grille.VIDE

def test_ajoute_bateau_hors_limites():
    g = Grille(2, 3)
    # Dépasse horizontalement
    b_horiz = Bateau(0, 2, vertical=False)
    b_horiz.longueur = 2
    assert g.ajoute(b_horiz) == False
    
    # Dépasse verticalement
    b_vert = Bateau(1, 0, vertical=True)
    b_vert.longueur = 2
    assert g.ajoute(b_vert) == False

def test_ajoute_bateau_avec_marque_specifique():
    g = Grille(5, 5)
    torp = Torpilleur(1, 1) # Marque "🚣"
    assert g.ajoute(torp) == True
    index = 1 * 5 + 1
    assert g.grille[index] == Torpilleur.MARQUE