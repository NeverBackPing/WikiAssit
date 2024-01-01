# Import Wikipedia-API
import wikipediaapi

user_agent = "MyUserAgent/1.0 (https://github.com/NeverBackPing/)"


# Créer un objet wiki en spécifiant la langue
wiki_wiki = wikipediaapi.Wikipedia(language='fr', user_agent=user_agent)


# Vérifier si la page existe

while(1):
  # Obtenir une page de Wikipédia
  texte_saisi = input("\nVeuillez entrer quelque chose : ")
  print("\nVous avez saisi :", texte_saisi)
  page = wiki_wiki.page(texte_saisi)

  if page.exists():
    #Imprimer le résumé de la page
    print("\nTitre de la page : ", page.title)
    print("\nRésumé de la page : ", page.summary[0:80])
