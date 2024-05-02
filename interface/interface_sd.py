import keyboard
import time
import os
import pickle
from interface_admin import InterfaceAdmin

etoiles = "***********************************************"
"****************************"


class InterfaceSd:
    def __init__(self, admin=False):
        self._admin = admin
        print(etoiles)
        print("Bienvenu sur l'iterface d'affichage")
        print(etoiles)
        self.main_menu()

    def admint_plus(self):
        print("[a] Retour menu administrateur")
