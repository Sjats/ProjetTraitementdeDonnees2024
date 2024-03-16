# ProjetTraitementdeDonnees2024

## Description
L'objectif de ce projet est de réaliser du web scraping sur plusieurs sites afin de créer une base de données sur les prix de différents produits. Ensuite, le projet se propose de traiter ces données et de visualiser les résultats à travers une interface graphique.

## Mise en Place
Pour installer les bibliothèques nécessaires à l'exécution, veuillez saisir la commande suivante dans votre terminal :
```bash
pip install -r requirements.txt
```

## Contribution

Pour mettre à jour le fichier requirements.txt, veuillez saisir :

```bash
pipreqs --savepath=requirements.in && pip-compile
```


Si le module pipreqs n'est pas installé, veuillez exécuter la commande suivante dans votre terminal : 
```bash
pip install pipreqs
pip install pip-tools
```