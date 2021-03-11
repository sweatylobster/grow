from functools import reduce
# number of lights:    n  (integer)
# dimensions of light: s  (square feet)
# size of aisle:       a  (feet)
# ::: n*s*a  = area of facility, as 'A'.
# A * height = volume of facility (cubic feet).
# CFM = (V : hour :: 1.5) -- set arbitrarily and without criteria.
# CFH must be balanced so as not to waste CO2.
# V holds a quantity of air in mol
# density * V = mol(air)

# inferences from Chandra's "Table 2"
# 350 umol/mol = ambient CO2/air
# 750 umol/mol shows 50%|111%|115% increases in Pn, WUE, Ci when the two are compared.
# 650 umol/mol 
# ::: data suggest higher yield with (even) higher CO2, perhaps 1000 umol/mol.

def elec_price(n, W, hrs):
    kW = n * W * 0.001
    # 20 cents a kW/h in CA
    p = .20
    day = kW * hrs
    year = day * 365.25
    ppy = year * p
    return ppy
    #return f'kWh costs of {n}, {W}W lights a year: ${ppy}'

lights = (72, 480, 15)
cypress = (20, 725, 15)
T4 = {'cfm': 205, 'W' : 28}

# price per month
container_year = 165 * 12
total = reduce(lambda x, y: x+y, [elec_price(*cypress), container_year])

print(f"rental of 40x8.5x8 shipping container: ${container_year}/year")
print("environment (Temp, RH, VPD) costs unknown.")
print(f"for {cypress[0]}, {cypress[1]}W lights running {cypress[2]}h/day, ${elec_price(*cypress)}")
print(f"total yearly cost = ${total}")
