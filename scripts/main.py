from scraper import sc_bonpreu
from get_urls import urls_list
import pandas as pd
from tqdm import tqdm
from datetime import date

url = 'https://www.compraonline.bonpreuesclat.cat/products'

# Definim el Dataframe bp_dataset, per anar guardant la informació obtinguda a través del scraping:

bp_dataset = pd.DataFrame(
    columns=['Categoria_1', 'Categoria_2', 'Categoria_3', 'Categoria_4', 'Categoria_5', 'Nom', 'Preu', 'Quantitat',
             'Preu unitari', 'Oferta', 'Promocio', 'URL', 'Date'])

llista_urls = []
llista_urls = urls_list(url)
#llista_urls = ['https://www.compraonline.bonpreuesclat.cat/products?sortBy=favorite&sublocationId=b4098292-6a2a-428f-ace6-076a19878890']

# Finalment, executem la funció per a cada una de les urls obtingudes en el script anterior:
print("\nStart Scraping...")
for x in tqdm(llista_urls):
    df = sc_bonpreu(x)
    bp_dataset = bp_dataset.append(df, ignore_index=True)


# Abans de guardar, eliminem rows amb al menys quatre 'na'.
#bp_dataset.drop()
print("Scraping done, cleaning...")
bp_dataset = bp_dataset[bp_dataset['Nom'] != 'PRODUCTE NO OBTINGUT']

# Guardem la informació en el dataset:
print("Saving dataset...")
dt = date.today()
name_to_save = dt.strftime("%Y%m%d") + '_BP_dataset.csv'
bp_dataset.to_csv(name_to_save, index=False)

print(dt.strftime("%d/%m/%Y"), ' - Your saved Dataset has ', bp_dataset.shape[0], ' ROWS and ', bp_dataset.shape[1], 'COLUMNS.')