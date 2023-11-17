
import time

from openai import OpenAI

from constants.params import NESSAI, TOKEN, DELAI

# Initalisation
openai_token=TOKEN
# Définissez le nombre de rée ssais
nombre_de_reessais = NESSAI
delai_dattente = DELAI  # Temps d'attente en secondes (ajustez selon vos besoins)
client = OpenAI(api_key=openai_token)

# Fonction pour effectuer la requête à l'API avec gestion des erreurs et des réessais
def effectuer_requete_avec_reessais(contexte,command):
    for i in range(nombre_de_reessais):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": contexte},
                    {"role": "user", "content": command}
                ]
            )
            return response.choices[0].message.content
        except :
            print(f"Une erreur s'est produit")
            print("Réessai...")
            time.sleep(delai_dattente*i)
    print("Trop de réessais, la requête a échoué.")
    return None




def transform_elementcle_to_rap(element_cle,titre=""):
   contexte="" "Tu es un compositeur de parole de rap,a partir des elemnts clés en mettant en evidence des notions educatifs et l'accent sur des dates, des evenements marquant, ne dépassant pas 2  couplets de 4 vers maximum."
   command=f"Compose du texte rap court et concret en precisant avant chaque section entre crochet couplet et refrain,a partir de {titre} : {element_cle} "
   return effectuer_requete_avec_reessais(contexte,command)



def transform_text_to_elementcle(text,titre=""):
    text=text.strip().replace('\n','')[:2000]
    contexte="""Tu es capable de transformer un long texte en une liste d'elements clés de 5 minimum et 10 au maximum elements.Chaque elements clés est une phrase
    qui décrit correctement le texte,les années date et tout sont importantes."""
    command=f"Voici le texte {titre} : {text} "
    return effectuer_requete_avec_reessais(contexte,command)



