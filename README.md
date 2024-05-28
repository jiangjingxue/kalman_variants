
# kalman_variants - a selective set of Nonlinear Kalman Filter Variants
**Maintainer Status: Actively maintained**

<img src="./doc/ekf.gif" width="360" height="270" style="border-radius: 10px box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);">

## Summary
`kalman_variants` implements several Kalman filter nonlinear variants with robtics applications in mind. This package specifically targets state estimation applications for robot and autonomous systems and includes detailed annotated code for every implementation of the kalman filter. You will also have free access to ahighly digestible kalman filter fundamentals book at [jiangjingxue/Kalman_filter_variants/doc/Kalman_blue.pdf](https://github.com/jiangjingxue/Kalman_filter_variants/blob/9ae24f5df8738824c020d176d75c514b8e39707d/doc/Kalman_blue.pdf) to go along with the annotated code to accelerate your learning. 
<br/> <br/>
At the moment, this package implements 
* Extended Kalman Filter (EKF) w/ landmark-localization tutorial
* Error State Extended Kalman Filter (ESEKF) 
* Unscented Kalman Filter (UKF)

Moreover, it implements the following vehicle motion model in both discrete and continuous formulations
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



