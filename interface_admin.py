import keyboard  # using module keyboard
import time
# import pickel
etoiles = "***********************************************"
"****************************"


class Interface:
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

    def menu_recolte(self):
        time.sleep(0.5)
        print(etoiles)

        print("[1] Ajouter site web")
        print("[2] Ajouter nouveau indice")
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
                self.ajouter_indice()

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

        nom = str(input("Comment souhaitez vous appeler se site ?"))
