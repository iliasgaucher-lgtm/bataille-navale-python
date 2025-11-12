# story_bateau.py
from bateau import Bateau

print("User Story: Chevauchement")

b1 = Bateau(1, 1, vertical=False)
b1.longueur = 3 # Positions: (1,1), (1,2), (1,3)

# Cas 1: Chevauchement
b2 = Bateau(1, 2, vertical=True)
b2.longueur = 3 # Positions: (1,2), (2,2), (3,2)

# On vérifie si une position de b1 est dans b2
pos_b1 = set(b1.positions)
pos_b2 = set(b2.positions)

intersection = pos_b1.intersection(pos_b2)
if intersection:
    print(f"Cas 1: Les bateaux se chevauchent en {intersection}")
else:
    print("Cas 1: Pas de chevauchement.")


# Cas 2: Pas de chevauchement
b3 = Bateau(5, 5)
pos_b3 = set(b3.positions)
intersection = pos_b1.intersection(pos_b3)

if intersection:
    print(f"Cas 2: Les bateaux se chevauchent en {intersection}")
else:
    print("Cas 2: Pas de chevauchement.")