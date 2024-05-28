import numpy as np

class AdditiveNoise(object):
    def __init__(self,dim):
        self.dim = dim 

    def zero_mean_gaussian(self): 
        uniform_rand = np.random.uniform(0, 1, size=self.dim)
        gaussian_noise = np.sqrt(-2 * np.log(uniform_rand)) * np.cos(2 * np.pi * np.random.uniform(0, 1, size=self.dim))
        return gaussian_noise

    def arbitrary_mean_gaussian(self, mean, std):
        gaussian_noise = np.random.normal(loc=mean, scale=std, size=self.dim)
        return gaussian_noise
    

    

