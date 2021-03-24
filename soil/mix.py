import pandas as pd
# tuple order is NPK, scaling it down from unity kg-soil -> g-element
# because the ocean and forest is .30%, .45%, .05%, the total g content per unit weight is .0030, etc.
# units are kg/L
index = ["O&F", "NEEM", "KELP", "NAPR"]

a = pd.DataFrame([{'kg/mL' : 2.72/13.2, 'N' : .3, 'P' : .45, 'K' : .05, "Ca" : 1},
                  {'kg/mL' : 2.27/3.2 , 'N' : 6.0, 'P' : 1.0, 'K' : 2.0},
                  {'kg/mL' : 1.80/1.89, 'N' : 1.0, 'P' : 0.0, 'K' : 2.0, "Ca" : 1.0, "Mg" : .50, "S" : 2.0}, 
                  {'kg/mL' : 4.5/28, 'N' : 6.0, 'P' : 3.0, 'K' : 3.5, "Ca" : 7.0, "Mg" : 0.7, "S" : 2.5, "Fe" : 0.2}], index=index)
print(a.head())

class mix():

    soils     = {"ocean and forest": (0.0030, 0.0045, 0.0005),
                 "neem seed":        (0.60, 0.10, 0.20),
                 "kelp meal":        (0.010, .0, 0.020),
                 "nature's pride":   (0.006, 0.0030, 0.0035)
                 }

    densities = {"ocean and forest": 2.72/13.2,
                 "neem seed":        0,
                 "kelp meal":        1.8/1.89
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