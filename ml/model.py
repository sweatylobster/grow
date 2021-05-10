import pandas as pd
from pycaret.classification import *

# TODO: fill f
f = '4-15-21.csv'
index = ['temp', 'humidity', 'CO2', 'PPFD', 'weight', 'canopy']
df = pd.read_csv(f, index=index)

# prepare data
data = df.sample(frac=0.95, random_state=42)

# i don't get this step fully
hold_out = df.drop(data.index)

data.reset_index(drop=True, inplace=True)

hold_out.reset_index(drop = True, inplace=True)

# model 
clfs       = setup(data=f, target='weight', session_id=123)
best_model = compare_models()
print(best_model)
