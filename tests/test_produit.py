import pytest
import re
from classes.produit import Produit


@pytest.mark.parametrize(
    'nom, articles, erreur, message_erreur',
    [
        (['coffee_maker'], {"article1": pytest.article1},
         TypeError, "Le nom doit être une instance de str."),

        ('coffee_maker', pytest.article1,
         TypeError, "Les articles doivent être une instance de dictionnaire."),

        ('coffee_maker', {1: pytest.article1},
         TypeError, ("Les clés du dictionnaire d'articles doivent être une"
                     " instance de str.")
         ),

        ('coffee_maker', {'coffee_maker1': pytest.prix_euros},
         TypeError, (
             "Les valeurs du dictionnaire d'articles doivent être une "
             "instance d'Article"
         )),

     ]
)
def test_produit_init_echec(nom, articles, erreur, message_erreur):
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        Produit(nom, articles)


@pytest.mark.parametrize(
    'kwargs_str',
    [
        'bread_kwargs', 'coffe_maker_kwargs'
    ]
)
def test_station_init_succes(kwargs_str, request):
    kwargs = request.getfixturevalue(kwargs_str)
    prod = Produit(**kwargs)
    prod.Enregistrement_prod()
    prod.Enregistrement_ind()
