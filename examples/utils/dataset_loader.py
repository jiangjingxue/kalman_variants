"""
Dataset loader for UTIAS Multi-Robot Cooperative Localization and Mapping Dataset
Author: Jingxue Jiang <jingxue07@gmail.com> 
Dataset: http://asrl.utias.utoronto.ca/datasets/mrclam/index.html 
"""
import numpy as np
import pandas as pd
import os

class UTIASDatasetLoader(object):
    '''
    Dataset Info
    ----------
    - Barcodes.dat
        -> each subject (robot or landmark) has a unique barcode number associated with it 
    - Landmark_Groundtruth.dat
        -> mean groundtruth position (x,y) of all (static) landmarks and 
           standard deviations of the groundtruth measurements
    - Robot_Groundtruth.dat
        -> time-stamped groundtruth poses (x,y,θ) of robot
    - Robot__Odometry.dat
        -> time-stamped velocity commands (v,ω) of robot 
    - Robot_Measurement.dat
        -> time-stamped range and bearing measurements (r,φ) of robot
        -> each measurement identifies a measured subject

    Preprocessing
    ----------------
    - 
    '''
    def __init__(self,root_dir):
        self.root_dir = root_dir
        self.load_dataset()

    def load_dataset(self):
        self.barcodes = np.genfromtxt(self.root_dir + "/Barcodes.dat", names=['subject', 'subject_id'], dtype=int)
        self.landmark_groundtruth = np.genfromtxt(self.root_dir + "/Landmark_Groundtruth.dat", usecols = [0,1,2], dtype=[("subject", int), ("x", float), ("y", float),("x_std", float),("y_std", float)])
        self.robot_groundtruth = np.genfromtxt(self.root_dir + "/Robot1_Groundtruth.dat", usecols = [1,2,3], dtype=[("Time", float), ("x", float), ("y", float),("orientation", float)])
        self.robot_measurement = np.genfromtxt(self.root_dir + "/Robot1_Measurement.dat", usecols = [1,2,3],  dtype=[("Time", float), ("subject", int), ("range", float),("bearing", float)])
        self.robot_odometry = np.genfromtxt(self.root_dir + "/Robot1_Odometry.dat", usecols = [1,2],  dtype=[("Time", float), ("forward_velocity", float), ("angular_velocity", float)])

        # For robot_measurement, remove measurements where the subject is a moving robot
        subjects_to_remove = np.unique(self.barcodes['subject_id'][0:5])
        self.robot_measurement = self.robot_measurement[~np.isin(self.robot_measurement["subject"], subjects_to_remove)]

        # Convert the dataset to a Pandas DataFrame
        df = pd.DataFrame(self.robot_measurement)

        # Display the table
        print(df)


if __name__ == "__main__":
    root = os.path.abspath(os.curdir)
    target = root + "/data/UTIAS_dataset"
    DataLoader = UTIASDatasetLoader(target)

