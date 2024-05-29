from kalman_variants.motion_models import MotionModels
from numpy import array, pi, allclose

def test_generalized_model():
    x = array([[1], [1], [pi]])
    u = array([[1], [1]])

    f1 = MotionModels.generalized(x,u)
    f2 = array([[-1], [0], [1]])
    assert allclose(f1, f2), "Generalized Model Failed: Matrices are not equal"

def test_differential_drive_model():
    x = array([[1], [1], [pi]])
    u = array([[2], [1]])
    L = 1.0

    f1 = MotionModels.differential_drive(x,u,L)
    f2 = array([[-1.5], [0], [-1]])
    assert allclose(f1, f2), "Differential Drive Model Failed: Matrices are not equal"

def test_bicycle_model():
    x = array([[1], [1], [pi],[1]])
    u = array([[1], [pi]])
    L = 1.0

    f1 = MotionModels.bicycle(x,u,L)
    f2 = array([[-1], [0], [0], [1]])
    assert allclose(f1, f2), "Bicycle Drive Model Failed: Matrices are not equal"

if __name__ == "__main__":
    test_generalized_model()
    test_differential_drive_model()
    test_bicycle_model()
    print("Tests Passed")