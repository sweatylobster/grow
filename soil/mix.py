import pandas as pd
from pandas import DataFrame as df
# tuple order is NPK, scaling it down from unity kg-soil -> g-element
soils = {"ocean and forest" : (.30, .45, .05), "neem seed" : (.60, .10, .20)}
# units are kg/L
densities = {"ocean and forest" : 2.72/13.2, "neem seed" : }

class NPK():
    "constructs a tuple specified in order: (N, P, K) for the three indices."

    def __init__(self, nitrogen, phosphorous, potassium):
        self.N = nitrogen
        self.P = phosphorous
        self.K = potassium

    def __eq__(self):
        return (self.nitrogen, self.phosphorous, self.potassium)

units = ["kg"]

def mix(units, *args):
    "put the elements of the tuple, weigh them by unit of choice"
    times = len(*args)
    l = [x for x in this]
    pass



class mix():

    def __init__(self, *args):
