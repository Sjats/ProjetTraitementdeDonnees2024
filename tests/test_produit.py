import pytest
import re
from classes.produit import Produit
from classes.article import Article
from classes.prix import Prix


@pytest.mark.parametrize(
    'produit', 'erreur', 'message_erreur',
    [
        (Produit(['coffee_maker'], {'coffee_maker1':
                                    Article('France/Coffee+maker/0',
                                            Prix(30, 'EUR'),
                                            'France')}),
         TypeError, "Le nom doit être une instance de str."),

        (Produit('coffee_maker', Article('France/Coffee+maker/0',
                                         Prix(30, 'EUR'),
                                         'France')),
         TypeError, "Les articles doivent être une instance de dictionnaire."),

        (Produit(['coffee_maker'], {0: Article('France/Coffee+maker/0',
                                               Prix(30, 'EUR'),
                                               'France')}),
         TypeError, (
             "Les clés du dictionnaire d'articles doivent être une "
             "instance de str."
         )),

        (Produit(['coffee_maker'], {'coffee_maker1': Prix(30, 'EUR')}),
         TypeError, (
             "Les valeurs du dictionnaire d'articles doivent être une "
             "instance d'Article"
         )),

     ]
)
def test_produit_init_echec(produit, erreur, message_erreur):
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        produit
