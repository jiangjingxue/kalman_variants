"""
A minimal example
Author: Jingxue Jiang <jingxue07@gmail.com> 
GitHub: https://github.com/jiangjingxue/Kalman_filter_variants
"""
import numpy as np
from kalman_variants.process_models.motion_models_n import MotionModelsN
from kalman_variants.measurement_models.measurement_models import MeasurementModels
from kalman_variants import EKF

def main():
    # system params
    sys = {}

    motion_models = MotionModelsN()
    measurement_models = MeasurementModels()

    # set up models and noise covariances
    motion_model = motion_models.simple_car
    measurement_model = measurement_models.landmark_range_bearing
    sys['Q'] = np.diag(np.power([0.015, 0.01, 0.01], 2))
    sys['R'] = np.diag(np.power([0.5, 0.5], 2))

    # provide an initial state estimate
    sys['X'] =  np.array([[1], [1], [np.pi]])
    sys['P'] = 0.1 * np.eye(3)

    ekf = EKF(sys,motion_model,measurement_model)

if __name__ == "__main__":
    main()