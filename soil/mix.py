import pandas as pd
# tuple order is NPK, scaling it down from unity kg-soil -> g-element
# because the ocean and forest is .30%, .45%, .05%, the total g content per unit weight is .0030, etc.
# units are kg/L
index = ["O&F", "NEEM", "KELP", "NAPR"]

a = pd.DataFrame([{'L/kg' : 13.2/2.72, 'N' : .3, 'P' : .45, 'K' : .05, "Ca" : 1},
                  {'L/kg' : 3.2/2.27, 'N' : 6.0, 'P' : 1.0, 'K' : 2.0},
                  {'L/kg' : 1.89/1.80, 'N' : 1.0, 'P' : 0.0, 'K' : 2.0, "Ca" : 1.0, "Mg" : .50, "S" : 2.0}, 
                  {'L/kg' : 28/4.5, 'N' : 6.0, 'P' : 3.0, 'K' : 3.5, "Ca" : 7.0, "Mg" : 0.7, "S" : 2.5, "Fe" : 0.2}], index=index)
print(a.head())

class mix():

    soils     = {"ocean and forest": (0.0030, 0.0045, 0.0005),
                 "neem seed":        (0.60, 0.10, 0.20),
                 "kelp meal":        (0.010, .0, 0.020),
                 "nature's pride":   (0.006, 0.0030, 0.0035)
                 }

    densities = {"ocean and forest": 13.2/2.72,
                 "neem seed":        0,
                 "kelp meal":        1.89/1.8
                 "nature's pride":   28/4.5
                 }
    print(densities)

    def __init__(self, weight):
        self.weight = weight

    def vol_by_weight(weight):
        pass

    def weight_by_vol(vol):
        pass

    def quanta(vol, weight):
        pass
