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

    # convert lat/lng from degrees to radians
    lat1_rad = math.radians(lat1)
    lng1_rad = math.radians(lng1)
    lat2_rad = math.radians(lat2)
    lng2_rad = math.radians(lng2)
    
    delta_sigma = acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lng1 - lng2))

    return r*delta_sigma 
    
    
