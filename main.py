import time
import wikipedia

from input.data import liste_educative
from tools.exp import transform_text_to_elementcle, transform_elementcle_to_rap
from tools.utils import wiki_mot_cle_to_data, save_in_file, enlever_elements_dictionnaire, read_file, save_in_file_full

# Logique
wikipedia.set_lang('fr')
datas=[]
refs=read_file("references/basis.json")
ref_current=[]
for i,mot_cle in enumerate(liste_educative):
    print(f'---------Traitement {mot_cle} numero{i}')
    tmp=wiki_mot_cle_to_data(mot_cle) # Recherche sur wikipédia
    print(f"- with duplicates on {len(tmp)}")
    tmp=enlever_elements_dictionnaire(tmp,refs+ref_current)#Filtre from repetitives
    print(f"- without duplicates on {len(tmp)}")
    t=[]
    for d in tmp:
        print("--generate elements_cle")
        d['element_cle']=transform_text_to_elementcle(titre=d.get('titre'),text=d.get('text_origine'))# Genere mots clés
        print("--generate rap")
        d['rap']=transform_elementcle_to_rap(element_cle=d.get('element_cle'),titre=d.get('titre'))#Génere rap
        if (d['element_cle']!=None) and (d['rap']!=None):
            t.append(d)
            ref_current.append(d["titre"])
            print(f"Fini : {d}")
    print(t)
    datas.extend(t)# Ajoute a la liste principale
    print(f"Taille actuelle : {len(datas)}")
    save_in_file(datas)#Save a chaque fois

    if (i % 10 ==0):
        save_in_file(datas, f"slots/data{len(datas)}.json")#Save a chaque 50

save_in_file_full(refs+ref_current,f"references/basis.json")

