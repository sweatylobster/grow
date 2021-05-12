import pandas as pd
import numpy as np

labels = ["O&F", "NEEM", "KELP", "NAPR"]

ingredients = pd.DataFrame(
              [{'kg/L': 2.72/13.2, 'in_mix' : 0.929444, 'N' : .03, 'P' : .045, 'K' : .005,  "Ca" : .1},
               {'kg/L':  2.27/3.2,  'in_mix' : 0.003888, 'N' : .60, 'P' : .10, 'K' : .20},
               {'kg/L':  1.80/1.89, 'in_mix' : 0.046666, 'N' : .10, 'P' : 0.0, 'K' : .20,  "Ca" : .10, "Mg" : .050, "S" : .20},
               {'kg/L':  4.5/28, 'in_mix' : 0.02, 'N' : .60, 'P' : .30, 'K' : .35,  "Ca" : .70, "Mg" : 0.07, "S" : 0.25,  "Fe" : 0.02}], index=labels)


density = ingredients[['kg/L']]
#convert kg/L -> lb/gal
galones = density * 8.3454
# add galones to ingredients
ingredients.insert(1, "lb/gal", galones)

print(ingredients)
