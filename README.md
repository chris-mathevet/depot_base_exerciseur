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

# index.rst

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

Il vous faudra un index.rst pour chaque niveau de votre table des matières, dans leur répertoire correspondant.

# Exercices

Pour chaque exercice, vous avez besoin : 
- Un répertoire avec les fichiers nécessaires pour l'exercice (Code Python et autres fichiers de configurations)
- Un fichier rst pour dire à Sphinx comment créer votre exercice

Par convention, je vous conseille que le nom du répertoire et du fichier soit le même.

## Contenu du répertoire 

Veuillez vous référer à la documentation du module docker-exerciseur présente ici: https://gitlab.com/FlorentBecker2/docker-exerciseur/-/blob/master/doc/Manuel.md?ref_type=heads


## Fichier .rst

```
.. easypython:: ./exo1/        -> Chemin relatif vers le répertoire contenant les fichiers de configurations
   :language: Jacadi           -> Langage de l'exercice (Voir documentation exerciseur)
   :titre: Exercice 1          -> Titre de l'exercice
   :extra_yaml:                -> Précision des fichiers de configurations se trouvant dans le répertoire, différent pour chanque langage (Voir documentation exerciseur)
     fichier_ens: exo1.py      -> Ici, fichier_ens pour Jacadi, fichier de la fonction de solution avec entrées visibles et invisibles

```


# Plusieurs exercices par feuilles

Comme démontré dans l'exemple des exercices du 2_Jacadi_multi, au lieu d'avoir exercice par exercice, l'on peut configurer pour avoir des feuilles avec plusieurs exercices.

Les fichiers des exercices en soi ne vont pas changer, mais c'est le fichier index.rst du dessus qui va changer.

Il sera différent des fichiers index.rst précédemment écrits.
Au lieu d'avoir un doctree, nous allons inclure les fichiers rst des exercices.

```
.. include::  Exercices1/exo1.rst    -> Inclu le fichier rst de ce chemin relatif
.. include::  Exercices1/exo2.rst
```

Le résultat sera comme s'il n'y avait qu'un fichier rst pour tous les exercices.