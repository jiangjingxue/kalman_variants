from kalman_variants.process_models.motion_models import MotionModels
from numpy import array, pi, allclose

def test_generalized_model():
    x = array([[1], [1], [pi]])
    u = array([[1], [1]])

    motion_models = MotionModels()
    f1 = motion_models.simple_car(x,u)
    f2 = array([[-1], [0], [1]])
    assert allclose(f1, f2), "Generalized Model Failed: Matrices are not equal"
    print(motion_models.name)

def test_differential_drive_model():
    x = array([[1], [1], [pi]])
    u = array([[2], [1]])

    motion_models = MotionModels()
    f1 = motion_models.differential_drive(x,u)
    f2 = array([[-1.5], [0], [-1]])
    assert allclose(f1, f2), "Differential Drive Model Failed: Matrices are not equal"
    print(motion_models.name)

def test_bicycle_model():
    x = array([[1], [1], [pi],[1]])
    u = array([[1], [pi]])

    motion_models = MotionModels()
    f1 = motion_models.bicycle(x,u)
    f2 = array([[-1], [0], [0], [1]])
    assert allclose(f1, f2), "Bicycle Drive Model Failed: Matrices are not equal"
    print(motion_models.name)


def test_model_type():
    x = array([[1], [1], [pi],[1]])
    u = array([[1], [pi]])

    motion_models = MotionModels()
    f = motion_models.bicycle(x,u)

    expected_model = "bicycle"
    assert motion_models.name == expected_model
  
if __name__ == "__main__":
    test_generalized_model()
    test_differential_drive_model()
    test_bicycle_model()
    test_model_type()
    print("Tests Passed")