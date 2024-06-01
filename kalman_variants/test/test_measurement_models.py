from kalman_variants.measurement_models.measurement_models import MeasurementModels
from numpy import array, pi, allclose, sqrt


def test_landmark_range_bearing_model():
    X = array([[1], [1], [pi/2]])
    l = array([[2], [2]])

    measurement_models = MeasurementModels()
    h1 = measurement_models.landmark_range_bearing_model(X,l)
    h2 = array([[sqrt(2)], [-0.25 * pi]])
    assert allclose(h1, h2), "Landmark Range and Bearing Model Failed: measurement vectors are not equal"

if __name__ == "__main__":
    test_landmark_range_bearing_model()
    print("Tests Passed")
