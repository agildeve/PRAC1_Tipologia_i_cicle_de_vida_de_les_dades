from bs4 import BeautifulSoup
import requests
import pandas as pd

# url a la que volem fer scraping
url = 'https://www.compraonline.bonpreuesclat.cat/products/'

# descarreguem la url i visualitzem la estructura imbricada:
page = requests.get(url)
soup = BeautifulSoup(page.content)

print(soup.prettify())
