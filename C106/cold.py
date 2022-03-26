import pandas as pd
import plotly.express as px
import numpy as np
df =pd.read_csv('ice.csv')
temperature = df['Temperature'].tolist()
cold_drink = df['Cold drink sales( ₹ )'].tolist()
d = {'x':temperature,'y':cold_drink}
correlation = np.corrcoef(d['x'],d['y'])
print(correlation)