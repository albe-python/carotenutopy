import pandas as pd
import plotly.express as px

df = pd.read_csv('DatiStatistici.csv')


fig = px.bar(df, x = 'Classe di eta', y = '  usano il pc', title='Persone di 3 anni e più per utilizzo del personal computer e frequenza di utilizzo', labels={"Uso del PC"})
fig.show()
