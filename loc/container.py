# for modeling purposes

# inches
wall_thickness = {'board' : 3/16, 'container' : 2}

def lit_in(feet, thickness):
    # since the cargo container thickness is 2 inches
    scale = thickness * 6
    return [x * scale for x in feet]

twenty = (20, 8, 8.5)
tw_doors = (7.6666, 7.4166)
forty = (40, 8, 8.5)
print(lit_in(twenty, 3/16))
print(lit_in(tw_doors, 3/16))
