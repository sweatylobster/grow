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

I/O = Input is measurement, output is control. Every plant is optically monitored, since nutrients go into *their* soil. Lotta baby cameras that are color-accurate/sensitive. Environmental stuff (temp, humidity, VPD) are determined for *locales*. What other input do we need for our if-then automated event flow? Watering, lights, ventilation. 

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
