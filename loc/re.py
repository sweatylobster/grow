# central problem is value per unit of real estate
# to determine this we need the price/g
# for which it's necessary to determine yield:
# the factors guiding plant morphology: lights, trellising, root depth
# we can grow in three dimensions -- the choice must be to optimize for volume
# the leaves are being accelerated down by gravity, and so only grow to a certain proportion --
# the plants whose roots are deepest have developed the most robust leaves  


# the general thing that i need per three types of plant: seedling, veg, flowering
# vol, light(kWh), soil
# the space of the container has ambient conditions that are unique


class plant():

    # in L
    volumes = {'solo': 0.5, 'young' : 11.4, 'rest' : 28.3}

    # vol is for soil volume, leaf is leaf area
    def __init__(self, vol, leaf, stem):
        self.vol = vol 
        self.leaf = leaf
        self.stem = stem

class container():

    # all quantities in SI units -- not yet for cost analysis
    def __init__(self, x, y, z, lights, ventilation, humidifier):
        self.x = x
        self.y = y
        self.z = z
        self.lights = lights
        self.ventilation = ventilation
        self.humidifier = humidifier

    def __vol__(self):
        return self.x * self.y * self.z
    
    def __elec_cost__(self):
        # avg. price per kWh in CA
        price = .20
        kWh = self.lights

    def cost(self):
        return self.elec_cost()

d = container(40, 8.5, 8)
