"""
Motion model class for common vehicle types.    
Motions models are expressed in its matrix form.

file:  motion_models.py
author: Jingxue Jiang <jingxue07@gmail.com>
data: May 28, 2024 
"""
import numpy as np

class MotionModels(object):
    def __init__(self):
        self.model = None
        self.L = 1.0 

    def generalized(self,x,u):
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
        assert x.shape[0] == 3, "State vector must have 3 variables"
        assert u.shape[0] == 2, "Control parameter must have 2 variables"
        self.model = "generalized"

        A = np.array([[np.cos(x[2,0]), 0],
                      [np.sin(x[2,0]), 0], 
                      [0, 1]])
        return A @ u 
    
    def differential_drive(self,x,u):
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
        assert x.shape[0] == 3, "State vector must have 3 variables"
        assert u.shape[0] == 2, "Control parameter must have 2 variables"
        self.model = "differential"

        A = np.array([[0.5 * np.cos(x[2,0]), 0.5 * np.cos(x[2,0])],
                      [0.5 * np.sin(x[2,0]), 0.5 * np.sin(x[2,0])], 
                      [-1 / self.L, 1 / self.L]])
        return A @ u 
    
    def bicycle(self,x,u):
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
        assert x.shape[0] == 4, "State vector must have 3 variables"
        assert u.shape[0] == 2, "Control parameter must have 2 variables"
        self.model = "bicycle"

        return np.array([[x[3,0] * np.cos(x[2,0])], 
                         [x[3,0] * np.sin(x[2,0])], 
                         [x[3,0] * np.tan(u[1,0]) / self.L],
                         [u[0,0]]]) 
    