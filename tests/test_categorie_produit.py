import pytest
import re
from classes.categorie_produit import CategorieProduit
from classes.produit import Produit
from classes.article import Article
from classes.prix import Prix


@pytest.mark.parametrize(
    'categorie', 'erreur', 'message_erreur',
    [
        (CategorieProduit(
            ['Electroménager'],
            {'coffee_maker':
             Produit('coffee_maker',
                     {'coffee_maker1': Article('France/Coffee+maker/0',
                                               Prix(30, 'EUR'),
                                               'France')})}),
         TypeError, "Le nom doit être une instance de str."),

        (CategorieProduit(
            'Electroménager',
            Produit(['coffee_maker'],
                    {'coffee_maker1': Article('France/Coffee+maker/0',
                                              Prix(30, 'EUR'),
                                              'France')})),
         TypeError, (
             "Les produits doivent être une instance de dictionnaire."
             )),

        (CategorieProduit(
            'Electroménager',
            {1: Produit('coffee_maker',
                        {'coffee_maker1': Article('France/Coffee+maker/0',
                                                  Prix(30, 'EUR'),
                                                  'France')})}),
         TypeError, (
             "Les clés du dictionnaire de produits doivent être une "
             "instance de str."
             )),

        (CategorieProduit(
            'Electroménager',
            {'coffee_maker':
             Article('France/Coffee+maker/0', Prix(30, 'EUR'), 'France')}),
         TypeError, "Le nom doit être une instance de str.")
     ]
)
def test_categorie_init_echec(categorie, erreur, message_erreur):
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        categorie
