# SEG-FAULT
### NOTE: Both programs have to be executed in Jupyter, for the graphs to be visible.

### Also, a GUI based version of the demonstrated application could not be developed because of time constraints and late registration.

#### Problem Statement
Participants will be provided with a dataset containing COVID-19 infections in a city of area 400 square kilometres over a period of 240 days. Using this data, each team is expected to come up with innovative solutions using this dataset.

#### Solutions/Applications:
The file “Graphical_Anlaysis.py” contains a menu-driven program, when prompted in a Jupyter instance, outputs a graph containing various details. This can be used to calculate the percentage of the number of people who are at risk because of COVID-19.

### Graphical Analysis
![TimeOfInfection](https://user-images.githubusercontent.com/69480337/99783166-1418c100-2b40-11eb-919b-a81db9c868e5.png)
![TimeOfReporting](https://user-images.githubusercontent.com/69480337/99783168-1418c100-2b40-11eb-8b86-e3d77dc0a46e.png)
![Respiratory](https://user-images.githubusercontent.com/69480337/99783163-13802a80-2b40-11eb-9fff-03e5a2d7c2bd.png)
![Outcome](https://user-images.githubusercontent.com/69480337/99783155-124efd80-2b40-11eb-8be2-53e1a0e2ec3a.png)
![Age](https://user-images.githubusercontent.com/69480337/99783151-10853a00-2b40-11eb-94ca-affdbe0672f9.png)
![BP](https://user-images.githubusercontent.com/69480337/99783152-11b66700-2b40-11eb-8435-555b88f8aabb.png)
![Diabetes](https://user-images.githubusercontent.com/69480337/99783153-11b66700-2b40-11eb-9dcc-4be9496e262b.png)

### Prediction Graphs
<p align="center">
 <img width="460" height="300" src="https://github.com/dpsbangalorenorth/SEG-FAULT/blob/Prediction-Graphs/Population%2BCases%20Density.png">
</p>
<p align="center">**Population+Cases Density**</p>
<p align="center">
 <img width="460" height="300" src="https://github.com/dpsbangalorenorth/SEG-FAULT/blob/Prediction-Graphs/ProbabilityofInfection.png">
</p>
<p align="center">**Probability of Infection Heat Map**</p>

#### Algorithms Used:
<p>DBSCAN (Density-Based Spatial Clustering of Applications with Noise)</p>
<p>OPTICS (Ordering Points to Identify Clustering Structure)</p>
