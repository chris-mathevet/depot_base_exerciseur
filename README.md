# Configurations

Tous vos fichiers vont se trouver dans le répertoire source, sauf le fichier de configuration readthedocs.yaml et votre requirements.txt.

## .readthedocs.yaml

Ce fichier sera utilisé par l'application readthedocs afin d'établir les configurations de base, comme quelle version de python, le chemin des requirements et du conf.py.

## source/conf.py

Ce fichier contient les informations générales du projet que vous allez créer, vous devrez y rentrer son nom, vos nom/prénoms et d'autres informations.

Voici les différentes lignes à changer : 

- 22-24
Pour les copyright et author, si plusieurs personnes, séparez par une virgule et un espace.

- 110
- 137,138
- 147,148
- 158-160

# Génerer la documentation en local

Pour prévisualiser, vous pouvez générer les fichiers HTML qui seront présents sur la plateforme (Pas de tentatives possibles).

Pour cela, créer un environnement virtuel Python en 3.7 et activer le.

```
  virtualenv -p python3.7 venv
  source venv/bin/activate
```

Ensuite installer les dépendances depuis la venv.

```
  pip install -r requirements.txt
```

Et compiler avec make.

```
  make html
```

Ensuite vos documentations seront dans build/html et vous pourrez les parcourir depuis le fichier index.html.

# Explications des fichiers .rst

Tout d'abord, dans le fichier index.rst, vous pourrez voir les différentes tailles de textes disponibles (En fonction du symbole situé en dessous. Le nombre de symboles doit être égal ou supérieur au nombre de lettres situées au-dessus).

Ensuite vous pouvez voir comment créer une table des matières.

```
.. toctree::              -> Démarer une table des matières
   :maxdepth: 1           -> Niveau de titre maximal affiché
   :numbered: 0           -> Nombre de niveau qui devrait être numérotés
   :glob:                 -> Permet la jointure automatique d'autres fichiers .rst
   :caption: Exercices    -> Titre de la table des matières

   1_Jacadi_solo/index*   -> gràce au :glob: permet d'inclure au niveau inférieur les fichiers index se trouvant dans "1_Jacadi_solo/" (Titres de niveau 2)
```

Vous pouvez mettre plusieurs tables des matières dans un même fichier, comme montré dans le fichier index.rst à la racine du répertoire source.