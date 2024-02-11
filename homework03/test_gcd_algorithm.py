from gcd_algorithm import greater_circle_distance
import pytest
import math 

def test_greater_circle_distance():
    first_lat = 30.2862   # The UT Tower 
    first_lng = 97.7394
    second_lat = 48.8049  # Palace of Versailles
    second_lng = 2.1204
    expected_distance =  10142.18155
    result = greater_circle_distance(first_lat, first_lng, second_lat, second_lng)
    assert isinstance(greater_circle_distance(first_lat, first_lng, second_lat, second_lng), float) == True
    

def test_greater_circle_distance_exceptions():
    first_lat = 30.2862   # The UT Tower
    first_lng = 97.7394
    second_lat = 48.8049  # Palace of Versailles
    second_lng = 2.1204
    first_wrong_lat = 'i am a wrong lat'
    with pytest.raises(ValueError):  # value not a float 
        greater_circle_distance(first_wrong_lat, first_lng, second_lat, second_lng) 
