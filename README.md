# grow
To automate the optimization of any grow operation.

# Bruce Bugbee's Nine Cardinal Parameters
1. ABOVE GROUND: Temperature, humidity, wind, CO2. 
2. BELOW GROUND: Root-zone temp, nutrients, oxygen, water.

# Approach
Because plant growth is a physical phenomenon, it seems proper to the realms of organic chemistry and physics to set forth the optimal approach for the cultivation of a given species. "Given these underlying quanta, to do..., in order to attain..." But this is a practical question, and not a living scientific process. What is being created here is a method for *further* refining, in real time, an approach tending towards that definite goal. To this end we propose statistical inference. Then plant growth will be stated as a machine learning problem. A possible target is yield, another, flavor. 

# Questions
1. Accuracy of ML prediction: is it advantageous to implement manifold approaches of the same data? Or, for a given dataset, is there one and only one preferable model?

Is the model determined by the dataset? certain algorithms are not usable when the targets and features have a certain relation to each other. Would there be advantages to schematizing diverse modes of recording data that would be appropriate to the requirements of manifold ML models? Is there a class of machine learning problem (e.g. classification, regression) which is almost always preferable? Are there algorithms, which, given appropriately cleaned data, tend generally to perform better than other Does this "preferable" refer only to ease of implementation in Python? Ultimately, ML is statistical inference -- I have a hard time imagining that statistical 

# Contests
1. The question is almost clear. Because a ML model is tailored to the data, which is of a certain type already, already a selection has been made, as to which type of problem the model is addressing (classification, regression). The answer depends on whether, for example, regression is an "easier" problem. In other words, is the real optimization data preparation, and not model selection? Are there algorithms which will tend to outperform others, if only the data is prepared a certain way? In what sense is one class of machine learning problem preferable to another?

# TODO
1. Determine method of taking periodic measurements.
2. Convey measurements into a table.
3. Determine the target from the dataset.

# PROPOSALS
1. SBC receives input from devices which record the 9 cardinal parameters, periodically logs them.
2. The log is either in the form of a .csv, or is easily converted into it. Then it becomes a DataFrame, and is labeled. The mode of interpreting and representing the values of 
