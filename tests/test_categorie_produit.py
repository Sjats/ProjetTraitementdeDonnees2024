import pytest
import re
from classes.categorie_produit import CategorieProduit


@pytest.mark.parametrize(
    'kwargs, erreur, message_erreur',
    [
        ({"nom": ["electromenager"]},
         TypeError, "Le nom doit être une instance de str."),

        ({"produits": [pytest.bread, pytest.coffe_maker]},
         TypeError, (
             "Les produits doivent être une instance de dictionnaire."
             )),

        ({"produits": {1: pytest.bread, 2: pytest.coffe_maker}},
         TypeError, (
             "Les clés du dictionnaire de produits doivent être une "
             "instance de str."
             )),
     ]
)
def test_categorie_init_echec(categorie_kwargs, kwargs,
                              erreur, message_erreur):
    categorie_kwargs.update(kwargs)
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        CategorieProduit(**categorie_kwargs)


@pytest.mark.parametrize(
    "kwargs_str",
    [

        "categorie_kwargs"
    ]
)
def test_categorie_init_succes(kwargs_str, request):
    kwargs = request.getfixturevalue(kwargs_str)
    CategorieProduit(**kwargs)
