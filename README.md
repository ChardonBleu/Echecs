# Gestion de tournois d'échec

Projet 4 de la formation DA python d'Openclassrooms.

Application permettant la gestion de tournois d'échecs( joueurs , rounds et matchs, scores)

Menu:

    1. Charger tournoi passé
        1. Charger dernier tournoi sauvegardé et affiche les données
        2. Charger un tournoi à partir de son id_bdd et affiche les données
        3. Retour

    2. Créer nouveau tournoi
        1. Effacer joueurs et tournoi du tournoi courant
        2. Ajouter joueurs
            1. Charger 8 joueurs à partir de leur id_bdd
            2. Entrer manuellement 8 nouveaux joueurs puis les sauvegarder
            3. Retour
        3. Créer nouveau tournoi
        4. Retour

    3. Rapports tournoi
        1. Afficher liste simple de tous les tournois
        2. Afficher liste de tous les tournois avec rounds et matchs
        3. Afficher liste de tous les tours et match du tournoi courant
        4. Retour

    4. Gérer tournoi
        1. Démarer premier round (tri, affectation matchs, affichage)
        2. Terminer round en cours (saisie scores, tri,  affichages résultats)
        3. Round suivant (tri, affectation matchs, affichage)
        4. Sauvegarder tournoi
        5. Retour

    5. Gérer joueurs:
        1. Mettre à jour classement ELO joueurs et sauvegarder dans bdd
        2. Afficher tous les joueurs
            1. par ordre alphabétique
            2. par clasement
            3. Retour
        3. Afficher joueurs du tournoi courant
            1. par ordre alphabétique
            2. par classement
            3. Retour
        4. Retour

    6. Quitter

Installation
---
Télécharger les dossier et fichier et les copier dans un dossier de votre choix
Dans la console aller dans ce dossier choisi.

Environnement virtuel
---
https://docs.python.org/fr/3/library/venv.html?highlight=venv

Créer un environnement virtuel: 

```bash
python -m venv env
```

Activer cet environnement virtuel:
sur windows dans Visual Studio Code: 
```bash 
. env/Scripts/activate 
```
sur mac ou linux: 
```bash 
source env/bin/activate 
```
Packages
---

Puis installer les modules necessaires:
```bash 
python -m pip -r requirements.txt
```

Exécution
---
Se mettre dans le répertoire contenant le dossier application et taper dans la console:

```bash 
python -m application
```

Générer un rapport flake-8 html
---

Se mettre dans le répertoire application
Dans la console excécuter:
```bash 
flake8 --format=html --htmldir=flake-report
```
Un nouveau rapport flake8 est généré. aller dans le répertoire flake-report et ouvrir le fichier index.html dans un navigateur web.

Ressources utilisées
---

Livres:
    Apprenez à programmer en Python - Vincent Le Goff - Eyrolles
    Python crash courses - Eric Matthes - no starch press

Ressources web:

    Write Maintainable Pyhton Code - Daniel Timms

    https://openclassrooms.com/fr/courses/6900866-write-maintainable-python-code

    Webinaires MVC jeu du Pendu parties 1 et 2 - Thierry Chappuis

    https://www.notion.so/Webinaires-Pythonclassmates-Cafes-Zoom-8223a18f53a8457d94d96887c326c652


Remerciements
---

Un très grand merci à Aurélien Massé et à Thierry Chappuis pour tous leurs précieux conseils et retours,
et à tous les apprenants du Discord DA Pyhton.

http://discord.pythonclassmates.org/