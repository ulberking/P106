import pandas as pd
import plotly.express as px
import numpy as np
df = pd.read_csv('ice.csv')
temperature = df['Temperature'].tolist()
ice_creame = df['Ice-cream Sales( ₹ )'].tolist()
d = {'x':temperature,'y':ice_creame}
correlation = np.corrcoef(d['x'],d['y'])
# print(correlation)
# graph = px.scatter(df,x='Temperature',y='Ice-cream Sales( ₹ )')
# graph.show()