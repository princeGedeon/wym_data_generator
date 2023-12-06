import json
import time

import wikipedia


def save_in_file(data,name="data.json"):
    with open(f'output/{name}', 'w') as f:
        json.dump(data, f)

def save_in_file_full(data,name="data.json"):
    with open(f'{name}', 'w') as f:
        json.dump(data, f)
def read_file(path_file="outputs/data.json"):
    data=[]
    with open(path_file) as f:
        data = json.load(f)

    return data


def enlever_elements_dictionnaire(dictionnaire, liste_titres_a_supprimer):
    # Utilisation d'une copie du dictionnaire pour éviter de modifier le dictionnaire d'origine pendant l'itération
    dictionnaire_copie = dictionnaire.copy()

    for element in dictionnaire_copie:
        if element["titre"] in liste_titres_a_supprimer:
            dictionnaire.remove(element)
    return dictionnaire

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
#L = read_file(path_file="../final_dataset/data.json")
#print(len(L))
""" 
L=read_file(path_file="../final_dataset/data_partie1.json")
L2=read_file(path_file="../final_dataset/data_partie2.json")
L3=read_file(path_file="../final_dataset/data_partie3.json")
L4=read_file(path_file="../final_dataset/data_partie4.json")
L5=read_file(path_file="../final_dataset/data_partie5.json")
L6=read_file(path_file="../final_dataset/data_partie6.json")
L7=read_file(path_file="../final_dataset/data_partie7.json")

L8=read_file(path_file="../final_dataset/data_partie8.json")
L9=read_file(path_file="../final_dataset/data_partie9.json")
L10=read_file(path_file="../final_dataset/data_partie10.json")
L11=read_file(path_file="../final_dataset/data_partie11.json")
L12=read_file(path_file="../final_dataset/data_partie12.json")
L13=read_file(path_file="../final_dataset/data_partie13.json")
L14=read_file(path_file="../final_dataset/data_partie14.json")
L15=read_file(path_file="../final_dataset/data_partie15.json")
L16=read_file(path_file="../final_dataset/data_partie16.json")
L17=read_file(path_file="../final_dataset/data_partie17.json")
L19=read_file(path_file="../final_dataset/data_partie18.json")
L20=read_file(path_file="../final_dataset/data_partie20.json")
L21=read_file(path_file="../final_dataset/data_partie21.json")

L22=read_file(path_file="../final_dataset/data_partie22.json")
L23=read_file(path_file="../final_dataset/data_partie23.json")
L24=read_file(path_file="../final_dataset/data_partie24.json")
L25=read_file(path_file="../final_dataset/data_partie25.json")
L26=read_file(path_file="../final_dataset/data_partie26.json")
L27=read_file(path_file="../final_dataset/data_partie27.json")
L28=read_file(path_file="../final_dataset/data_partie28.json")
L29=read_file(path_file="../final_dataset/data_partie29.json")
L30=read_file(path_file="../final_dataset/data_partie30.json")
L31=read_file(path_file="../final_dataset/data_partie31.json")
L32=read_file(path_file="../final_dataset/data_partie32.json")
L33=read_file(path_file="../final_dataset/data_partie33.json")
L34=read_file(path_file="../final_dataset/data_partie34.json")
L35=read_file(path_file="../final_dataset/data_partie35.json")
L36=read_file(path_file="../final_dataset/data_partie36.json")
L37=read_file(path_file="../final_dataset/data_partie37.json")
L38=read_file(path_file="../final_dataset/data_partie38.json")
L39=read_file(path_file="../final_dataset/data_partie39.json")
L40=read_file(path_file="../final_dataset/data_partie40.json")
L41=read_file(path_file="../final_dataset/data_partie41.json")
L42=read_file(path_file="../final_dataset/data_partie42.json")
L43=read_file(path_file="../final_dataset/data_partie43.json")
L44=read_file(path_file="../final_dataset/data_partie44.json")
L45=read_file(path_file="../final_dataset/data_partie45.json")
"""
#print(len(L)+len(L2)+len(L3)+len(L4)+len(L5)+len(L6)+len(L7)+len(L9)+len(L8)+len(L10)+len(L11)+len(L12)+len(L13)+len(L14)+len(L15)+len(L16)+len(L17)+len(L19)+len(L20)+len(L21)+len(L22)+len(L23)+len(L24)+len(L25)+len(L26)+len(L27)+len(L28)+len(L29)+len(L30)+len(L31)+len(L32)+len(L33)+len(L34)+len(L35)+len(L36)+len(L37)+len(L38)+len(L39)+len(L40)+len(L41)+len(L42)+len(L43)+len(L44)+len(L45))
