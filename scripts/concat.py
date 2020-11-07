############################################################################################################
#                                                                                                          #
# Inspired by an example found in stackoverflow with some modifications:                                   #
# https://stackoverflow.com/questions/53189427/how-to-open-multiple-csv-files-from-a-folder-in-python      #
#                                                                                                          #
############################################################################################################

import glob
import os
import pandas as pd

# llistem tots els csv que hi han en el directori:
csv_files = glob.glob(os.path.join('*.csv'))
print("Your final file will contain: ", csv_files)

# loop through the files and read them in with pandas
dataframes = []  # fem una llista on guardar tots els dataframes individualment:
for file in csv_files:
    if file == 'BP_dataset.csv' : # En cas d'haver executat l'script anteriorment evitem considerar l'arxiu que creem.
        print('Processing...')
    else:
        df = pd.read_csv(file)
        df = df[df['Nom'] != 'PRODUCTE NO OBTINGUT'] # Fem un petit filtatge de urls no valides
        dataframes.append(df)

result = pd.DataFrame()
#concatenem tots els dataframes:
for element in dataframes:
    result = result.append(element, ignore_index = True)

#result = pd.concat(dataframes, ignore_index=True)

# Guardem el dataframe obtingut.
result.to_csv('BP_dataset.csv', index=False)
print("You've created a Dataset with ", result.shape[0], ' ROWS and ', result.shape[1], 'COLUMNS.')