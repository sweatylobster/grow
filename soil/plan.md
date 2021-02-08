# Master Mark's Program

We have this google doc resource to guide the grow, but is it enough? To grow well, of course. For quantitative predictions, hardly. Our framework must arithmetically describe the relation between PPFD and nutrient exhaustion. What's required to do this?

We need quantity of nutrients, and we can use PPM. In fact, the doc mentions the use of PPM to measure run-off for concentration of nutrients. Whether we want to use PPM ultimately depends on whether it's more _convenient_ to adopt, than say, mol mol^-1. PPM is a non-dimensional unit -- so we can do whatever units we want, which is not for the best; PPM being general doesn't elucidate its use case. 

# Back to Bruce: The Nine Cardinal Parameters

To list them once again, they are:

AMBIENT:
1. TEMP
2. HUMIDITY
3. WIND
4. CO2

SOIL:
1. ROOT-ZONE TEMP
2. NUTRIENTS
3. OXYGEN
4. WATER

Bruce's work shows that PPFD drives the growth cycle. Yield is directly related to DLI. Furthermore, the relationship between efficiency and DLI is linear. We're left wondering, however, what the relation between PPFD and nutrient exhaustion is. That is: what quantities in soil are directly proportional to yield? The ratio of PPFD : H20 | C02 exhaustion is also entirely unknown. The most significant emendation of Bruce's work which lies to us to perform is:

1. Quantifying soil constituents in SI units.
   1. noting that percentages eventually give grams,
   2. g(nutrient)/g(soil) is our preliminary unit.
   3. What device enables direct measurement of particular soil constituents?
   4. This will enable quantifying plant metabolism when we compare start values (of our unit of choice) to run-off values (in identical units).
2. Showing the relation between PPFD|DLI : 


Really, what we want is to quantify is each the plant's qualitatively distinguishable metabolic events. This must be exhaustively, empirically verified if we expect the quantities to have inferential power. Is this beyond our power? Well, is there not already a qualitative theory of plant metabolism, associated with quantities of metabolic products, in known relations? There must be. So what's left for us to determine is the change in quantities determined by the qualitatively distinguishable metabolic events. 

# Measurement devices

Rule number one of doing business: get your shit from China. China, however, is very far. Since all of our measuring devices have to be here soon, we can't do this -- unless we are doing it pre-emptively, for our facility. The TDS tester I have will only be of use in regulating the plant's water supply -- I don't see an alternative heuristic application. It is essential, though, to make sure that the water given to the plant has no minerals, since the minerals would inhibit root function. So far, a dull DataFrame of what to order comprises `units.py`. It is of primary importance that we are able to measure ambient CO2. From the paper of [Chandra et al.](https://ncbi.ncm.nih.gov/pmc/articles/PMC3550641/), PPFD oughtta be ~1500 umol/m^2*s, and CO2 concentration should be, optimally, around 750 umol/mol, where the latter mol is of quantity of air. Chandra's finding should be translated into PPM, since this measurement is ubiquitous.

# Our plan -- learn statistics to draw inferential power from a 'gross' collection of data

While Bruce and Chandra give us our baseline, Master Mark's program must be quantitatively expressed. In Chandra et al's' paper, I was struck by the use of statistical methods to determine which quantities had a correlation -- what the hell was I doing before this? Now, we can expect to draw meaningful conclusions from whatever data we gather. These conclusions will apply generally, by the (still mysterious) value r that recognizes the 'scope' of its applicability for inference. We want _quantized causes_. I'm starting "All of Statistics," by Larry Wasserman. Stats seem to be an emendation of analysis and synthesis, as applied to EMPIRICAL OBJECTS. In statistics, _a posteriori_ objects are characterized without having to 'ransom' back the formal qualities which, in intuition, set it apart from all other objects. Geometry is expanded by animating, in a regulated manner, _a priori_ intuitions. The understanding then The arithmetic determination of empirical objects has typically required that empirical objects be divested of their particular character -- for the sake of mathematical articulability -- and hence, inferential power in accordance with the PNC. This is because arithmetic contradictions are spotted easily, since they are self-identical. 2 + 2 = 5 is not self-identical, and the meaning, both of 2 and +, is so strictly regulated that it grants inferential power. Statistics promises a way of arithmeticizing(?) empirical objects, not qua _a priori_ objects -- which, when considering the 'prudent' mode of Euclid's presentation, sort of loses its meaning -- but qua -- what? Freakonomics, bias correction, etc. -- all point to the fact that we're considering the particular objects, though quantified, and rationally related to other objects, as themselves in statistics.
