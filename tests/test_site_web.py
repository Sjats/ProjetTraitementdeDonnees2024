import pytest
import re
from classes.site_web import SiteWeb
import pickle

with open("donnees/rsw_data.pkl", "rb") as file:
    rsw = pickle.load(file)
val_nom = rsw.keys()


@pytest.mark.parametrize(
    'nom, erreur, message_erreur',
    [
        (['amazon'], TypeError, "nom est de type str"),

        ('carrefour', ValueError, (
            "nom non valide, les noms valides"
            " sont " + str(val_nom)
        )),
    ]
)
def test_produit_init_echec(nom, erreur, message_erreur):
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        SiteWeb(nom)


@pytest.mark.parametrize(
    "nom",
    [
        "amazon",
        "iherb"
    ]
)
def test_produit_init_succes(nom):
    SiteWeb(nom)


@pytest.mark.parametrize(
    "requetes, erreur, message_erreur",
    [
        ({"rice", "pasta", "pen"},
         TypeError,
         ("requetes est de type list")),
        (["rice", "pasta", {"pen"}],
         TypeError,
         "les elements de requetes sont de type str")
    ]
)
def test_produit_WebScrapping_echec(requetes, erreur, message_erreur):
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        amazon = SiteWeb("amazon")
        amazon.WebScrapping(requetes)


# @pytest.mark.parametrize(
#    "requetes",
#    [
#        ["rice"]
#    ]
# )
# def test_produit_WebScrapping_succes(requetes):
    # amazon = SiteWeb("amazon")
    # amazon.WebScrapping(requetes)
