from interface.interface_admin import InterfaceAdmin
from interface.interface_sd import InterfaceSd


if __name__ == "__main__":
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
