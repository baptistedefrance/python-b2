import pandas as pd
import numpy as np

df_export = pd.DataFrame({'A':[0, 3, 4],'B':[2, 9, 7],'C':[6, 5, 5]}, index = ['a', 'b', 'c'])

df_export.to_csv('exempleExport.csv')

df_export.to_csv('exempleExport.csv', sep = ';')