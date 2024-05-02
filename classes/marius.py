import pickle

with open("classes\database.pkl", "rb") as file:
                database_fichier = pickle.load(file)

print(database_fichier.keys())
