from pathlib import Path

import pandas as pd

p=Path.cwd()
dataframes = []

# Parcourir tous les fichiers commençant par "data" et se terminant par ".json"
for file_path in p.glob("data*.json"):
    if file_path.is_file():
        # Charger le fichier JSON en dataframe et l'ajouter à la liste
        df = pd.read_json(file_path)
        dataframes.append(df)
if dataframes:
    df=pd.concat(dataframes,ignore_index=True)
    print(df.shape)
    do=df.drop_duplicates(subset="titre")
    do.to_json("data_x2.json")