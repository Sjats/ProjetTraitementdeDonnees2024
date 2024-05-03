from classes.produit import Produit
import pickle


with open("donnees/database.pkl", "rb") as file:
    data_articles = pickle.load(file)


NomsProduits = []
for art in data_articles:
    aux = art.split("/")[1]
    if aux not in NomsProduits:
        NomsProduits.append(aux)

for nom in NomsProduits:
    aux = Produit(nom, data_articles)
    aux.Enregistrement_prod()
