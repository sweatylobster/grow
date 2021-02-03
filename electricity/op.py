def hor_ft(rows=3, aisle_size=4, row_size=4):
    'how many feet required along x-axis?'
    aisles = rows + 1
    aisles, rows = aisles * aisle_size, rows * row_size
    return (aisles + rows)

def ver_ft(stacks=3, stack_size=7):
    'how many feet required along y-axis'
    return stacks * stack_size

def depth(units=8, ft_to_walls=12, ft_per_unit=4):
    'where each of the {0} unit is 4 ft:'.format(units)
    depth = ft_per_unit * units + ft_to_walls
    return depth

def operation_dimensions(rows=3, stacks=3, units=8):
    x = hor_ft(rows)
    y = ver_ft(stacks)
    z = depth(units)
    op = operation_yield(rows, stacks, units)
    return 'With {0} 4x4x7s in each of {1} rows stacked {2} times: {3} x {4} x {5} ft.'.format(units, rows, stacks, x, y, z)

def operation_yield(rows=3, stacks=3, units=8):
    'How many pounds can I expect?'
    quant = str(rows * stacks * units)
    return 'With {0} rows, {1} stacks, and {2} pounds, expect {3} lbs.'.format(rows, stacks, units, quant)

def sq_ft_req(rows, units):
    x = hor_ft(rows)
    z = depth(units)
    return str(x * z) + ' sq. ft.'

def light_price(num_LEDs=1, ppkwh=.20, adjust=True, hours_on=24):
    '''
Electricity price for a number of LEDs.
If called with adjust=True,
avg. energy consumption is lowered for the cycle.
'''
    # each LED is .425 kW
    kW = .425
    # if we adjust, we factor in reduced light, where 14.5 is average of
    #  hrs * wks + hrs * wks; averages to 14.5; common unit is weeks, so / 8
    # ((16 * 5) + (12 * 3)) / 8 == 14.5 hours. kW * hours = kWh/day
    if adjust:
        kWh_day = kW * 14.5
        kWh_year = kWh_day * 365.25
    else:
        kWh_year = kW * hours_on * 365.25
        print('Where light is on for {0} hours:'.format(hours_on))
    print('adjust:', adjust, ', kWh/year per light: ', kWh_year)
    result = kWh_year * ppkwh * num_LEDs 
    return 'For {0}, {1} kW LEDs, at ${2}/kWh: ${3} per year'.format(num_LEDs, kW, ppkwh, result) 

def operation_light_costs(quant, full_blast=False):
    if full_blast == True:
        return light_price(num_LEDs=quant, adjust=False)
    else:
        return light_price(num_LEDs=quant, adjust=True)

def ventilation_costs(n, W=100, adjust=True):
    # make both of these into one electricity cost calculator
    # watts = {'fan' : 100, 'led', : 425}
        kWh_year = kWh_day * 365.25
    else:
        kWh_year = kW * 24 * 365.25
    result = n * .20 * kWh_year
    return f'For {n} {kW} kW fans running 14.5h/day, at $.20/kWh, ${result} per year.'

#print('x: ', hor_ft(3))
#print('y: ', ver_ft())
#print('z: ', depth())
#print("facility's minimum requirements: ", operation_dimensions()) 
#print('square feet: ', sq_ft_req(3, 8))
#print(light_price(num_LEDs=72, adjust=False))
#print(light_price(adjust=False))
print(operation_light_costs(72))
print(operation_yield())
print(ventilation_costs(72))
