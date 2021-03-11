from functools import reduce

def gain(ppp=2000, ppc=20, cpy=56//12):
    # income per year
    ipy = ppp * ppc * cpy
    return f"at {cpy} (complete) cycles/year, producing {ppc}lbs each, at ${ppp} a pound: ${ipy}"

def elec_price(n, W, hrs):
    kW = n * W * 0.001
    # 20 cents a kW/h in CA
    p = .20
    day = kW * hrs
    year = day * 365.25
    ppy = year * p
    return ppy
    #return f'kWh costs of {n}, {W}W lights a year: ${ppy}'

def soil_price(price, volume, plants):
    total = price * plants * volume
    return total

lights = (72, 480, 15)
cypress = (20, 725, 15)

# price per month
container_year = 165 * 12
total = reduce(lambda x, y: x+y, [elec_price(*cypress), container_year])

print(f"rental of 40x8.5x8 shipping container: ${container_year}/year")
print("environment (soil, temp, RH) costs unknown.")
print(f"for {cypress[0]}, {cypress[1]}W lights running {cypress[2]}h/day, ${elec_price(*cypress)}")
print(f"total yearly cost = ${total}")
print("on the other hand:")
print(gain())
