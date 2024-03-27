# ProjetTraitementdeDonnees2024

## Description
L'objectif de ce projet est de réaliser du web scraping sur plusieurs sites afin de créer une base de données sur les prix de différents produits. Ensuite, le projet se propose de traiter ces données et de visualiser les résultats à travers une interface graphique.
## Organisation
```plantuml
@startuml
skinparam class {
    BackgroundColor LightGoldenRodYellow
    BorderColor black
}

class "Site Web" {
    # nom: str
    - url_recherche : list<str>
    - WebScrapping(nom_article: str): list<Article>
}

class "Interface Utilisateur" {
    + requete
    - AfficherCarte()
    - AfficherHistogramme()
    - AfficherGraphique()
}

class Article {
    # nom: str
    # prix: float
    # id_article: str
    # Pays : str
}

class Produit {
    # nom: str
    # articles: dict{str, article}
    # CalculIndicesProduit() : float
    + AjouteDonneesExterieures(Dict[str, Article]) 
}

class "Catégorie Produit" {
    # nom: str
    # produits: dict[str, Produit]
    # CalculIndicesCategorie() : float
}

class Pays {
    + nom : str
    + devise : str
    + IndcicesProduits : dict[str, float]
    + IndcicesCategorieProduit : dict[str, float]
    # ConversionEuros() : float
    - GetTauxdeChange(devise: str) : float
}

"Site Web" --* Article
Article --* Produit
Produit --* "Catégorie Produit"

Pays -- "Interface Utilisateur"
Pays-- "Catégorie Produit"
Pays -- Produit
@enduml
```
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