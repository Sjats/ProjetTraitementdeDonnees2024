import keyboard
import os
from classes.affichages_donnees import AffichageDonnees
from classes.categorie_produit_corrige import bddinterfacecat as ind_cat_imp
from classes.produit_corrige import bddinterfaceprod as ind_prod_imp
import time

etoiles = "***********************************************"


class InterfaceSd:
    def __init__(self, admin=False):
        os.system('cls' if os.name == 'nt' else 'clear')
        self._admin = admin
        print(etoiles)
        print("Bienvenue sur l'interface d'affichage")
        print(etoiles)
        time.sleep(1.5)

        self.main_menu()

    def main_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Choix des variables d'affichage")
        print("[1] Indices Produit")
        print("[2] Indices Catégories")
        print("[q] pour quitter")
        while True:
            if keyboard.is_pressed("1"):
                self.type_affichage(var_af=True)
            if keyboard.is_pressed("2"):
                self.type_affichage(var_af=False)
            if keyboard.is_pressed("q"):
                print("Au revoir")
                break

    def type_affichage(self, var_af):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Chargement en cours...")
        afficheur = AffichageDonnees(ind_prod_imp(), ind_cat_imp())
        os.system('cls' if os.name == 'nt' else 'clear')
        print(etoiles)
        print("Type d'affichage")
        print("[1] Carte")
        print("[2] Histogramme")
        print("[espace] pour revenir au menu précédent")
        print("[q] pour quitter")
        while True:

            if keyboard.is_pressed("1"):
                afficheur.AfficherCarte(var_af)
                command = "streamlit run " + os.getcwd() + "/__main__.py"
                os.system(command)
                self.main_menu()
            if keyboard.is_pressed("2"):
                afficheur.plot_histogramme(var_af, self.main_menu)
                return  # Sortir de cette boucle
            if keyboard.is_pressed("q"):
                print("Au revoir")
                break
            if keyboard.is_pressed("space"):
                self.main_menu()
