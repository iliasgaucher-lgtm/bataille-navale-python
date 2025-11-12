# test_bateau.py

from bateau import Bateau, PorteAvion, Croiseur
from grille import Grille

def test_init_bateau_defaut():
    b = Bateau(2, 3)
    assert b.ligne == 2
    assert b.colonne == 3
    assert b.longueur == 1 # Par défaut
    assert b.vertical == False # Par défaut

def test_init_sous_classes():
    p = PorteAvion(1, 1)
    assert p.longueur == 4
    assert p.marque == "🚢"
    
    c = Croiseur(2, 2)
    assert c.longueur == 3
    assert c.marque == "⛴"

def test_positions_horizontal():
    b = Bateau(2, 3)
    b.longueur = 3
    attendu = [(2, 3), (2, 4), (2, 5)]
    assert b.positions == attendu

def test_positions_vertical():
    b = Bateau(2, 3, vertical=True)
    b.longueur = 3
    attendu = [(2, 3), (3, 3), (4, 3)]
    assert b.positions == attendu

def test_bateau_pas_coule():
    g = Grille(5, 5)
    b = Bateau(1, 1)
    b.longueur = 2
    g.ajoute(b) # Place '⛵' '⛵' en (1,1) et (1,2)
    
    g.tirer(1, 1) # Touche le bateau
    assert b.coule(g) == False # Pas encore coulé

def test_bateau_coule():
    g = Grille(5, 5)
    b = Bateau(1, 1)
    b.longueur = 2
    g.ajoute(b) # Place '⛵' '⛵' en (1,1) et (1,2)
    
    g.tirer(1, 1) # Touche le bateau
    g.tirer(1, 2) # Touche le bateau
    
    assert b.coule(g) == True