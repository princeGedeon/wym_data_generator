import json
import time

import wikipedia


def save_in_file(data,name="data.json"):
    with open(f'output/{name}', 'w') as f:
        json.dump(data, f)

def read_file(path_file="outputs/data.json"):
    data=[]
    with open(path_file) as f:
        data = json.load(f)

    return data


def wiki_mot_cle_to_data(mot_cle):
    L = []
    try:
        search=wikipedia.search(mot_cle)
        for i in range(len(search)-1):
            page=wikipedia.page(search[i])

            resume=page.summary
            if len(resume)>=500:
                data={
                    "titre":page.title,
                    "text_origine":resume,
                }
                L.append(data)
                time.sleep(5)
            else:
                print("Trop court")
    except:
        print(f"Sortie automatique : mots clé {mot_cle} avec {len(L)}")
        return L
    else:
        print(f"Sortie manuelle : Mot_cle : {mot_cle}-------------------------------({len(L)}) finished")
        return L
