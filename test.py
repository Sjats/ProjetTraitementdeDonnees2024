import pickle

with open("donnees/database.pkl", "rb") as file:
    dd = pickle.load(file)
print(dd)
