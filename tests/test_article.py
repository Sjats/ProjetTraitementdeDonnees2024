import pytest
import re
from classes.article import Article
from classes.prix import Prix


@pytest.mark.parametrize(
    'id_article, prix, pays, erreur, message_erreur',
    [
        ({'Pays': 'France', 'Nom': 'Coffee+maker', 'Numéro': 0},
         Prix("EUR", 30),
         'France',
         TypeError, "id_article doit être de type str"),

        ('France/Coffee+maker/0',
         30,
         'France',
         TypeError, "prix doit être de type Prix"),

        ('France/Coffee+maker/0',
         Prix('EUR', 30),
         ['France'],
         TypeError, "pays doit être de type str"),
     ]
)
def test_produit_init_echec(id_article, prix, pays, erreur, message_erreur):
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        Article(id_article, prix, pays)


@pytest.mark.parametrize(
    'id_article, prix, pays',
    [
        ('France/Coffee+maker/0',
         Prix("EUR", 30),
         'France')

     ]
)
def test_produit_init_succes(id_article, prix, pays):
    art = Article(id_article, prix, pays)
    str(art)
