import pandas as pd
from functools import reduce

def gain(lights=20, price=2000, cpy=52//12, mode='quiet'):
    "Each light illuminates a 4x4 area of 6 plants"
    # area is .4444 ft^2
    plant = (8/12) * (8/12)
    num_plants = 16/plant
    ppl = num_plants * 0.25
    ipy = price * lights * ppl * cpy
    if mode == 'quiet':
        print(f"at {cpy} (complete) cycles/year, with {lights} lights each producing {ppl}lbs, at ${price} a pound: ${ipy}")
        pass
    return ipy

def elec_price(n, W, hrs):
    kW = n * W * 0.001
    # 20 cents a kW/h in CA
    p = .20
    day = kW * hrs
    year = day * 365.25
    ppy = year * p
    return ppy
    #return f'kWh costs of {n}, {W}W lights a year: ${ppy}'

def soil_price(price_per_volume, volume, plants):
    total = price_per_volume * volume * plants 
    return total

# electrical
lights = (72, 480, 15)
cypress = (20, 725, 15)

# soil pp(vol)
index = ["O&F"]
ingredients = pd.DataFrame({'weight': ['40 lbs'], 'price':[300], '$/lb' : 300/40}, index=index)
print(ingredients)

# price per month
container_year = 165 * 12
total_cost = reduce(lambda x, y: x+y, [elec_price(*cypress), container_year])
total = gain() - total_cost

#print(f"rental of 40x8.5x8 shipping container: ${container_year}/year")
#print("environment (soil, temp, RH) costs unknown.")
#print(f"for {cypress[0]}, {cypress[1]}W lights running {cypress[2]}h/day, ${elec_price(*cypress)}")
#print(f"total yearly cost = ${total_cost}")
#print("on the other hand:")
#print(gain(mode='quiet'))
#print(f"for a total of {total}")
