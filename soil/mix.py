import pandas as pd

labels = ["O&F", "NEEM", "KELP", "NAPR"]

ingredients = pd.DataFrame(
                  [{'kg/L': 2.72/13.2, 'in_mix' : 0.929444,   'N' : .3,  'P' : .45, 'K' : .05,  "Ca" : 1.0},
                  {'kg/L':  2.27/3.2,  'in_mix' : 0.003888,    'N' : 6.0, 'P' : 1.0, 'K' : 2.0},
                  {'kg/L':  1.80/1.89, 'in_mix' : 0.046666,    'N' : 1.0, 'P' : 0.0, 'K' : 2.0,  "Ca" : 1.0, "Mg" : .50, "S" : 2.0},
                  {'kg/L':  4.5/28,    'in_mix' : 0.02, 'N' : 6.0, 'P' : 3.0, 'K' : 3.5,  "Ca" : 7.0, "Mg" : 0.7, "S" : 2.5,  "Fe" : 0.2}], index=labels)


density = ingredients[['kg/L']]
#convert kg/L -> lb/gal
galones = density * 8.3454

# add galones to ingredients
ingredients.insert(1, "lb/gal", galones)
