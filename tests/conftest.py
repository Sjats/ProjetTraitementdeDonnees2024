from classes.prix import Prix
from classes.article import Article
from classes.produit import Produit
from classes.categorie_produit import CategorieProduit

import pytest


# Prix

@pytest.fixture
def prix_euros_kwargs():
    return {"devise": "EUR",
            "montant": 30}


@pytest.fixture
def prix_dollars_kwargs():
    return {"devise": "USD",
            "montant": 37}


@pytest.fixture
def prix_none_kwargs():
    return {"devise": "EUR",
            "montant": None}


# Articles

@pytest.fixture
def article1_kwargs(prix_euros_kwargs):
    return {
          "id_article": 'France/Coffee+maker/0',
          "prix": Prix(**prix_euros_kwargs),
          "pays": 'France'
    }


@pytest.fixture
def article2_kwargs(prix_dollars_kwargs):
    return {
        "id_article": 'United States/Coffee+maker/1',
        "prix": Prix(**prix_dollars_kwargs),
        "pays": 'United States'
    }


@pytest.fixture
def article3_kwargs(prix_euros_kwargs):
    return {
        "id_article": 'Spain/Bread/2',
        "prix": Prix(**prix_euros_kwargs),
        "pays": 'Spain'
    }


@pytest.fixture
def article4_kwargs(prix_none_kwargs):
    return {
        "id_article": 'Japan/Coffee+maker/1',
        "prix": Prix(**prix_none_kwargs),
        "pays": 'Japan'
    }

# Produit


@pytest.fixture
def coffe_maker_kwargs(article1_kwargs, article2_kwargs):
    return {
        "nom": "Coffee+maker",
        "articles": {article1_kwargs["id_article"]: Article(**article1_kwargs),
                     article2_kwargs["id_article"]: Article(**article2_kwargs)
                     }

    }


@pytest.fixture
def bread_kwargs(article3_kwargs, article4_kwargs):
    return {
        "nom": "bread",
        "articles": {article3_kwargs["id_article"]: Article(**article3_kwargs),
                     article4_kwargs["id_article"]: Article(**article4_kwargs)
                     }
    }


# Stations
@pytest.fixture
def categorie_kwargs(coffe_maker_kwargs, bread_kwargs):
    return {
        "nom": "cat",
        "produits": {coffe_maker_kwargs._nom: Produit(**coffe_maker_kwargs),
                     bread_kwargs._nom: Produit(**bread_kwargs)}
    }

# Configuration globale


def pytest_configure():

    # Prix
    pytest.prix_euros = Prix(devise="EUR", montant=30)
    pytest.prix_dollars = Prix(devise="USD", montant=30)
    pytest.prix_none = Prix(devise="EUR", montant=None)

    # Articles
    pytest.article1 = Article(id_article='France/Coffee+maker/0',
                              prix=pytest.prix_euros,
                              pays='France')

    pytest.article2 = Article(id_article='United States/Coffee+maker/1',
                              prix=pytest.prix_dollars,
                              pays='United States')

    pytest.article3 = Article(id_article='Spain/Bread/2',
                              prix=pytest.prix_euros,
                              pays='Spain')

    pytest.article4 = Article(id_article='Japan/Coffee+maker/1',
                              prix=pytest.prix_none,
                              pays='Japan')

    # Produits
    pytest.coffe_maker = Produit(nom="Coffe+maker",
                                 articles={
                                     pytest.article1._id_article:
                                     pytest.article1,
                                     pytest.article2._id_article:
                                     pytest.article2,
                                     })

    pytest.bread = Produit(nom="bread",
                           articles={
                                     pytest.article3._id_article:
                                     pytest.article3,
                                     pytest.article4._id_article:
                                     pytest.article4,
                                     })

    # Categories Produits
    pytest.categorie = CategorieProduit(nom="cat",
                                        produits={
                                         pytest.bread._nom: pytest.bread,
                                         pytest.coffe_maker._nom:
                                         pytest.coffe_maker
                                        })
