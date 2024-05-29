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
    def __init__(self,sys,mm):
        '''
        f: nonlinear process model f(x,u,w)
        Jf: Jacobian matrix of f
        h: nonlinear measurement model h(x,v)
        Jh: Jacobian matrix of h 
        Q: process noise covariance matrix  
        W: process noise covariance matrix (WQW^T, W is identity matrix if additive noise)
        w: process noise  
        R: measurement noise covariance matrix
        V: measurement noise covariance matrix (VRV^T, V is identity if additive noise)
        v: measurement noise
        x: state estimate vector
        P: state covariance matrix
        K: kalman gain
        '''
        self.f = sys['f']
        self.x = sys['x']
        self.P = sys['P']
        self.Q = sys['Q']
        self.R = sys['R']


        self.w = np.zeros((self.x.size, 1))
        self.W = np.eye(self.x.size)
    
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
    - user should select a specific vehicle model. Available models: differential, ackermann 
    - user should provide a initial state estimate and a initial state covariance 
    - user should provide the process noise covariance Q and measurement noise covariance R 
        -> size of the noise covariances matrices are constrained by the state vector size
           and the measurement vector size, which is subsequently decided by the specific vehicle motion model as
           and the sensor model. 
            -> TODO: perform dimension check inside init() 
    - user will have the option to choose if the nonlinear system should be excited by an 
    additive or multiplicative noise. 
        -> default: no noise 
        -> TODO: add enable_additive_noise() and enable_multiplicative_noise()
        -> TODO: add methods to transform the current model to a noisy model
        -> possibly need to create a new jacobian matrix as well

    Disallowed actions for users
    ----------------------------
    - User don't get to set the process model matrix 
    - User don't set up the noise w,v and their covariances W,V from users 
        -> only request w,v in enable_additive_noise() method 
        -> request w,v, W,V in enable_multiplicative_noise() method 
    - User don't set up the observation matrix 
        -> TODO: hard-encode H inside the EKFLocalization class 
    - User don't set up the measurement vector 

    '''

    # build system
    sys = {} 

    # select motion model
    # provide an initial state estimate and its covariance
    # set up the noise covariances
    motion_models = MotionModels()
    sys['f'] = motion_models.generalized
    sys['x'] =  np.array([[1], [1], [np.pi]])
    sys['P'] = 0.1 * np.eye(3)
    sys['Q'] = np.diag(np.power([0.015, 0.01, 0.01], 2))
    sys['R'] = np.diag(np.power([0.5, 0.5], 2))

    ekf = EKFLocalization(sys,motion_models)
    # ekf.enable_additive_noise()
    # ekf.run() 

if __name__ == "__main__":
    main()
    