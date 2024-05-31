import numpy as np

def zero_mean_gaussian(dim): 
    uniform_rand = np.random.uniform(0, 1, size=dim)
    gaussian_noise = np.sqrt(-2 * np.log(uniform_rand)) * np.cos(2 * np.pi * np.random.uniform(0, 1, size=dim))
    return gaussian_noise

def arbitrary_mean_gaussian(mean, std, dim):
    gaussian_noise = np.random.normal(loc=mean, scale=std, size=dim)
    return gaussian_noise
    

    

