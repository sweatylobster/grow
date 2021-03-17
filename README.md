# grow
To specify the controlling elements of any grow operation.

# Elements a cannabis plant requires in its soil

1. Nitrogen, 
2. Potassium,
3. Phosphorous.

The minor nutrients are:
1. Calcium,
2. Iron,
3. Sulfur,
4. Zinc,
5. Boron,
6. Manganese,
7. Copper.

# Table of nutrient deficiency symptoms

TBA. 

# Labor concerns

Determining yield *a priori* renders a ***MASSIVE*** facility. For a 3-dimensional grow, light height adjustments and water distribution will have to be automated... Worker's compensation!!! The problem with employees anyway is that they have to "show up." But they don't. And they need to eat. But they don't. Worst of all, they complain about you not paying them. In short: there is no reason I should hire a human being. Human labor is overrated anyway. No employees!

# Automation

I/O = Input is measurement, output is action. {The input is read into the form anticipated by a conditional statement, whereupon the output is converted into a pragmatic action of a machine *in that quantity specified* by the conditional statement. Since optical evaluation of the plants is slated to be one of the inputs, even discrete nutrient programs (per plant) can be determined by conditional statements. 'Assessment' and 'correction' is the pragmatic translation of the terms 'input' and 'output'. Measurements fall under one of two categories: discrete or ambient. 

# Discrete measurements

Two examples of discrete measurements are PPM [of electrolytes] in its soil runoff, and the optical appraisal of a plant by a ML/statistical inference model. A given measurement might result in the following course of conditional statements, in Python. 
 - def doctor_mode(plant):
     - if plant.hue==deficiency[3]:
         - assessment = how_bad_is_it(pixel_to_area_ratio, ['Ca', 'K'])
	 - return "given ML assessment, nutrient PPM, & soil comp: plant lacks *x* units of Ca, and *y* units of K."
If a human must assemble the nutrient mix for each plant, there would be a 'nutrient report' for a block of plants whose respective cameras diagnose their deficiencies. If a machine does assemble it, perhaps through regulation of dispensers, or soil mix ratios which meet the requirements, the variables need to be stored and passed on to the appropriate function that interfaces with the machine controls, or voltages. 

# Ambient measurements

These are determined for *locales*; (temp, humidity, CO2). VPD for a volume of air: the relation between its current moisture, and its maximum capacity for moisture: their difference is VPD. [Look it up.](https://en.wikipedia.org/wiki/Vapour-pressure_deficit).

# ...Human labor, after all
Well, how the hell is a machine gonna transfer plants from their seedling pots to their vegetative pots, etc? Well, certain grow setups don't require this anyway. Also, discrete phenotype examination (if ML is undeployed/inadequate -- i.e., "a bitch" -- or the exhaustive-quantity-of-cameras is c-o-s-t-l-y) can be done really easily by a human. 

# Costs

The cyclical ones are electricity, maintenance, seeds + soil, real-estate. The one-time expenses are the electrical devices.

1. kWh/year
2. soil/cycle
3. RE/year

Can these be offset by revenue?

#Enabled questions/optimizations
How to optimize DLI for electricty costs? Where C_a = canopy_area:

1. efficiency = umol/m^2*s X 1/C_a
2. or E = PPFD * 1/canopy area

So a height must be selected for PPFD which gives not only optimal umol values, but greatest energy efficiency, lest kWh costs bite us in the ass. The larger the grow, the more noticeable this is. Once PPFD is converted into DLI, we can ask -- does the efficiency value stay the same? We should select a height so that the area of the cone base matches, as closely as possible, canopy area.
