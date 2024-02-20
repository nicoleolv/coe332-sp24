from iss_tracker import compute_average_speed, compute_distance
import pytest
import math

def test_compute_average_speed():
    data = [{'x_dot': 1, 'y_dot': 2, 'z_dot': 3},
            {'x_dot': 1, 'y_dot': 2, 'z_dot': 3}]
    expected_avg_speed = math.sqrt(14)
    result = compute_average_speed(data)
    assert expected_avg_speed == result 
    
def test_compute_distance():
    x1 = 1
    x2 = 2
    y1 = 3
    y2 = 4
    z1 = 5
    z2 = 6
    expected_distance = math.sqrt(3)
    result = compute_distance(x1, x2, y1, y2, z1, z2)
    assert expected_distance == result
