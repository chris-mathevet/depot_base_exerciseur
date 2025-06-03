# Configurations

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

Pour prévisualiser, vous pouvez générer les fichiers html qui seront présent sur la plateforme (Pas de tentatives possible).

Pour cela, créer un environement virtuelle python en 3.7 et activer le

```
  virtualenv -p python3.7 venv
  source venv/bin/activate
```

Ensuite installer les dépendances depuis la venv

```
  pip install -r requirements.txt
```

Et compiler avec make 

```
  make html
```

Ensuite vos documentations seront dans build/html et vous pourrez les parcourirs depuis le fichier index.html