from kalman_variants.common import zero_mean_gaussian, arbitrary_mean_gaussian 
from numpy import eye

def add_gaussian_noise():
    sys = eye(3) + zero_mean_gaussian(dim=3)
    print(sys)

if __name__ == "__main__":
    add_gaussian_noise()
