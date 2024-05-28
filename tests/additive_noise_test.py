import numpy as np
from kalman_variants.common.additive_noise import AdditiveNoise

def add_gaussian_noise():
    noise = AdditiveNoise(3)
    sys = np.eye(3) + noise.zero_mean_gaussian()
    print(sys)

if __name__ == "__main__":
    add_gaussian_noise()
