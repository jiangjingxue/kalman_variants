#!/usr/bin/env python3
"""
TODO: A detailed explanation of how this file work
Author: Jingxue Jiang <jingxue07@gmail.com> 
GitHub: https://github.com/jiangjingxue/kalman_filter_variants
"""
import scipy 
import numpy as np

class EKF():
    def __init__(self,sys,mom,mem):
        # System check:
        # 1. check for compatibility between the motion model and the measurement model
        # Matrix dimension check:
        # 2. check for initial state X and state covariance P 
        #    - X is a X_dim dimensional vector (the motion model (mom) enforces a constraint on X_dim)
        #    - P is a X_dim by X_dim matrix 
        # 3. check for noise covariances Q and R
        #    - Q is a X_dim by X_dim matrix
        #    - R is a z_dim by z_dim matrix (the measurement model (mem) enforces a constraint on z_dim)
        # 4. check for Jacobian matrix Jf and Jh
        #    - Not checked here, should be performed inside the model classes
        if mom.name not in mem.compatibility_list:
            raise ValueError(f"The {mom.name} motion model is not compatible with the {mem.name} measurement model")
        if sys['X'].shape[0] != mom.X_dim:
            raise ValueError(f"The initial state estimate X should be a {mom.X_dim} by 1 column vector")
        if sys['P'].shape != (mom.X_dim,mom.X_dim):
            raise ValueError(f"The state covariance P should be a {mom.X_dim} by {mom.X_dim} matrix")
        if sys['Q'].shape != (mom.X_dim,mom.X_dim):
            raise ValueError(f"The process noise covariance Q should be a {mom.X_dim} by {mom.X_dim} matrix") 
        if sys['R'].shape != (mem.z_dim,mem.z_dim):
            raise ValueError(f"The measurement noise covariance R should be a {mom.z_dim} by {mom.z_dim} matrix")         
        '''
        mom: motion model object
        mem: measurement model object 
        f: nonlinear process model f(x,u,w). f is a nonlinear state transition function 
           that describes the evolution of states x from one time step to the next
        F: Jacobian matrix of f
        h: nonlinear measurement model h(x,v). The nonlinear measurement function h 
           relates x to the measurements z at time step k
        H: observation matrix, Jacobian of h 
        Q: process noise covariance matrix 
        R: measurement noise covariance matrix
        W: process noise Jacobian (WQW^T, W is identity matrix if additive noise)
        V: measurement noise Jacobian (VRV^T, V is identity if additive noise)
           w and v are the zero-mean, uncorrelated process and measurement noises
        X: state estimate vector
        P: state covariance matrix
        K: Kalman gain
        z: measurement vector
        innov: innovation 
        '''
        self.f = mom.f     
        self.F = mom.Jf                             
        self.h = mem.h
        self.H = mem.Jh
        self.Q = sys['Q']
        self.R = sys['R']
        self.X = sys['X']
        self.P = sys['P']
        self.W = np.eye(self.Q.shape[0])            
        self.innovation = None
        self.K = None                      

    def prediction(self,u):
        # EKF prediction (propagation) step
        # propagate state estimate and covariance
        self.X = self.f(self.X, u)                                             # use the nonlinear function f for state propagation
        self.P = self.F @ self.P @ self.F.T + self.W @ self.Q @ self.W.T       # P = FPF^T + WQW^T

    def correction(self,z,p):
        # EKF correction (measurement update) step
        # Inputs:
        # z: true range and bearing measurement 
        # p: true position of the detected landmark (used to map x to z)  
               
        # evaluate nonlinear measurement function h(x,p) = [range;bearing]
        z_hat = self.h(self.X,p)
        z_hat[1] = scipy.angle(z_hat[1])

        # compute the innovation: z - h(x,p) 
        self.innovation = z - z_hat 

        # compute the Kalman gain K 
        self.K = self.P @ self.H.T @ np.linalg.inv(self.H @ self.P @ self.H.T + self.V @ self.R @ self.V.T)

        # correct the state estimate
        self.X = self.X + self.K @ self.innovation

        # correct the state covariance
        I = np.eye(self.X.shape[0])
        self.P = (I - self.K @ self.H) @ self.P @ (I - self.K @ self.H).T + self.K @ self.R @ self.K.T


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