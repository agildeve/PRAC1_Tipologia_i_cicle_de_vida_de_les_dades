from bs4 import BeautifulSoup
import requests
import pandas as pd

# Definum el Dataframe bp_dataset, per anar guardant la informació obtinguda a través del scraping.
bp_dataset = pd.DataFrame(columns=['categoria_1','categoria_2','categoria_3','categoria_4', 'nom', 'preu', 'quantitat', 'preu unitari'])

# Definim la funció sc_bonpreu, que donada una categoria i una url, fa scraping a la url i utilitza la categoria per classificar la informació.

def sc_bonpreu(url):
    bp_dataset = pd.DataFrame(columns=['categoria_1','categoria_2','categoria_3','categoria_4', 'nom', 'preu', 'quantitat', 'preu unitari'])

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')

    #Primer, capturem les categories de classificació.
    cat = soup.find('div', class_='bar__Bar-gf1nko-0 EGrQK')
    pos = 0
    lst = ['element 1', 'element 2', 'element 3', 'element 4']
    for sibling in cat.li.next_siblings:
#        print(sibling.text)
        lst[pos] = sibling.text
        pos = pos + 1

    prd = soup.find_all('div', wrap='wrap')
#    print (prd)
    for i in prd:
        nom = i.div.h3.a.text
        preu =i.div.strong.text
        qntat = i.find('span', display="inline-block").text
        p_uni = i.find('span', class_="text__Text-x7sj8-0 jrIktQ").text
        add_row = {'categoria_1': lst[0],
                   'categoria_2': lst[1],
                   'categoria_3': lst[2],
                   'categoria_4': lst[3],
                   'nom': nom,
                   'preu': preu,
                   'quantitat' : qntat,
                   'preu unitari' : p_uni}

        bp_dataset = bp_dataset.append(add_row, ignore_index = True)

    return bp_dataset

urls =  ['https://www.compraonline.bonpreuesclat.cat/products?sortBy=favorite&sublocationId=030366a6-3f77-44d8-88a9-e7b6fb7b0eca',
         'https://www.compraonline.bonpreuesclat.cat/products?sortBy=favorite&sublocationId=7cf3a7c2-b7c6-49bd-b28b-bfc13069af9b',
         'https://www.compraonline.bonpreuesclat.cat/products?sortBy=favorite&sublocationId=dc45f555-b1ed-439b-975b-19507728bc7b',
         'https://www.compraonline.bonpreuesclat.cat/products?sortBy=favorite&sublocationId=c7dcde3c-8929-4cf5-92fe-26d3c3c6cffa',
         'https://www.compraonline.bonpreuesclat.cat/products?sortBy=favorite&sublocationId=ce6583fd-a6e5-4a76-8ee1-8d5fcd337618',
         'https://www.compraonline.bonpreuesclat.cat/products?sortBy=favorite&sublocationId=e3e2ecc0-1e30-4cf3-9cc5-37bccbc99033',
         'https://www.compraonline.bonpreuesclat.cat/products?sortBy=favorite&sublocationId=a2fe6045-6353-4666-917e-ea2d5f0af858']

for x in urls:
    df = sc_bonpreu(x)
#    print(df)
    bp_dataset = bp_dataset.append(df, ignore_index = True)

#print (bp_dataset)
bp_dataset.to_csv('bp_dataset.csv', index=True)
