#!/usr/bin/env python3
import requests
import math
from datetime import datetime
from typing import List
import xml.etree.ElementTree as ET

def loadISS():
        # Loads the ISS data using the requests library 
        url = 'https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml'
        response = requests.get(url)
        with open('iss_oem.xml', 'wb') as f: 
                f.write(response.content)
        
def parseXML(xmlfile):
        """
        Parses xmlfile and stores into a list of dictionaries
        
        Args:
            xmlfile (str): 

        Returns:
            data (list of dictionaries): Stores necessary elements from our xmlfile 
        """
        tree = ET.parse(xmlfile)
        root = tree.getroot()
        data = []
        for element in root.findall('.//stateVector'):
                epoch = datetime.strptime(element.find('EPOCH').text, '%Y-%jT%H:%M:%S.%fZ')   # matches format of '2024-047T12:00:00.000Z'
                x_dot = float(element.find('X_DOT').text)
                y_dot = float(element.find('Y_DOT').text)
                z_dot = float(element.find('Z_DOT').text)
                data.append({'epoch': epoch, 'x_dot': x_dot, 'y_dot': y_dot, 'z_dot': z_dot})
        return data

def compute_average_speed(data: List[dict]) -> float:
        """
        Iterates through a list of dictionaries gathering velocities and computing the average speed over the whole data set 

        Args:
            data (list): A list of dictionaries, each dict should have the same set of keys including velocity  

        Returns:
            total_speed/len(data) (float): Average speed over the whole data set
        """
        total_speed = 0
        for item in data:
                speed = math.sqrt(item['x_dot']**2 + item['y_dot']**2 + item['z_dot']**2)
                total_speed += speed
        return total_speed/len(data) 

def compute_distance(x1, x2, y1, y2, z1, z2) -> float:
        """
        Computes the distance between two data sets (velocities)

        Args: 
            x1 (float): First velocity in the x-direction
            x2 (float): Second velocity in the x-direction
            y1 (float): First velocity in the y-direction
            y2 (float): Second velocity in the y-direction
            z1 (float): First velocity in the z-direction
            z2 (float): Second velocity in the z-direction

        Returns: 
            distance formula (float): Distance between two velocities  
        """
        
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def main():
        loadISS()
        
        data = parseXML('iss_oem.xml')
        
        start_epoch = data[0]['epoch']
        end_epoch = data[-1]['epoch']   # [-1] accesses last element 
        print(f"Data ranges from {start_epoch} to {end_epoch}")

        time_now = datetime.utcnow()
        closest_epoch = min(data, key=lambda x: abs(x['epoch'] - time_now))
        print("\nFull epoch closest to now: ")
        print(f"Timestamp: {closest_epoch['epoch']}")
        print(f"X_DOT: {closest_epoch['x_dot']}")
        print(f"Y_DOT: {closest_epoch['y_dot']}")
        print(f"Z_DOT: {closest_epoch['z_dot']}")

        average_speed = compute_average_speed(data)
        print("\nAverage speed over the whole data set:", average_speed, "km/s")

        old_epoch = data[0]['epoch']
        old_x = data[0]['x_dot']
        old_y = data[0]['y_dot']
        old_z = data[0]['z_dot']
        for item in data[1:]:   # 1 to the end
                if item['epoch'] > time_now:
                        current_epoch = item['epoch']
                        current_x = item['x_dot']
                        current_y = item['y_dot']
                        current_z = item['z_dot']
                        time_diff = (current_epoch - old_epoch).total_seconds()
                        distance = compute_distance(old_x, current_x, old_y, current_y, old_z, current_z)
                        instantaneous_speed = distance/time_diff
                        print(f"\nInstantaneous speed closest to now: {instantaneous_speed} km/s")
                        break
                old_epoch = item['epoch']
                old_x = item['x_dot']
                old_y = item['y_dot']
                old_z = item['z_dot']

                
if __name__ == '__main__':
        main()
            
