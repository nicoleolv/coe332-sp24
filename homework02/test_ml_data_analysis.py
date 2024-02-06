from ml_data_analysis import meteorites_per_year, compare_mass, closest_meteorite
import pytest
import math

data = {'meteorite_landings':[{'name': 'Bevo', 'year': '2000', 'mass': '100', 'reclat': '0', 'reclong': '0'},
                              {'name': 'Hook em', 'year': '2004', 'mass': '200', 'reclat': '1', 'reclong': '1'},
                              {'name': 'Longhorn', 'year': '2000', 'mass': '300', 'reclat': '2', 'reclong': '2'}]}

def test_meteorites_per_year():
    expected_output = { '2000': 2, '2001': 1 }
    result = meteorites_per_year(data['meteorite_landings'], 'year')

def test_compare_mass():
    user_mass_input = 150
    expected_lighter_count = 1
    expected_heavier_count = 2
    lighter_count, heavier_count = compare_mass(data['meteorite_landings'], user_mass_input, 'mass')
    assert lighter_count == expected_lighter_count
    assert heavier_count == expected_heavier_count

def test_closest_meteorite():
    first_lat = 0
    first_lng = 0
    second_lat = 1
    second_lng = 1 
    expected_distance = 10007.5434
    actual_result = closest_meteorite(data['meteorite_landings'], first_lat, first_lng, second_lat, second_lng)
    
    
    


    
