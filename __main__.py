from interface.interface_admin import InterfaceAdmin
from interface.interface_sd import InterfaceSd


# Exemple d'utilisation des interfaces
if __name__ == "__main__":
    print("Attention, pour que le code fonctionne, "
          "il faut se trouver à l'adresse .../Projet"
          "TraitementdeDonnees2024.")
    print("Utilisateur : ")
    utilisateur = str(input())
    flag = True
    if utilisateur == "admin":
        print("Mot de pase : ")
        mdp = str(input())
        if mdp == "admin":
            InterfaceAdmin()
            flag = False
        else:
            print("Mauvais mot de passe")
            print("Se connecter en tant qu'utilisateur")

    if flag:
        InterfaceSd()
