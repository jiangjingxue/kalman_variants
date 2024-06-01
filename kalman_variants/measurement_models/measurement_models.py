"""
A class that implements several measurement models
and their Jacobian. 

file:  measurement_models.py
author: Jingxue Jiang <jingxue07@gmail.com>
date: May 30, 2024 
"""
import numpy as np

class MeasurementModels:
    def __init__(self):
        self.landmark_range_bearing = self.Model('landmark_range_bearing', 
                                                 self.__landmark_range_bearing_model, 
                                                 self.__J_landmark_range_bearing_model,
                                                 2,
                                                 ["simple_car", "differential_drive"])

    class Model:
        def __init__(self, name, h, Jh, z_dim, li):
            self.name = name
            self.h = h
            self.Jh = Jh
            self.z_dim = z_dim
            self.compatibility_list = li

    def __landmark_range_bearing_model(self,X,p):
        # state estimate vector X = [x, y, θ]
        # landmark true position vector p_landmark = [px,py]
        # need two positions (global) to obtain the range and bearing (in local frame)
        assert X.shape[0] == 3, "given the measurement model, state vector must have 3 variables"
        assert p.shape[0] == 2, "given the measurement model, landmark position vector must have 2 variables"

        sum = np.square(p[0,0] - X[0,0]) + np.square(p[1,0] - X[1,0])
        expected_range = np.sqrt(sum)
        expected_bearing = np.arctan2(p[1,0]-X[1,0],p[0,0]-X[0,0]) - X[2,0]

        # resulting expected_bearing value is now measured relative to the orientation of 
        # the robot's state X rather than the global coordinate system, no need to normalize
        return np.array([[expected_range],
                         [expected_bearing]])

    def __J_landmark_range_bearing_model(self,X,l):
        pass