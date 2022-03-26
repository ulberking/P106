
import pandas as pd
import plotly.express as px
import numpy as np
df = pd.read_csv('coffee.csv')
ml = df['Coffee in ml'].tolist()
sleep = df['sleep in hours'].tolist()
d={'x':ml,'y':sleep}
correlation = np.corrcoef(d['x'],d['y'])
print(correlation)
# graph=px.scatter(df,x='Coffee in ml',y='sleep in hours')
# graph.show()