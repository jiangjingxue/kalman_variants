
# kalman_variants - a selective set of variants of nonlinear Kalman Filter
**Maintainer Status: Actively maintained**

<img src="./doc/ekf.gif" width="360" height="270" style="border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);">

## Summary
`kalman_variants` implements several Kalman filter nonlinear variants and provides a a wealth of examples with a specific goal for educational purpose. Every single line of code is annotated in a detailed manner and the examples are developed with a thematic focus on state estimation applications for robot and autonomous systems. You also have free access to a beginner-friendly kalman filter implementation guide at https://github.com/jiangjingxue/kalman_filter_variants/doc/ to go along with the code to accelerate your learning. 
<br/> <br/>
At the moment, the package implements 
* Extended Kalman Filter (EKF)
* Error State Extended Kalman Filter (ESEKF) 
* Unscented Kalman Filter (UKF)

And the following vehicle motion model in both discrete and continuous formulation
* Kinematic Bicycle Model  
* Kinematic Differential Drive Model 
* Kinematic Ackermann Model
* Dynamic Bicycle Model

## Installation
Download the source via git clone 
````
cd <your directory>
git clone https://github.com/jiangjingxue/kalman_filter_variants.git
python setup.py install
````
## Basic Use
First, import the filters and helper functions.
````python
import numpy as np
from kalman_variants.ekf import EKFLocalization
from kalman_variants.common import AddictdeNoise
````
Create the filter 
````python
my_ekf = EKFLocalization()
````



