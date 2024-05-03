import keyboard
import time
import os
# import pickle
from classes.affichages_donnees import AffichageDonnees
from classes.categorie_produit_corrige import bddinterfacecat as ind_cat_imp
from classes.produit_corrige import bddinterfaceprod as ind_prod_imp

etoiles = "***********************************************"
"****************************"


class InterfaceSd:
    def __init__(self, admin=False):
        self._admin = admin
        print(etoiles)
        print("Bienvenu sur l'iterface d'affichage")
        print(etoiles)
        self.main_menu()

    def main_menu(self):
        time.sleep(0.5)
        print("Choix des variables d'affichage")
        print("[1] Indices Produit")
        print("[2] Indices Catégories")  # False
        print("[q] pour quitter")
        os.system("cd classes")
        while True:

            if keyboard.is_pressed("1"):
                self.type_affichage(var_af=True)

            if keyboard.is_pressed("2"):
                self.type_affichage(var_af=False)

            if keyboard.is_pressed("q"):
                break

    def type_affichage(self, var_af):
        afficheur = AffichageDonnees(ind_prod_imp(), ind_cat_imp())
        time.sleep(0.1)
        print(etoiles)
        print("Type d'affichage")
        print("[1] Carte")
        print("[2] Histogramme")  # False
        print(" espace pour aller en arrière")
        print("[q] pour quitter")

        # with open("donnees/base_indice_produit.pkl", "rb") as file:
        #    prod_data = pickle.load(file)

        # with open("donnees/base_indice_categorie.pkl", "rb") as file:
        #    cat_data = pickle.load(file)

        

        while True:

            if keyboard.is_pressed("1"):
                afficheur.AfficherCarte(var_af)
                os.system("streamlit run c:/Users/Sunifred/Documents/GitHub/ProjetTraitementdeDonnees2024/__main__.py")  # mettre commande execution carte

            if keyboard.is_pressed("2"):
                afficheur.plot_histogramme(var_af)

            if keyboard.is_pressed("q"):
                break

            if keyboard.is_pressed("space"):
                self.main_menu()
