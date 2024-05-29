"""
A minimal example
Author: Jingxue Jiang <jingxue07@gmail.com> 
GitHub: https://github.com/jiangjingxue/kalman_filter_variants
"""
import numpy as np
from kalman_variants.motion_models import MotionModels
from kalman_variants.extended_kalman_filter import EKFLocalization

def main():
    # build system
    sys = {} 

    # set up motion model and covariances
    motion_models = MotionModels()
    sys['f'] = motion_models.generalized
    sys['x'] =  np.array([[1], [1], [np.pi]])
    sys['P'] = 0.1 * np.eye(3)
    sys['Q'] = np.diag(np.power([0.015, 0.01, 0.01], 2))
    sys['R'] = np.diag(np.power([0.5, 0.5], 2))

    ekf = EKFLocalization(sys,motion_models)

if __name__ == "__main__":
    main()