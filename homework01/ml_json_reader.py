import json
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('file_name', metavar= 'file_name', type=str, help= 'enter data file name')
args = parser.parse_args()
file_name = args.file_name
print(args.file_name)   # check to see if it is working 

def compute_average_mass(a_list_of_dicts, a_key_string):  
    total_mass = 0.
    for i in range(len(a_list_of_dicts)):
        total_mass += float(a_list_of_dicts[i][a_key_string])
    return (total_mass / len(a_list_of_dicts))

def check_name_hemisphere(lat, lon):
    location = 'Northern' if (lat > 0) else 'Southern'
    location = f'{location} & Eastern' if (lon > 0) else f'{location} & Western'
    return(location)   

def check_hemisphere(latitude: float, longitude: float, counts):
    if latitude > 0:
        counts['Northern'] += 1
    else:
        counts['Southern'] += 1

    if longitude > 0:
        counts['Eastern'] += 1
    else:
        counts['Western'] += 1

    return f'{latitude},{longitude}'

def calculate_location_percentages(counts):
    total_locations = sum(counts.values())

    northern_percentage = (counts['Northern'] / total_locations) * 100
    southern_percentage = (counts['Southern'] / total_locations) * 100
    eastern_percentage = (counts['Eastern'] / total_locations) * 100
    western_percentage = (counts['Western'] / total_locations) * 100

    return northern_percentage, southern_percentage, eastern_percentage, western_percentage

with open(file_name, 'r') as f:
    ml_data = json.load(f)

# prints out summary statistics
print(compute_average_mass(ml_data['meteorite_landings'], 'mass (g)'))

counts = {'Northern': 0, 'Southern': 0, 'Eastern': 0, 'Western': 0}

for row in ml_data['meteorite_landings']:
    print(check_hemisphere(float(row['reclat']), float(row['reclong']), counts))

for row in ml_data['meteorite_landings']:
    print(check_name_hemisphere(float(row['reclat']), float(row['reclong'])))
    
northern_percentage, southern_percentage, eastern_percentage, western_percentage = calculate_location_percentages(counts)

print(f'Overall Percentages:')
print(f'  Northern Percentage: {northern_percentage:}%')
print(f'  Southern Percentage: {southern_percentage:}%')
print(f'  Eastern Percentage: {eastern_percentage:}%')
print(f'  Western Percentage: {western_percentage:}%')
