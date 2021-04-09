import numpy as np

class ingredient():
    
    def __init__(self, density, nutrients, portion):
        self.density   = density
        self.nutrients = nutrients
        self.portion   = portion
        self.kg_per_L  = self.portion * self.density

    def total_nutrients(self, volume):
        kg = self.kg_per_L * volume
        return kg * nutrients

# I is ingredient, E is element,
# algebraically:
# density(I) * ratio(I/mix) * vol(mix) = kg(I)
# kg * %(E) = kg(E)

# 18 liters
volume = 6 * 3
dens = np.array([2.72/13.2, 2.27/3.2, 1.8/1.89, 4.5/28])
ratio = np.array([.93, .004, .046, .02])
kg = dens * ratio * volume

# elements
N    = np.array([.3, 6.0, 1.0, 6.0])
P    = np.array([.45, 1.0, 0.0, 3.0])
K    = np.array([.05, 2.0, 2.0, 3.5])
Ca   = np.array([1.0, 0.0, 1.0, 7.0])
Mg   = np.array([0, 0, .5, 0.7])
S    = np.array([0, 0, 2.0, 2.5])
Fe   = np.array([0, 0, 0, 0.2])

nutrients = np.array([N, P, K, Ca, Mg, S, Fe])

stuff = kg * nutrients
print("N-P-K-Ca-Mg-S-Fe, in kg:")
print(np.sum(stuff, axis=1) / 6)
