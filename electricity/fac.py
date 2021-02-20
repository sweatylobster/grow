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
    rate = .20
    day = kW * hrs
    year = day * 365.25
    ppy = year * p
    return f'Cost per year: {ppy}'

lights = (72, 480, 15)
print(elec_price(*lights))
