# Ring-like clustering on noisy data

## Table of content

1. **Introduction**
   - Description of the Problem
   - Proposed Solution: Clustering

2. **Guide of Use**
   - 2.1 Generate Experiment
   - 2.2 Run Algorithm Over Experiment
   - 2.3 Revisit Experiment Result
   - 2.4 Evaluate New Points

## 1 Introduction.

This study addresses a simplified version of a problem encountered in the LHCb experiment at CERN involving the RICH (Ring Imaging Cherenkov) detectors. These detectors aim to identify circular or elliptical patterns resulting from Cherenkov radiation. We abstract the problem to finding optimal ring configurations for a given dataset within a defined spatial range, accounting for noise. Our goal is to minimize error in fitting the data.   


![image](https://github.com/LuisMelladoDiaz/ring-clustering/assets/93400291/e7ddbe4e-8733-4f2c-9e33-6e706f75db3d)

The problem of fitting a circle to a collection of points in the plane holds significance in various domains. The main goal of this study is to design, implement, understand and analyze an algorithm that searches for circumference and takes uncertainty explicitly into account. 

### Description of the Problem.
In general, suppose that we have a collection of points of n ≥ 3 points in a 100x100 2D-space labeled (x1, y1), (x2, y2), . . . , (xn, yn). Our basic problem is to find a circle that best represents the data in some sense. With the circle described by (x − a) 2 + (y − b) 2 = r 2, we need to determine values for the center (a,b) and the radius r for the best fitting circle.
### Proposed Solution: Clustering.
Clustering is an unsupervised learning technique used to group data points into classes (clusters) based on similarity. The partition into subsets aims to discover patterns or hidden insights previouly unknown.
Each cluster will be represented by a circumference defined by a center (a,b) and a radius r, while each point (x,y) is associated with all clusters but with a different membership degree.


## 2 Guide of use
In order to start the use of the program you just need to clone the repository and run main.py. A small window will pop up and you will be presented with 4 options: Generate Experiment, Run Algorithm Over Experiment, Revisit Experiment Result and Evaluate New Points. In this guide we will break down the purpose of these 4 tools and how they are used.

### 2.1 Generate Experiment

For the purpose of facilitating the study and produce a high number of experiments, a experiment generator tool was designed. This tool receives the following inputs:        
**1.    Maximum number of points per circular pattern:** Integer number that limits how many points any circular pattern can have.     
**2.    Number of circular patterns:** Input here an integer number representing how many circular patterns are going to be generated.       
**3.    Maximum uncertainty:** A float number that represent the distance a point can deviate from the circular pattern. In other words, the maximum allowed noise.        
**4.    Experiment title:** A string that will serve as a name to identify the experiment.         

<img src="https://github.com/LuisMelladoDiaz/ring-clustering/assets/93400291/87c8c223-1892-4496-be27-66064a45f4dc" alt="Generate Experiment" width="600"/>

The tool outputs a .csv file containing a series of randomly generated points that follow the restrictions imposed by inputs 1, 2 and 3. This points compose an experiment over which you can run the algorithm and evaluate the results.

### 2.2 Run Algorithm Over Experiment
To run the algorithm over a generated or handcrafted experiment you need to provide:
-	The title of the experiment, in order to scan the points from the .csv file.
-	Number of clusters K.
-	Initialization type.
-	Maximum number of iterations.
-	Maximum allowed noise. That is, how far must a point be from a cluster to be considered noise.
-	Maximum cluster equivalence rate. This parameter is used to remove cluster that are too close to each other. The value ranges from 0.0 to 1.0 but I recommend using always values greater than 0.95.

When you are ready click on execute algorithm. A figure will pup up showing the problem you selected and the initial classification. Close the figure and wait a little. When the algorithm finishes the final classification of the points will be shown.

<img src="https://github.com/LuisMelladoDiaz/ring-clustering/assets/93400291/f29cf096-89cb-45b6-961e-913fb2558abe" alt="Run Algorithm Over Experiment" width="600"/>



What these parameter are and how they relate to the different stages of the algorithm is explained in depth in section II of the Ring-like_Clustering_Scientific_Paper that you can find in this repository.
When the algorithm is run over an experiment a .csv file is generated so the results of the experiment can be revisited. This time the .csv do not only contain the x and y coordinates of a series of poins but also the cluster they belong to (represented by a color).

### 2.3 Revisit Experiment Result
If you want to see the results of an experiment again you can just click on "Revisit Experiment Results". Provide the csv file name and hit "Results".
<img src="https://github.com/LuisMelladoDiaz/ring-clustering/assets/93400291/85bf179e-4cca-4e66-9ebe-bcc2c9945891" alt="Revisit Experiment Result" width="600"/>


### 2.4 Evaluate New Points
Once the results of an experiment have been produced it is natural to introduce new points and evaluate them to know to which cluster or class they belong to.
To do so, we can use the “evaluate new points” tool that was implemented. It is necessary to provide:       
**1.    The experiment results title**: Necessary to scan the experiment resuls and load the points and clusters. Please do not confuse a experiment file with a experiment results file.         
**2.    A list of the new points** to evaluate in the format [(x1,y1), (x2,y2), … , (xn,yn)]. Be careful, there must be a space between the commas and the next point in the list.        
Finally, the classification of the new points will be shown. When you evaluate new points the output of the evaluation is not stored in the experiment results file.          


<img src="https://github.com/LuisMelladoDiaz/ring-clustering/assets/93400291/94a2b5b8-6768-4843-b4bd-a5f4ad68563f" alt="Evaluate New Points" width="600"/>









