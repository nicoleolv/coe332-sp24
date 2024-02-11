import math 

def greater_circle_distance(lat1: float, lng1: float, lat2: float, lng2:float) -> float:
    """
    Given 2 coordinate points the function will find the distance between them using the greater circle distance formula

    Args:
        lat1: Latitude of first point 
        lng1: Longitude of first point
        lat2: Latitude of second point
        lng2: Longitude of second point

    Returns:
        result (float): Distance (between the points) in kilometers 
    """
    r = 6371  # in kilometers

    if not all(isinstance(coord, (int, float)) for coord in [lat1, lng1, lat2, lng2]):
        raise ValueError("Latitude and longitude values must be of type float.")
    
    # convert lat/lng from degrees to radians
    lat1_rad = math.radians(lat1)
    lng1_rad = math.radians(lng1)
    lat2_rad = math.radians(lat2)
    lng2_rad = math.radians(lng2)
    
    delta_sigma = math.acos(math.sin(lat1_rad) * math.sin(lat2_rad) + math.cos(lat1_rad) * math.cos(lat2_rad) * math.cos(lng1_rad - lng2_rad))

    return r*delta_sigma 
