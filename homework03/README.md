# Meteorite Landings Data Analysis

## Purpose
This repository contains 2 main scripts and 2 testing scripts that are used to analyze meteorite landings data, as well as a Dockerfile used to build an image. The goal is to parse data from a CSV file and print out a few informative statistics, including the amount of meteorites that landed on given years, the comparison of masses to 100g, and the ability to gather which meteorite landed closest to a point (in this case I used the UT Tower coordinates). Overall, this project was used to learn how to parse data from a CSV file (and dealing with big data sets), unit testing, the use of `pytest`, and the whole process of building a Docker image. 

## Description of Scripts
* `gcd_algorithm.py`: Script that calculates the distance between two points using the greater circle distance formula. 
* `ml_data_analysis.py`: Main script that reads the CSV data and calculates & prints out summary statistics.
* `test_gcd_algorithm.py`: Tests the `greater_circle_distance` function from the 'gcd_algorithm.py' file to ensure the function is working as intended 
* `test_ml_data_analysis`: Tests `meteorite_per_year`, `compare_mass`, and `closest_meteorite`, in the 'ml_data_analysis.py` file to ensure they are all working as intended.
* `Dockerfile`: Contains instructions to build our image 
 
## Instructions 
1. Make a Docker account (if you don't have one already)
2. Ensure `pytest` and `python3` are installed in your system
3. Clone this repository or download the files to your local machine
4.  View the meteorite landings data [here](https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh/about_data), head to 'export'/API Endpoint/CSV (for data format), copy the .csv file link, and/or run this command in your (my cloned) repository:
  ```python
  wget https://data.nasa.gov/resource/gh4g-9sfh.csv
  ```
You should have a file named `gh4g-9sfh.csv` in your repository now. 
8. Run these commands (to view summary statistics):
  ```python
  python3 gcd_algorithm.py
  ```
  ```python
  python3 ml_data_analysis.py 'gh4g-9sfh.csv'
  ```
5. (Optional) If you would like to change my ml_data_analysis.py or gcd_algorithm.py, `test_gcd_algorithm.py` & `test_ml_data_analysis.py` allow you to, and ensure the functions are still working as intended. You may run these with this command: 
  ```python
  pytest
  ```
6. Now you want to build an image using our Dockerfile, so run this command:
   ```python
   docker build -t <dockerhubusername>/<code>:<version> . 
   ```
   To build my image I would execute:
   ```python
   docker build -t nicoleolv/ml_data_analysis.py:1.0 . 
   ```
   **DO NOT FORGET THE DOT . AT THE END & MAKE SURE YOU'RE IN THE DIRECTORY (homework03) THAT CONTAINS ALL YOUR FILES**
7. Ensure your image has been built by executing this command:
   ```python
   docker images
   ```
   You should see something like this:
   ```python
  REPOSITORY                   TAG       IMAGE ID       CREATED          SIZE
  nicoleolv/ml_data_analysis   1.0      fbc71f1bf83a   6 seconds ago    446MB
   ```
8. Then, to test/run the containerized code, execute this:
  ```python
  docker run --rm \
             -v $PWD/gh4g-9sfh.csv:/data/gh4g-9sfh.csv \
             nicoleolv/ml_data_analysis:1.0 \
             ml_data_analysis.py /data/gh4g-9sfh.csv
  ```
  We volume mount the data, instead of actually including it in our container, by using `-v`.
  And the summary statistics should print out!
9. To test/run the containerized tests, execute this:
   ```python
  docker run --rm \
             -v $PWD/gh4g-9sfh.csv:/data/gh4g-9sfh.csv \
             nicoleolv/ml_data_analysis:1.0 \
             pytest
  ```

## Overview
Overall, my docker image illustrates a program used to print summary statistics on meteorite landings data. The output of `ml_data_analysis` provide a series of numbers that help the user gain clarity on the meteorite landings data. First, all the years are printed along with a number that depicts the amount of meteorites that landed on that year. Second, the meteorites masses are compared to 100g, giving the user an overview of how heavy/light these meteorites are. Lastly, the name of the meteorite that landed closest to the UT Tower is provided along with that distance itself. 


