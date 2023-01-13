# surfs_up

## Overview of the analysis: 
### Purpose
The reason for this analysis is to examine weather trends (precipitation, temperature) in June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.

The analysis was done by explaining the structures, interactions, and types of data of a provided dataset, differentiatiating between SQLite and PostgreSQL databases, using SQLAlchemy to connect to and query a SQLite database and using statistics like minimum, maximum, and average to analyze data, and designing a Flask application using data.

### Resources
- Data Analysis Tools: SQLAlchemy, Object Relational Mapper, Pandas, Numpy
- Software: SQLlite, Python 3.9.2, Flask, Jupyter Notebook

## Results: 
### Summary Statistics for June
- Mean Temp in June is 75
- Max temp in June is 85
- Min Temp in June is 64 
![Summary Statistics for June](https://github.com/pfrivas/surfs_up/blob/main/Resources/June%20Statistics.png)
### Summary Statistics for December
- Mean Temp in December is 71
- Max temp in December is 83
- Min Temp in December is 56
![Summary Statistics for December](https://github.com/pfrivas/surfs_up/blob/main/Resources/December%20Statistics.png)

## Summary: 
### Result Summary
- The mean temperatures for June (75) and december (71) are only 4 degrees different however the month of december has more variation in temperatures and an 8 degree difference in the minimum temperature (56 vs 64 in June) which means that based on this data alone the shop could still be open in the winter and there would still be a demand for ice cream but maybe the shop could have shorter hours in december. 

### Additional Querues that could be performed to gather more weather data for June and December.
- The first query that could be conducted is narrowing in on the temperature changes within different areas of the island instead of looking at the island as a whole in order to determine the best location on the island to set up the shop
- The second query that could be conducted are other weather conditions besides temperature that could affect the buisness year-round such as precipitation, wind speed, high vs. low tide, etc. in order to further analyza weather the shop could be sustainable year round.
