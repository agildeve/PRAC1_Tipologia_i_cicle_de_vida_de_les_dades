# Instal·lem 'BeautifulSoup' en cas de no tenir-lo:
# pip install beautifulsoup4

# Instal·lem 'tqdm' en cas de no tenir-lo (és per veure el progrés dels for loops que siguin llargs):
# pip install tqdm

# Instal·lem 'lxml' en cas de no tenir-lo:
# pip install lxml

# Instal·lem 'requests' en cas de no tenir-lo:
# pip install requests

# Importem les llibreries que utilitzarem:
from bs4 import BeautifulSoup
from tqdm import tqdm
import requests

# Com a url principal agafem la més general:
#url = 'https://www.compraonline.bonpreuesclat.cat/products'

def urls_list(url):

    # Obtenim el contingut de la url
    page = requests.get(url).text

    # Organitzem el format html:
    soup = BeautifulSoup(page, 'lxml')

    # Ens situem a la secció de la pàgina d'on obtindrem les categories:
    llista = soup.find('div', class_='spacing__Spacing-sc-5fzqe7-0 kcPzHi')

    # Creem un diccionari per a les categories més externes on hi posarem el nom de la categoria juntament amb la seva url:
    categoria_1 = {}

    # Iterem per omplir el diccionari:
    for i in tqdm(llista.find_all('li')):
        categoria_1[i.a.text] = 'https://www.compraonline.bonpreuesclat.cat' + i.a['href']

    # Creem un diccionari per a les categories següents:
    categoria_2 = {}

    # Iterem per omplir el diccionari:
    for i in tqdm(categoria_1.values()):
        soup = BeautifulSoup(requests.get(i).text, 'lxml')
        match = soup.find('div', class_='spacing__Spacing-sc-5fzqe7-0 kcPzHi')

        for j in match.find_all('li'):
            categoria_2[j.a.text] = 'https://www.compraonline.bonpreuesclat.cat' + j.a['href']

    # Creem un diccionari per a les categories següents:
    categoria_3 = {}

    # Creem un llistat per emmagatzemar aquelles categories que ja són les últimes:
    productes_2 = []

    # Iterem per omplir el diccionari i en cas de no trobar més categories, és a dir, que trobi una que és la última, posar-la en la llista 'productes':
    for i in tqdm(categoria_2.values()):
        try:
            soup = BeautifulSoup(requests.get(i).text, 'lxml')
            match = soup.find('div', class_='spacing__Spacing-sc-5fzqe7-0 kcPzHi')

            for j in match.find_all('li'):
                categoria_3[j.a.text] = 'https://www.compraonline.bonpreuesclat.cat' + j.a['href']

        except Exception as e:
            productes_2.append(list(categoria_2.keys())[list(categoria_2.values()).index(i)])

    # Creem un diccionari per a les categories següents:
    categoria_4 = {}

    # Creem un llistat per emmagatzemar aquelles categories que ja són les últimes:
    productes_3 = []

    # Iterem per omplir el diccionari i en cas de no trobar més categories, és a dir, que trobi una que és la última, posar-la en la llista 'productes':
    for i in tqdm(categoria_3.values()):
        try:
            soup = BeautifulSoup(requests.get(i).text, 'lxml')
            match = soup.find('div', class_='spacing__Spacing-sc-5fzqe7-0 kcPzHi')

            for j in match.find_all('li'):
                categoria_4[j.a.text] = 'https://www.compraonline.bonpreuesclat.cat' + j.a['href']

        except Exception as e:
            productes_3.append(list(categoria_3.keys())[list(categoria_3.values()).index(i)])

    # Creem un diccionari per a les categories següents:
    categoria_5 = {}

    # Creem un llistat per emmagatzemar aquelles categories que ja són les últimes:
    productes_4 = []

    # Iterem per omplir el diccionari i en cas de no trobar més categories, és a dir, que trobi una que és la última, posar-la en la llista 'productes':
    for i in tqdm(categoria_4.values()):
        try:
            soup = BeautifulSoup(requests.get(i).text, 'lxml')
            match = soup.find('div', class_='spacing__Spacing-sc-5fzqe7-0 kcPzHi')

            for j in match.find_all('li'):
                categoria_5[j.a.text] = 'https://www.compraonline.bonpreuesclat.cat' + j.a['href']

        except Exception as e:
            productes_4.append(list(categoria_4.keys())[list(categoria_4.values()).index(i)])

    # Creem un diccionari per a les categories següents:
    categoria_6 = {}

    # Creem un llistat per emmagatzemar aquelles categories que ja són les últimes:
    productes_5 = []

    # Iterem per omplir el diccionari i en cas de no trobar més categories, és a dir, que trobi una que és la última, posar-la en la llista 'productes':
    for i in tqdm(categoria_5.values()):
        try:
            soup = BeautifulSoup(requests.get(i).text, 'lxml')
            match = soup.find('div', class_='spacing__Spacing-sc-5fzqe7-0 kcPzHi')

            for j in match.find_all('li'):
                categoria_6[j.a.text] = 'https://www.compraonline.bonpreuesclat.cat' + j.a['href']

        except Exception as e:
            productes_5.append(list(categoria_5.keys())[list(categoria_5.values()).index(i)])

    # Finalment, agrupem totes les categories finals:
    categories_finals = productes_2 + productes_3 + productes_4 + productes_5

    # Les podem veure per pantalla si volem (n'hi ha unes 800):
    # categories_finals

    # Però el que ens interessa a nosaltres és la url d'aquestes categories, així que les emmagatzemarem aqui:
    urls_finals = []

    # Obtenim la url de cada categoria final i la emmagatzem a la llista 'urls_finals' que hem creat:
    for i in productes_2:
        urls_finals.append(categoria_2[i])

    for i in productes_3:
        urls_finals.append(categoria_3[i])

    for i in productes_4:
        urls_finals.append(categoria_4[i])

    for i in productes_5:
        urls_finals.append(categoria_5[i])

    # Mostrem per pantalla el llistat de urls finals que hem obtingut i sobre les quals realitzarem el scraping:

    return urls_finals