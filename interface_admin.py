import keyboard  # using module keyboard
import time
import os
import pickle
from classes.site_web import SiteWeb

etoiles = "***********************************************"
"****************************"


class InterfaceAdmin:
    def __init__(self):
        print(etoiles)
        print("Cette application permet de visualiser des"
              " données de prix et d'en obtenir")
        print(etoiles)
        self.main_menu()

    def main_menu(self):
        time.sleep(0.5)
        print(etoiles)
        print("[1] Récolecter des données")
        print("[2] Entrer la section d'affichage")
        print("Pour quitter, appuyez sur q")

        while True:
            if keyboard.is_pressed('q'):
                print('Quitter')
                break
            if keyboard.is_pressed('1'):
                self.menu_recolte()

            if keyboard.is_pressed('2'):
                self.menu_affichage()

    def menu_affichage(self):
        pass

    def ajouter_requetes(self):

        if not os.path.exists("donnees/rr_data.pkl"):
            # Cree un dictionnaire vide si le fichier n'existe pas
            rr = {}

        else:
            # Ouvre la BDD
            with open("donnees/rr_data.pkl", "rb") as file:
                rr = pickle.load(file)

        print("Nom de la requete, attention si le nom figure "
              "dans la site suivante,"
              " les anciennes requetes seront remplacés par les nouvelles.")
        print(rr.keys())

        nom = str(input)

        liste = []
        exit = False
        while True:
            print("requetes dans " + nom + " : " + str(liste))
            liste.append(str(input("nom requete à ajouter")))
            print("Ajouter en plus ?")
            while True:
                if keyboard.is_pressed('o'):
                    break

                if keyboard.is_pressed('n'):
                    exit = True
                    break

            if exit:
                break

        rr.update({nom: liste})
        with open("donnees/rr_data.pkl", "wb") as file:
            pickle.dump(rr, file)

        print("Ajouter une nouvelle requete ?")
        print("[o] Oui")
        print("[n] Non")
        print(" q pour quitter")
        while True:
            if keyboard.is_pressed('n'):
                self.main_menu()

            if keyboard.is_pressed('y') or keyboard.is_pressed("o"):
                self.ajouter_requetes()
            if keyboard.is_pressed('q'):
                break

    def menu_recolte(self):
        time.sleep(0.5)
        print(etoiles)

        print("[1] Ajouter site web")
        print("[2] Ajouter un nouvel ensemble de requete")
        print("[3] lancer web scraping ")
        print("Pour aller en arrière appuye sur espace")
        print("Pour quitter, appuyez sur q")

        while True:
            if keyboard.is_pressed('q'):
                print('Quitter')
                break
            if keyboard.is_pressed('space'):
                self.main_menu()

            if keyboard.is_pressed('1'):
                self.ajouter_sw()

            if keyboard.is_pressed("2"):
                self.ajouter_requetes()

            if keyboard.is_pressed("3"):
                self.lancer_web_scraping()

    def ajouter_sw(self):
        time.sleep(0.5)
        print(etoiles)
        print()  # sites webs
        print("Souhaitez vous ajouter un site web ?")
        print("[o] Oui")
        print("[n] Non")

        while True:
            if keyboard.is_pressed('n'):
                self.menu_recolte()

            if keyboard.is_pressed('y') or keyboard.is_pressed("o"):
                break

        nom = str(input("Comment souhaitez vous appeler se site ? "))
        print("Veuillez rentrer l'url de recherche : ")
        print("Exemple : https://www.amazon.com/s?k=")
        url_recherche = str(input())
        pays = str(input("Domaine internet pays de recherche : "))
        avant_prix1 = str(input("Dans le code source html du site,"
                                " l'affichage du type est fait dans"
                                " quelle modalité ? Ex : span"))
        avant_prix2 = {"class": str(input("Dans le code source html du site,"
                                          " l'affichage du type est fait dans"
                                          " quelle class ? Ex : "
                                          "a-price-whole"))}

        print("Quelle méthode pour scraper ?")
        print("[1] Bee, Recomandé")
        print("[2] Sans proxy")
        while True:
            if keyboard.is_pressed('1'):
                scraping_type = "Bee"
                break

            if keyboard.is_pressed('2'):
                scraping_type = "Normal"
                break
        dictsite = {
                    "_url_recherche": ["", ""],
                    "_pays_domaines": [url_recherche],
                    "_devant_prix_entier":  [avant_prix1, avant_prix2],
                    "_devant_prix_decimal": None,
                    "_pays": pays,
                    "_scraping_type": scraping_type,
                    "requete": []}

        if not os.path.exists("donnees/rsw_data.pkl"):
            # Cree un dictionnaire vide si le fichier n'existe pas
            rsw = {}

        else:
            # Ouvre la BDD
            with open("donnees/rsw_data.pkl", "rb") as file:
                rsw = pickle.load(file)

        rsw.update({nom: dictsite})

        with open("donnees/rsw_data.pkl", "wb") as file:
            pickle.dump(rsw, file)

        print("Ajouter un nouveau site ?")
        print("[o] Oui")
        print("[n] Non")
        print(" q pour quitter")
        while True:
            if keyboard.is_pressed('n'):
                self.main_menu()

            if keyboard.is_pressed('y') or keyboard.is_pressed("o"):
                self.ajouter_sw()
            if keyboard.is_pressed('q'):
                break

    def lancer_web_scraping(self):
        time.sleep(0.5)
        print(etoiles)
        print("Quel site voulez vous utiliser pour web scraper ?")

        with open("donnees/rsw_data.pkl", "rb") as file:
            rsw = pickle.load(file)

        with open("donnees/rr_data.pkl", "rb") as file:
            rr = pickle.load(file)

        print("Choix possibles : ")
        print(rsw.keys())
        choix_sw = str(input())
        while choix_sw not in rsw.keys():
            print("Appuyez sur espace pour retour au menu")
            if keyboard.is_pressed('space'):
                self.main_menu()
            time.sleep(0.5)
            print("le site web rentré ne figure pas dans la base")
            choix_sw = str(input())

        print(etoiles)
        print("Quel requete utiliser pour web scraper ?")
        print("Choix possibles : ")
        print(rr.keys())
        choix_rq = str(input())
        while choix_sw not in rsw.keys():
            print("Appuyez sur espace pour retour au menu")
            if keyboard.is_pressed('space'):
                self.main_menu()
            time.sleep(0.5)
            print("la requete rentrée ne figure pas dans la base")
            choix_rq = str(input())

        site = SiteWeb(choix_sw)
        site.WebScrapping(choix_rq)
