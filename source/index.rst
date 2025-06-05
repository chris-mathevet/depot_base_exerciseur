.. EasySphinx documentation master file, created by
   sphinx-quickstart on Thu Oct 20 12:10:31 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Titre
================================

Sous-titre
----------

Sous-sous-titre
~~~~~~~~~~~~~~~

Autre niveau
^^^^^^^^^^^^^

Potentiel description

.. toctree::
   :maxdepth: 2
   :numbered: 2
   :glob:
   :caption: Exercices fait avec Jacadi (python), 1 exercice par feuille
   
   1_Jacadi_solo/index*

.. toctree::
   :maxdepth: 1
   :numbered: 0
   :glob:
   :caption: Exercices fait avec Jacadi (python), plusieurs exercices par feuille
   
   2_Jacadi_multi/index*

.. toctree::
   :maxdepth: 1
   :numbered: 0
   :glob:
   :caption: Exercice fait avec Dockerfile
   
   3_Dockerfile/*

.. toctree::
   :maxdepth: 1
   :numbered: 0
   :glob:
   :caption: Exercice fait avec Démon Python (python)
   
   4_DemonPython/*

.. toctree::
   :maxdepth: 1
   :numbered: 0
   :glob:
   :caption: Exercice fait avec Package Python (python)
   
   5_PackagePython/*


.. toctree::
   :maxdepth: 1
   :numbered: 0
   :glob:
   :caption: Exercice fait avec Tests Python (python)
   
   6_TestsPython/*

.. toctree::
   :maxdepth: 1
   :numbered: 0
   :glob:
   :caption: Exercice fait avec java
   
   7_Java/*