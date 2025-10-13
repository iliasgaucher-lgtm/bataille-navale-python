# 🚢 Projet Bataille Navale

Un jeu de bataille navale simple en ligne de commande, développé en Python dans le cadre d'un projet d'étude.

---
## Prérequis

* Python 3.x
* Git

---
## Installation

Suivez ces étapes pour préparer le projet sur votre machine.

1.  **Clonez ce dépôt** :
    ```bash
    git clone <URL_DE_VOTRE_REPO_GITHUB>
    cd <NOM_DU_DOSSIER_DU_PROJET>
    ```

2.  **Créez et activez un environnement virtuel** :

    * Sur **Windows** :
        ```bash
        py -m venv venv
        .\venv\Scripts\activate
        ```
    * Sur **macOS / Linux** :
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Installez les dépendances** :
    ```bash
    pip install -r requirements.txt
    ```
    
---
## Lancement du Jeu

Pour démarrer une partie, exécutez la commande suivante depuis le dossier du projet :
```bash
python bataille_navale.py
```


---
## Lancement des Tests

Pour vérifier que le code fonctionne correctement, vous pouvez lancer les tests unitaires avec `pytest` :
```bash
pytest
```