import numpy as np

def normalize(angle):
    # normalize the angle between [-pi,pi]
    while(angle > np.pi):
        angle -= 2 * np.pi
    while(angle <  -np.pi):
        angle += 2 * np.pi   
    return angle