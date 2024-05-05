import pytest
import re
from classes.prix import Prix


@pytest.mark.parametrize(
    'prix', 'erreur', 'message_erreur',
    [
        (Prix(0.9308, 30), TypeError, "devise doit être de type str"),

        (Prix('USD', {'USD': 25}),
         TypeError, (
            "montant doit être de "
            "type float ou None"
        ))
     ]
)
def test_produit_init_echec(prix, erreur, message_erreur):
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        prix
