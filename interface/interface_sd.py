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
    
    def main_menu(self):
        time.sleep(0.5)
        print("Choix des variables d'affichage")
        print("[1] Indices Produit") 
        print("[2] Indices Catégories") #False
        print("[q] pour quitter")
        if self._admin:
            self.admint_plus()

        while True:

            if keyboard.is_pressed(1):
                pass

            if keyboard.is_pressed(2):
                pass
                    


