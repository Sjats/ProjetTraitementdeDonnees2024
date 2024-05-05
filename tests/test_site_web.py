import pytest
import re
from classes.site_web import SiteWeb
from donnees import renseigement_sites_web


val_nom = renseigement_sites_web.configurations_sites.keys()


@pytest.mark.parametrize(
    'site_web', 'erreur', 'message_erreur',
    [
        (SiteWeb(['amazon']), TypeError, "nom est de type str"),

        (SiteWeb('carrefour'), ValueError, (
            "nom non valide, les noms valides"
            " sont " + str(val_nom)
        )),
     ]
)
def test_produit_init_echec(site_web, erreur, message_erreur):
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        site_web
