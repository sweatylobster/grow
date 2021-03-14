# trying to make a container to scale
# board was directly measured, container was inferred from the difference of outside, inside

# inches
wall_thickness = {'board' : 3/16, 'container' : 2}
wt = wall_thickness

# here go the x,y,z dimensions of the container


def lit_in(feet):
    scale = 1.5
    return [x * scale for x in feet]

twenty = (20, 8, 8.5)
tw_doors = (7.6666, 7.4166)
forty = (40, 8, 8.5)
print(lit_in(twenty))
print(lit_in(tw_doors))
