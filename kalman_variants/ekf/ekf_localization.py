#!/usr/bin/env python3
"""
TODO: A detailed explanation of how this file work
Author: Jingxue Jiang <jingxue07@gmail.com> 
GitHub: https://github.com/jiangjingxue/kalman_filter_variants
"""
from __future__ import absolute_import

import numpy as np
import matplotlib.pyplot as plt

class EKFLocalization():
    def __init__(self,f_type:str):
        '''
        f_type: process model type: {differential,ackermann}
        f: nonlinear process model f(x,u,w)
        Jf: Jacobian matrix of f
        h: nonlinear measurement model h(x,v)
        Jh: Jacobian matrix of h 
        Q: process noise covariance matrix  
        W: process noise covariance matrix (WQW^T, W is identity matrix if additive noise)
        R: measurement noise covariance matrix
        V: measurement noise covariance matrix (VRV^T, V is identity if additive noise)
        x_hat: state estimate
        P: state covariance matrix
        K: kalman gain
        w_addi: artificial additive noise vector 
        v_addi: artificial additive measurement noise vector
        '''

        if f.lower() not in ["differential", "ackermann"]:
            raise ValueError("This process model is not supported at the moment")
    
    def process_model(self): 
        if self.f_type == "differential":
            self.f = np.eye(1)
        else:
            self.f = np.eye(1)

    # def measurement_model(self): 


        

    # def prediction(self):

    # def correction(self):

if __name__ == "__main__":
    n = noise.AdditiveNoise()