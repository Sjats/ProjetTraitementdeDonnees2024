# ProjetTraitementdeDonnees2024

## Description
L'objectif de ce projet est de réaliser du web scraping sur plusieurs sites afin de créer une base de données sur les prix de différents produits. Ensuite, le projet se propose de traiter ces données et de visualiser les résultats à travers une interface graphique.

## Diagramme des Cas d'Utilisation

![Diagramme Cas d'Utilisation](https://github.com/Sjats/ProjetTraitementdeDonnees2024/blob/main/diagrammes/cas_utilisation.png)

## Diagramme des Classes

![Diagramme UML](https://github.com/Sjats/ProjetTraitementdeDonnees2024/blob/main/diagrammes/uml.png)

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

[def]: \ProjetTraitementdeDonnees2024\diagramme_uml\uml.png?raw=true "uml"