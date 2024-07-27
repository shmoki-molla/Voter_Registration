from interface import root
from dotenv import load_dotenv
from database import engine
import pandas as pd

names = ['Jurisdiction', 'Year', 'Month', 'quantity']
df = pd.read_csv('new-voter-registrations.csv', sep=',', names=names)
df = df[df['Month'] != 'May']
df.to_sql('voters', engine, if_exists='replace', index=False)

root.mainloop()
