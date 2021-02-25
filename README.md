# grow
For an arithmetically-guided grow operation.

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

Here goes the section where we say how we can tell WITH OUR EYEBALLS what nutrients our lady requires. Perhaps(!) even those amounts in which she needs them *forthwith!*

# Quantities, rates?

How much of each of the specified elements is required, *on average*? We need quite the sample size to determine this, and data is wanting since people are either lazy or secretive. Hopefully, secretive has nothing to do with glands here.

# Labor?

Determining yield *a priori* renders a ***MASSIVE*** facility. Just run "op.py", and be amazed. Nothing that can't be handled... it's just, serious man-power is required. If we do a 3-dimensional facility, how high up are we gonna go? Adjusting light height would have to be automated, water distribution too. The problem with employees anyway is that they have to "show up." But they don't. And they need to eat. But they don't. Worst of all, they complain about you not paying them. In short: there is no reason I should hire a human being. Human labor is overrated anyway. No employees!

# Automation

I/O = Input is measurement, output is action. {The input is read into the form anticipated by a conditional statement, whereupon the output is converted into a pragmatic action of a machine *in that quantity specified* by the conditional statement. Since optical evaluation of the plants is slated to be one of the inputs, even discrete nutrient programs (per plant) can be determined by conditional statements. 'Assessment' and 'correction' is the pragmatic translation of the terms 'input' and 'output'. Measurements fall under one of two categories: discrete or ambient. 

# Discrete measurements

Two examples of discrete measurements are PPM [of electrolytes] in its soil runoff, and the optical appraisal of a plant by a ML/statistical inference model. A given measurement might result in the following course of conditional statements, in Python. 
 - def doctor_mode(plant):
     - if plant.hue==deficiency[3]:
         - assessment = how_bad_is_it(pixel_to_area_ratio, ['Ca', 'K'])
	 - assessment as a
	 - return "given a: plant lacks *x* units of Ca, and *y* units of K."
If a human must assemble the nutrient mix for each plant, there would be a 'nutrient report' for a block of plants whose respective cameras diagnose their deficiencies. If a machine does assemble it, perhaps through regulation of dispensers, or soil mix ratios which meet the requirements, the variables need to be stored and passed on to the appropriate function that interfaces with the machine controls, or voltages. Bits and voltages... 

# Ambient measurements

These are determined for *locales*; (temp, humidity, CO2). VPD for a volume of air: the relation between its current moisture, and its maximum capacity for moisture: their difference is VPD. [Look it up.](https://en.wikipedia.org/wiki/Vapour-pressure_deficit).

# ...Human labor, after all
Well, transferring plants from their seedling pots to their vegetative pots, (but certain grow setups don't require this anyway). Phenotype examination (if ML is undeployed/inadequate -- i.e., "a bitch" -- or the exhaustive-quantity-of-cameras is c-o-s-t-l-y). 

# Costs

The cyclical ones are electricity, maintenance, seeds + soil, real-estate. The one-time expenses are the electrical devices.

1. How much does ventilation cost?/year
2. How much does soil cost?/cycle
3. How much do lights cost?/year

#Enabled questions
Given PAR, photosynthetically active radiation, in units of PPFD (umol/m^2 * s), to convert it into DLI(mol/m^2 * day), and then: how to optimize DLI for electricty costs?

1. What is the ratio of yield value to light costs? (per cycle)
2. What is the ratio of yield value to ventilation costs? (per cycle)
3. What is the ratio of yield value to electricity costs?
