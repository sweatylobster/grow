import pandas as pd

# list(dict()) -- individuals

ambient = {'parameters' : ['TEMP', 'HUMIDITY', 'WIND', 'CO2', 'R-Z TEMP', 'NUTRIENTS', 'OXYGEN', 'WATER'],
                        'units' : ['F', '%', 'v/m^2*s', 'PPM/g(soil)', 'F', 'g/vol', 'PPM', 'g'],
                        'light-driven' : [False, False, False, True, False, True, True, True],
                        'device on-hand' : [True, True, False, False, False, False, False, True],
                        'purchase device?' : [True, True, False, True, True, True, True, False]
}

amb_df = pd.DataFrame(ambient)

print(amb_df)
