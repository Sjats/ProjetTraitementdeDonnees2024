import keyboard
import os
from classes.affichages_donnee import AffichageDonnees
import time
import pickle

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

        with open("donnees/bdd_indice_cat.pkl", "rb") as file:
            ind_cat = pickle.load(file)

        with open("donnees/bdd_indice_prod.pkl", "rb") as file:
            ind_prod = pickle.load(file)
        afficheur = AffichageDonnees(ind_prod, ind_cat)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(etoiles)
        time.sleep(0.25)
        print("Type d'affichage")
        print("[1] Carte")
        print("[2] Histogramme")
        print("[espace] pour revenir au menu précédent")
        print("[q] pour quitter")
        while True:

            if keyboard.is_pressed("1") and not var_af:
                command = ("streamlit run " +
                           os.getcwd() +
                           "/classes/execute_carte_categories.py")
                os.system(command)
                os.system('cls' if os.name == 'nt' else 'clear')
                self.main_menu()
            if keyboard.is_pressed("1") and var_af:
                command = ("streamlit run " +
                           os.getcwd() +
                           "/classes/execute_carte_produits.py")
                os.system(command)
                os.system('cls' if os.name == 'nt' else 'clear')
                self.main_menu()
            if keyboard.is_pressed("2"):
                afficheur.plot_histogramme(var_af, self.main_menu)
                return  # Sortir de cette boucle
            if keyboard.is_pressed("q"):
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Au revoir")
                break
            if keyboard.is_pressed("space"):
                os.system('cls' if os.name == 'nt' else 'clear')
                self.main_menu()
