import pytest
import re
from classes.prix import Prix


@pytest.mark.parametrize(
    'devise, montant, erreur, message_erreur',
    [
        (0.9308, 30, TypeError, "devise doit être de type str"),

        ('USD', {'USD': 25},
         TypeError, (
            "montant doit être de "
            "type float ou None"
        ))
     ]
)
def test_produit_init_echec(devise, montant, erreur, message_erreur):
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        Prix(devise, montant)


@pytest.mark.parametrize(
    'devise, montant',
    [
        ('USD', 30),
        ('EUR', 30),
        ("EUR", None)
     ]
)
def test_produit_init_succes(devise, montant):
    p = Prix(devise, montant)
    str(p)


@pytest.mark.parametrize(
    'devise, montant, offline',
    [
        ('USD', 30, True),
        ('USD', 30, False)
     ]
)
def test_produit_conversioneuros(devise, montant, offline):
    p = Prix(devise, montant)
    p._ConversionEuros(offline)
