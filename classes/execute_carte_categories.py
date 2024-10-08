import pickle
from affichages_donnee import AffichageDonnees
import os


with open("donnees/bdd_indice_prod.pkl", "rb") as file:
    ind_prod = pickle.load(file)
with open("donnees/bdd_indice_cat.pkl", "rb") as file:
    ind_cat = pickle.load(file)

mon_test = AffichageDonnees(ind_prod, ind_cat)

mon_test.AfficherCarte(False)

command = ("python " +
           os.getcwd() +
           "/__main__.py")
os.system(command)
