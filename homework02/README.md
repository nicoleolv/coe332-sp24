# Meteorite Landings Data Analysis

## Purpose
This repository contains 2 main scripts and 2 testing scripts that are used to analyze meteorite landings data. The goal is to parse data from a CSV file and print out a few informative statistics, including the amount of meteorites that landed on given years, the comparison of masses by an input from the user, and the ability to gather which meteorite landed closest to a point (in this case I used the UT Tower coordinates). Overall, this project was used to learn how to parse data from a CSV file (and dealing with big data sets), as well as unit testing and the use of `pytest`.  

## Description of Scripts
* `gcd_algorithm.py`: Script that calculates the distance between two points using the greater circle distance formula. 
* `ml_data_analysis.py`: Main script that reads the CSV data and calculates & prints out summary statistics.
* `test_gcd_algorithm.py`: Tests the `greater_circle_distance` function from the 'gcd_algorithm.py' file to ensure the function is working as intended 
* `test_ml_data_analysis`: Tests `meteorite_per_year`, `compare_mass`, and `closest_meteorite`, in the 'ml_data_analysis.py` file to ensure they are all working as intended.
 
## Instructions 
1. Download your CSV file that contains data
2. Ensure `pytest` and `python3` are installed in your system
3. Clone this repository or download the files to your local machine
4. Run these commands (to view summary statistics):
  ```python
  python3 gcd_algorithm.py
  ```
  ```python
  python3 ml_data_analysis.py [name of your csv file]
  ```
  for my repository, my CSV file is called 'gh4g-9sfh.csv', so I would execute this command:
  ```python
  python3 ml_data_analysis.py 'gh4g-9sfh.csv'
  ```
5. (Optional) If you would like to change the functions `test_gcd_algorithm.py` & `test_ml_data_analysis.py` allow you to and ensure the functions are still working as intended. You may run these with this command: 
  ```python
  pytest
  ```

## Interpreting the Results
The output of `ml_data_analysis` provide a series of numbers that help the user gain clarity on the meteorite landings data. First, all the years are printed along with a number that depicts the amount of meteorites that landed on that year. Second, the user is asked to input a mass that will be used to compare to the other meteorites mass, giving the user an overview of how heavy/light these meteorites are. Lastly, the name of the meteorite that landed closest to the UT Tower is provided along with that distance itself. 


