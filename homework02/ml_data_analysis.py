#!/usr/bin/env python3
from gcd_algorithm import greater_circle_distance
from typing import List
import csv
import argparse
import logging
import socket

logging.basicConfig(level='DEBUG')

def meteorites_per_year(a_list_of_dicts: List[dict], a_key_string: str) -> float:
    """
    Iterates through a list of dictionaries, pulling out values associated with a given key. Keeps count of how many times each year shows up and returns this value (for each year).

    Args:
        a_list_of_dicts (list): A list of dictionaries, each dict should have the same set of keys
        a_key_string (string): A key that appears in each dictionary associated with the desired value

    Returns:
        year (float): The year for the meteorite 
        count (float): Amount of times a meteorite is dated with that year
    """
    meteorites_by_year = {}  # stores amount
    
    for each in a_list_of_dicts:
        year = each.get(a_key_string, 'year')
        meteorites_by_year[year] = meteorites_by_year.get(year, 0)+1  # for that year add one
    for year, count in meteorites_by_year.items():  # count how many are stored for each year
        print(f"Year: {year}, Number of Meteorites: {count}")     

def compare_mass(a_list_of_dicts: List[dict], mass_entry: float, a_key_string: str) -> float:
    """
    Iterates through a list of dictionaries, ensuring the values pulled out (associated with the given key) are converted to floats, and takes in an argument (a mass with units in grams). The input mass is then compared with the rest of the values and put into a lighter or heavier count.

    Args:
        a_list_of_dicts (List): A list of dictionaries, each dict should have the same set of keys
        mass_entry (float): An input mass given by the user, that is then compared to the rest of the masses
        a_key_string (string): A key that appears in each dictionary that is used to find the mass of each meteorite

    Returns:
        lighter (float): The number of meteorites who have a mass lower than the input mass
        heavier (float): The number of meteorties who have a mass higher than the input mass 
    """
    # initialize values that will hold the # of meteorites lighter/heavier than given mass
    lighter = 0
    heavier = 0

    # checks to make sure the value is a float and/or if there is any value
    for entry in a_list_of_dicts:
        mass_str = entry.get(a_key_string, '')
        try:
            mass = float(mass_str) if mass_str.strip() else 0
        except ValueError:
            logging.error('Error occurred while trying to convert the mass value to a float')
            continue
        
        if mass < mass_entry:
            lighter += 1
        elif mass > mass_entry:
            heavier += 1
            
    print(f"Number of meteorites lighter: {lighter}")
    print(f"Number of meteorites heavier: {heavier}")

def closest_meteorite(a_list_of_dicts: List[dict], lat: float, lng: float, lat_key: str, lng_key: str) -> float:
    """
    Iterates through a list of dictionaries, gathering values associated with given keys, to return the closest meteorite (to the given coordinate point).

    Args:
        a_list_of_dicts (list):  A list of dictionaries, each dict should have the same set of keys
        lat (float): Latitude of coordinate point (target)
        lng (float): Longitude of coordinate point (target)
        lat_key (str): A key that appears in each dictionary, for the latitude of a coordiante point
        lng_key (str): A key that appears in each dictionary, for the longitude of a coordinate point

    Results: 
        closest_meteorite (str): Name of the closest meteorite to the target
        min_distance (float): Smallest distance from the target to a meteorite (in kilometers) 
    """
    closest_meteorite = None
    min_distance = float('inf')  # initiate it to a very big number 

    for each in a_list_of_dicts:
        meteorite_lat_str = each.get(lat_key, '')
        meteorite_lng_str = each.get(lng_key, '')
        try:
            meteorite_lat = float(meteorite_lat_str) if meteorite_lat_str.strip() else 0
            meteorite_lng = float(meteorite_lng_str) if meteorite_lng_str.strip() else 0
        except ValueError:
            logging.error(f"Error occurred while trying to convert the latitude/longitude to a float")
        
        distance = greater_circle_distance(lat, lng, meteorite_lat, meteorite_lng)

        if distance < min_distance:
            min_distance = distance
            closest_meteorite = each
    if closest_meteorite:
        print(f"Closest meteorite: {closest_meteorite['name']}")
        print(f"Distance from target point: {min_distance} kilometers") 
    else:
        print("No meteorites found in the given data.")
        
def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', metavar= 'file_name', type=str, help= 'enter data file name')
    args = parser.parse_args()
    file_name = args.file_name

    logging.basicConfig(level=logging.ERROR)
        
    data = {}
    data['meteorite_landings'] = []

    with open(file_name, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data['meteorite_landings'].append(dict(row))

    print("First few rows of data:")
    for i, row in enumerate(data['meteorite_landings']):
        if i >= 5:  # Print only first few rows for brevity
            break
        print(row)

            
    meteorites_per_year(data['meteorite_landings'], 'year')

    user_mass_entry = float(input("Enter a mass value: "))
    compare_mass(data['meteorite_landings'], user_mass_entry, 'mass')

    # The UT Tower
    target_latitude = 30.2862    
    target_longitude = 97.7394  
    closest_meteorite(data['meteorite_landings'], target_latitude, target_longitude, 'reclat', 'reclong')

if __name__ == '__main__':
    main()
