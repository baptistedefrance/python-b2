import pandas as pd
import numpy as np

df_import = pd.read_csv('exempleExport.csv')

df_import = pd.read_csv('exempleExport.csv', index_col = 0, names = ['X1', 'X2', 'X3'], sep = ';')