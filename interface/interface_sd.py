import keyboard
import time
import os
import pickle
from interface.interface_admin import InterfaceAdmin
from classes.affichages_donnees import AffichageDonnees

etoiles = "***********************************************"
"****************************"


class InterfaceSd:
    def __init__(self, admin=False):
        self._admin = admin
        print(etoiles)
        print("Bienvenu sur l'iterface d'affichage")
        print(etoiles)
        self.main_menu()

    def __admint_plus(self):
        print("[a] Retour menu administrateur")

    def main_menu(self):
        time.sleep(0.5)
        print("Choix des variables d'affichage")
        print("[1] Indices Produit")
        print("[2] Indices Catégories")  # False
        print("[q] pour quitter")
        if self._admin:
            self.admint_plus()

        while True:

            if keyboard.is_pressed(1):
                self.type_affichage(var_af=True)

            if keyboard.is_pressed(2):
                self.type_affichage(var_af=False)

            if keyboard.is_pressed("q"):
                break

            if keyboard.is_pressed("a") and self._admin:
                InterfaceAdmin()

    def type_affichage(self, var_af):
        time.sleep(0.5)
        print("Type d'affichage")
        print("[1] Carte")
        print("[2] Histogramme")  # False
        print(" espace pour aller en arrière")
        print("[q] pour quitter")

        if self._admin:
            self.__admint_plus()

        while True:

            if keyboard.is_pressed(1):
                pass

            if keyboard.is_pressed(2):
                pass

            if keyboard.is_pressed("q"):
                break

            if keyboard.is_pressed("space"):
                self.main_menu()

            if keyboard.is_pressed("a") and self._admin:
                InterfaceAdmin()
