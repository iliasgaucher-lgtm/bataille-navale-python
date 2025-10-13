# test_bataille_navale.py

import pytest
from bataille_navale import creer_grille, placer_bateaux, TAILLE_GRILLE, SYMBOLE_EAU, SYMBOLE_BATEAU

def test_creer_grille():
    """Teste si la grille est créée avec les bonnes dimensions et le bon symbole."""
    grille = creer_grille(TAILLE_GRILLE)
    assert len(grille) == TAILLE_GRILLE
    assert len(grille[0]) == TAILLE_GRILLE
    assert grille[0][0] == SYMBOLE_EAU

def test_placer_bateaux():
    """Teste si le bon nombre de bateaux est placé sur la grille."""
    grille = creer_grille(TAILLE_GRILLE)
    nombre_bateaux_a_placer = 3
    grille_avec_bateaux = placer_bateaux(grille, nombre_bateaux_a_placer)

    compteur = 0
    for ligne in grille_avec_bateaux:
        for case in ligne:
            if case == SYMBOLE_BATEAU:
                compteur += 1

    assert compteur == nombre_bateaux_a_placer