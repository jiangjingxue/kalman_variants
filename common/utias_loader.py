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
    '''
    def __init__(self,root_dir,dt,last_frame=None):
        self.root_dir = root_dir
        self.sample_interval = dt
        self.timesteps = None

        self._load()
        self._sample(dt)
        self._remove_moving_robots()

        if last_frame is not None:
            self._cut_frames(last_frame)

        self._encode_replace()
        # self._add_headers()
        
        # df_barcodes = pd.DataFrame(self.barcodes)
        # df_landmarks = pd.DataFrame(self.landmark_groundtruth)
        # df_groundtruth = pd.DataFrame(self.robot_groundtruth)
        # df_odom = pd.DataFrame(self.robot_odometry)
        # df_measurement = pd.DataFrame(self.robot_measurement)
        # print("Barcodes:")
        # print(df_barcodes)
        # print("Landmark groundtruth:")
        # print(df_landmarks)
        # print("Sampled groundtruth:")
        # print(df_groundtruth)
        # print("Sampled odom:")
        # print(df_odom)
        # print("Sampled measurement:")
        # print(df_measurement)        

    def _load(self):
        self.barcodes = np.genfromtxt(self.root_dir + "/Barcodes.dat")
        self.landmark_groundtruth = np.genfromtxt(self.root_dir + "/Landmark_Groundtruth.dat")
        self.robot_groundtruth = np.genfromtxt(self.root_dir + "/Robot1_Groundtruth.dat")
        self.robot_measurement = np.genfromtxt(self.root_dir + "/Robot1_Measurement.dat")
        self.robot_odometry = np.genfromtxt(self.root_dir + "/Robot1_Odometry.dat")

    def _sample(self,sample_time):
        # Step 1: find ground truth min max timestamp
        min_timestamps_groundtruth = np.min(self.robot_groundtruth[:, 0])
        max_timestamps_groundtruth = np.max(self.robot_groundtruth[:, 0])

        # Step 2: Subtracting the minimum time value from the time columns for Robot groundtruth,measurement, and odometry
        self.robot_groundtruth[:, 0] -= min_timestamps_groundtruth
        self.robot_measurement[:, 0] -= min_timestamps_groundtruth
        self.robot_odometry[:, 0] -= min_timestamps_groundtruth

        # Step 3: Calculate the timestamp based on the duration and the desired sample time
        max_timestamps_groundtruth = max_timestamps_groundtruth - min_timestamps_groundtruth
        self.timesteps = int(np.floor(max_timestamps_groundtruth / sample_time) + 1)
        self.duration = max_timestamps_groundtruth

        # Step 4: copy robot_groundtruth to old_data
        old_data = self.robot_groundtruth.copy()

        # Step 5: initialize variable k,t,i,p 
        k = 0
        t = 0
        i = 0
        p = 0

        # Step 6: get the rows and cols of the old_data (robot_groundtruth)
        rows, cols = old_data.shape

        # Step 7: create new_data using the timestamp and the number of cols of the old_data 
        new_data = np.zeros((self.timesteps, cols))

        # Step 8: Outer While loop
        # insert sampled time into the first column of the new_data
        # increment current timestamp value by the sample time every iteration util reaches max_timestamps_groundtruth
        # does something inside the loop, possibly populate data
        while t <= max_timestamps_groundtruth:
            new_data[k, 0] = t

            # Step 9: Inner while loop
            # as long as the timestamp value in the current row is smaller than 1, go to the next row and check again
            # break if reach the end of row (of the old_data)
            # the goal is to find the index where the timestamp value in old_data is greater than timestamp value in the new_data
            # it tries to find where the groundtruth should start, if we want data at 0.2 seconds, there is no point to retrieve
            # anything in old_data before 0.2 seconds. 
            while old_data[i, 0] <= t:
                if i == rows:
                    break
                i += 1
            # Step 10: What to do after you found the index 
            # Special Case (if statement)
            # if it is the first row or the last row of the old_data, 
            # set everything on the next row in the new_data to zero (not including the timestamp)
            # General Case (else statement)
            if i == 0 or i == rows:
                new_data[k, 1:] = 0
            else:
                # Step 11: Get p 
                # get p by manipulating the timestamp in old_data  
                p = (t - old_data[i-1, 0]) / (old_data[i, 0] - old_data[i-1, 0])

                # Step 12: Set sc
                sc = 1

                # Step 13: Another for loop
                # from column 2 to number of number in old_data 
                for c in range(sc, cols):
                    new_data[k, c] = p * (old_data[i, c] - old_data[i-1, c]) + old_data[i-1, c]



            # Step 14: 
            # increment the row index in new_data and the current timestamp
            k += 1
            t += sample_time

        # Step 15: Assign new_data to robot_groundtruth
        self.robot_groundtruth = new_data
        
        # --------End of the first while loop------------- # 
        # Step 16: Copy Robot_odometry to old_data 
        old_data = self.robot_odometry.copy()

        # Step 17: Clear variable k,t,i,p
        k = 0
        t = 0
        i = 0
        p = 0

        # Step 18: get the rows and cols of the old_data (robot_odometry)
        rows, cols = old_data.shape

        # Step 19: create new_data using the timestamp and the number of cols of the old_data 
        new_data = np.zeros((self.timesteps, cols))

        # Step 20: Outer While loop
        while t <= max_timestamps_groundtruth:
            new_data[k, 0] = t

            # Step 21: Inner while loop
            while old_data[i, 0] <= t:
                if i == rows:
                    break
                i += 1
            # Step 22: What to do after index is found (IMPORTANT)
            if i == 0 or i == rows:
                new_data[k, 1:] = old_data[i,1:]     # Different 
            else:
                # Step 23: Get p
                p = (t - old_data[i-1, 0]) / (old_data[i, 0] - old_data[i-1, 0]) # Same 

                # Step 24: Set sc
                sc = 1

                # Step 25: Another for loop
                for c in range(sc, cols):
                    new_data[k, c] = p * (old_data[i, c] - old_data[i-1, c]) + old_data[i-1, c] # Same

            k += 1
            t += sample_time
        
        # Step 26: Assign new_data to robot_odometry
        self.robot_odometry = new_data

        # --------End of the second while loop------------- # 
        # Step 27: Copy Robot_measurement to old_data 
        old_data = self.robot_measurement.copy()
        new_data = old_data.copy()

        # Step 28: For loop 
        for i in range (old_data.shape[0]):
            new_data[i, 0] = np.floor(old_data[i, 0] / sample_time + 0.5) * sample_time

        # Step 29: Assign new_data to robot_measurement
        self.robot_measurement = new_data


    def _remove_moving_robots(self):
        # Remove moving robots
        subjects_to_remove = np.unique(self.barcodes[:,1][0:5])
        self.robot_measurement = self.robot_measurement[~np.isin(np.round(self.robot_measurement[:,1]), subjects_to_remove)]
    
    def _cut_frames(self,last_frame):
        max_timestamps_groundtruth = self.robot_groundtruth[last_frame, 0]
        self.robot_groundtruth = self.robot_groundtruth[:last_frame]
        self.robot_odometry = self.robot_odometry[:last_frame]
        cutoff_idx = np.searchsorted(self.robot_measurement[:, 0], max_timestamps_groundtruth)
        if cutoff_idx == 0:
            # handle the case where no idx was found
            raise ValueError("No measurement data can be found as a result of an invalid last_frame parameter, increase the last_frame")
        else:
            self.robot_measurement = self.robot_measurement[:cutoff_idx]
    
    def _encode_replace(self):
        # create key-value pairs
        barcodes_swapped = np.array(self.barcodes.copy()[:, [1, 0]])
        barcodes_swapped = barcodes_swapped.astype(int)
        key_value_map = dict(barcodes_swapped)

        # replace the second columns in robot_measurement.dat
        self.robot_measurement[:, 1] = [key_value_map[int(x)] for x in self.robot_measurement[:, 1]]


    def _add_headers(self):
        pass
 

    



if __name__ == "__main__":
    target_dir = "./data/UTIAS_dataset"
    DataLoader = UTIASDatasetLoader(target_dir,0.1,1200)