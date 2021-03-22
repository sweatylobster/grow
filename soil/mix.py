import pandas as pd
# tuple order is NPK, scaling it down from unity kg-soil -> g-element
# because the ocean and forest is .30%, .45%, .05%, the total g content per unit weight is .0030, etc.
soils = {"ocean and forest" : (.0030, .0045, .0005), "neem seed" : (.60, .10, .20)}
# units are kg/L
densities = {"ocean and forest" : 2.72/13.2, "neem seed" : 0}

index = ["O&F", "NEEM", "KELP"]

a = pd.DataFrame([{'N' : .0030, 'P' : .0045, 'K' : .0005, "Ca" : .01}, {'N' : .0060, 'P' : .0010, 'K' : .0020, "Ca" : None}, {'N' : , 'P' : , 'K' : , "Ca" : }], index=index)
print(a.head())
