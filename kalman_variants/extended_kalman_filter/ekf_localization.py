#!/usr/bin/env python3
"""
TODO: A detailed explanation of how this file work
Author: Jingxue Jiang <jingxue07@gmail.com> 
GitHub: https://github.com/jiangjingxue/kalman_filter_variants
"""
import numpy as np
import matplotlib.pyplot as plt
from kalman_variants.motion_models import MotionModels

class EKFLocalization():
    def __init__(self,f_type:str, n_type:str):
        '''
        f_type: process model type: {differential,ackermann}
        n_type: noise type: {additive, multiplicative, or none}
        f: nonlinear process model f(x,u,w)
        Jf: Jacobian matrix of f
        h: nonlinear measurement model h(x,v)
        Jh: Jacobian matrix of h 
        Q: process noise covariance matrix  
        W: process noise covariance matrix (WQW^T, W is identity matrix if additive noise)
        R: measurement noise covariance matrix
        V: measurement noise covariance matrix (VRV^T, V is identity if additive noise)
        x_hat: state estimate vector
        P: state covariance matrix
        K: kalman gain
        w_addi: artificial additive noise vector 
        v_addi: artificial additive measurement noise vector
        '''

        if f_type.lower() not in ["differential", "ackermann"]:
            raise ValueError("This process model is not supported at the moment")
        if n_type.lower() not in ["additive", "multiplicative","multiplicative_colored","none"]:
            raise ValueError("Invalid noise type")
    
    def process_model(self): 
        if self.f_type == "differential":
            self.f = np.eye(1)
            self.n = 3
            self.m = 2
        else:
            self.f = np.eye(1)

    # def measurement_model(self): 


    def prediction(self, u): 
        # w = AdditiveNoise(self.n).zero_mean_gaussian
        # self.x_hat = self.f(self.x_hat,u) + w 
        pass 


    # def correction(self):



def main():
    '''
    Allowed actions for users
    -------------------------
    - should select a specific vehicle model. Available models: differential, ackermann 
        -> 
    - should provide a initial state estimate and a initial state covariance 
    - should provide the 2 of the 4 noise covariances, namely the process noise 
    covariance Q and the measurement noise covariance R

    Disallowed actions for users
    ----------------------------
    - User don't get to set the motion model 
        -> Only few vehicle motion model used in practice, hide this detail
        -> 
    The size of the noise covariances is constrained by the size of the state vector 
    and measurement vector, which is subsequently constrained by specific vehicle type as
    well as the sensor model. So probably a good idea to not let the user to set a 
    arbitrary-sized noise covariances. 
    - User dont

    '''

    vehicle_model = "differential"
    noise_type = "additive"
    EKFLocalization(f_type=vehicle_model,n_type=noise_type)

if __name__ == "__main__":
    main()
    