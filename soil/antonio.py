# SI units :P
import math

# in mm
sr = 7.7
br = 30.0
ar = (sr + br) / 2
ar_sq = ar ** 2
y = 23.0 
print(f"{ar_sq} cm^2")

area = math.pi * ar_sq
# in cubic mm
vol = y * area
vol_m = vol/1000

print(f"{vol} mm^3")
print(f"{vol_m} m^3")
