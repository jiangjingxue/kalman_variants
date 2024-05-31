"""
A class that implements common vehicle 
motion model and its Jocobian matrix. 
Certain vehicle models requires a constant
parameter wheelbase (L). The default 
wheelbase is 1.0.  

file:  motion_models.py
author: Jingxue Jiang <jingxue07@gmail.com>
date: May 28, 2024 
"""
import numpy as np

class MotionModelsN:
    def __init__(self):
        self.simple_car = self.Model('simple_car', self.__simple_car, self.__J_simple_car, 3, 2)
        self.differential_drive = self.Model('differential_drive', self.__differential_drive, self.__J_differential_drive, 3, 2)
        self.bicycle = self.Model('bicycle', self.__bicycle, self.__J_bicycle, 4, 2)
        self.ackermann = self.Model('ackermann', self.__ackermann, self.__J_ackermann, 4, 2)

        # default wheelbase
        self.L = 1.0
        
    class Model:
        def __init__(self, name, f, Jf, X_dim, u_dim):
            self.name = name
            self.f = f
            self.Jf = Jf
            self.X_dim = X_dim
            self.u_dim = u_dim
            
    def __simple_car(self,X,u):
        # Generalized kinematic vehicle model
        # state vector x = [x, y, θ]
        # control vector u = [v, ω]
        # 
        # Kinematic model in ODE form: 
        # x'(t) = v(t) * cos(θ(t))
        # y'(t) = v(t) * sin(θ(t))
        # θ'(t) = ω(t) 
        #
        # A = [cos(θ(t)) 0;
        #      sin(θ(t)) 0; 
        #          0     1] 
        # A is a state-dependent matrix that encapsulates the system's nonlinearity  
        assert X.shape[0] == 3, "given the motion model, state vector must have 3 variables"
        assert u.shape[0] == 2, "given the motion model, control vector must have 2 variables"

        A = np.array([[np.cos(X[2,0]), 0],
                      [np.sin(X[2,0]), 0], 
                      [0, 1]])
        return A @ u 
    
    def __J_simple_car(self,X,u):
        return np.eye(3)

    def __differential_drive(self,X,u): 
        # state vector x = [x, y, θ]
        # control vector u = [vl,vr], aka [left_wheel_vel,right_wheel_vel]
        # wheelbase L is a constant
        #
        # Kinematic model in ODE form: 
        # x'(t) = 0.5 * (vl + vr) * cos(θ(t))
        # y'(t) = 0.5 * (vl + vr) * sin(θ(t))
        # θ'(t) = (vr - vl) / L 
        #
        # In matrix form:
        # A = [0.5 * cos(θ(t)) 0.5 * cos(θ(t));
        #      0.5 * sin(θ(t)) 0.5 * sin(θ(t));
        #            -1 / L        1 / L      ]
        # A is a state-dependent matrix that encapsulates the system's nonlinearity  
        assert X.shape[0] == 3, "given the motion model, state vector must have 3 variables"
        assert u.shape[0] == 2, "given the motion model, control vector must have 2 variables"

        A = np.array([[0.5 * np.cos(X[2,0]), 0.5 * np.cos(X[2,0])],
                      [0.5 * np.sin(X[2,0]), 0.5 * np.sin(X[2,0])], 
                      [-1 / self.L, 1 / self.L]])
        return A @ u 
    
    def __J_differential_drive(self,X,u):
        raise NotImplementedError("the Jacobian for this motion model is not implemented yet")
    
    def __bicycle(self,X,u):
        # state vector x = [x, y, θ, v]
        # control vector u = [a, φ], aka [acceleration, steering angle]
        # wheelbase L is a constant
        # https://ywseo.github.io/vehicle-control/
        #
        # Kinematic model in ODE form: 
        # x'(t) = v(t) * cos(θ(t))
        # y'(t) = v(t) * sin(θ(t))
        # θ'(t) = v(t) * tan(φ(t)) / L
        # v'(t) = a(t) 
        assert X.shape[0] == 4, "given the motion model, state vector must have 4 variables"
        assert u.shape[0] == 2, "given the motion model, control vector must have 2 variables"

        return np.array([[X[3,0] * np.cos(X[2,0])], 
                         [X[3,0] * np.sin(X[2,0])], 
                         [X[3,0] * np.tan(u[1,0]) / self.L],
                         [u[0,0]]]) 
    
    def __J_bicycle(self,X,u):
        raise NotImplementedError("the Jacobian for this motion model is not implemented yet")
    
    def __ackermann(self,X,u):
        raise NotImplementedError("this motion model is not implemented yet")
    
    def __J_ackermann(self,X,u):
        raise NotImplementedError("the Jacobian for this motion model is not implemented yet")