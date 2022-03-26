
import pandas as pd
import plotly.express as px
import numpy as np
df = pd.read_csv('st.csv')
marks=df['Marks In Percentage'].tolist()
days=df['Days Present'].tolist()
d={'x':marks,'y':days}
correlation=np.corrcoef(d['x'],d['y'])
print(correlation)
