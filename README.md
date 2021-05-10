# grow
Business and science model for optimizing plant growth. Informed by Bruce Bugbee's work and Chandra et al's paper on a Mexican sativa strain. scientific framework for logging experiments. 

# X : Bruce Bugbee's Nine Cardinal Parameters
1. AMBIENT Temperature, humidity, wind, CO2. 
2. SOIL: Root-zone temp, nutrients, oxygen, water.

Filled in with [Chandra's values](https://ncbi.ncm.nih.gov/pmc/articles/PMC3550641/) in Table 2:

AMBIENT:
1. TEMP     - 30C
2. HUMIDITY - 70%
3. WIND     - ?
4. CO2      - 750 PPM

SOIL:
1. ROOT-ZONE TEMP - ?
2. NUTRIENTS      - ?
3. OXYGEN         - ?
4. WATER          - ?

PPFD, CO2, and temperature drive photosynthetic rate in tandem, which Chandra et al measure by a value PsubN. The relation between PPFD and nutrient exhaustion is not yet quantified, but can be inferred by electroconductivity of runoff(measured in PPM). An unrelated, but also import question is: What soil composition is optimized for yield?  The most significant emendation of Bruce's work which lies to us to perform is:

1. Quantifying nutrient consumption rate as a relation between:
   1. initial concentration of nutrients in soil
   2. amount of water in a day
   3. DLI
Which is the relation between PPFD|DLI, and run-off measured in electroconductive PartsPerMillion. The run-off is composed electroconductive nutrients "washed" out of the root-zone. These are already used by the plant.



# Approach
Pragmatic physics proposes a method of plant cultivation. PPFD, C02, TEMP, RH, all have been stated optimally, respectively as: 1500umol, 750umol/mol, 30C, 70%. We should optimize the environment for VPD as well. The only parameter whose optimal value needs to be determined is nutrition, and water (soil hydration, runoff values, etc.). Statistical inference of the environment under measurement will emend the plan. I suspect that for yield optimization to be a machine learning problem, I need to fully determine the applicability of time-series methods to machine learning problems, and whether they are suitable in predicting the yield of a given species given 

# TODO
1. Determine method of taking periodic measurements.
	1. Arduino logs analog inputs and runs continuously.
2. Convey measurements into a table.
	1. Conversion of arduino's output log into pd.DataFrame()
3. Determine the target from the dataset.
4. Specify mode of inferring yield.
	1. delta_kg (change in weight)
