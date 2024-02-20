# ISS Trajectory Data Analysis 

## Purpose
This repository contains a main script and a testing script that analyze and test the ISS trajectory data, as well as a Dockerfile used to build an image. The goal is to parse data from an XML file and print out a few informative statistics, including the range of data with timestamps, the full epoch closest to when the program was executed, the average speed of the ISS (international space station), and the instantaneous speed of the ISS closest to when the program was executed. Overall, this data is useful and important to analyze to gather accurate information about space and ensure the ISS is safe and not colliding with other objects in space, 

## Description of Scripts
* `iss_tracker.py`: Script that calculates and prints out the summary statistics described above.
* `test_iss_tracker.py`: Tests `compute_average_speed` and `compute_distance`, in the 'iss_tracker.py` file to ensure they are working as intended.
* `Dockerfile`: Contains instructions to build our image. 
 
## Instructions 
1. Make a Docker account (if you don't have one already)
2. Ensure `pytest` and `python3` are installed in your system
3. Clone this repository or download the files to your local machine
4.  View the ISS trajectory data [here](https://spotthestation.nasa.gov/trajectory_data.cfm), I recommend reading the paragraphs provided to get a sense of what the data provides and taking a look at the data itself (XML file is easier to read) 
5. Run these commands (to view summary statistics):
   ```python
   python3 iss_tracker.py
   ```
6. (Optional) If you would like to edit my `compute_average_speed` or `compute_distance` functions, `test_iss_tracker.py` allows you to, and ensures the functions are still working as intended. You may run it with this command: 
   ```python
   pytest
   ```
7. Now you want to build an image using our Dockerfile, so run this command:
   ```python
   docker build -t <dockerhubusername>/<code>:<version> . 
   ```
   To build my image I would execute:
   ```python
   docker build -t nicoleolv/iss_tracker.py . 
   ```
   **DO NOT FORGET THE DOT . AT THE END & MAKE SURE YOU'RE IN THE DIRECTORY (homework04) THAT CONTAINS ALL YOUR FILES**
8. Ensure your image has been built by executing this command:
   ```python
   docker images
   ```
   You should see something like this:
   ```python
       REPOSITORY                   TAG       IMAGE ID       CREATED          SIZE
    nicoleolv/iss_tracker           1.0      107dc2c7c488   7 seconds ago    449MB
   ```
9. Then, to test/run the containerized code, execute this:
   ```python
     docker run iss_tracker
   ```
   And the summary statistics should print out!
   
    To test/run the containerized tests.
   ```python
   docker run iss_tracker pytest
   ```
## Overview
Overall, my docker image illustrates a program used to print summary statistics on ISS trajectory data. The output of `iss_tracker.py` provide a series of statistics that help the user gain clarity on the ISS trajectory data. First, a range of the data using timestamps to illustrate when this data was gathered (on a 15 day period). Second, the full epoch closest to 'now' (now being when the program is executed) is printed, providing the user with the velocity and timestamp of the ISS. Third, the average speed of the whole 15-day period trajectory is printed, giving the user an overview of how fast the ISS is moving. Lastly, the instantaneous speed closest to 'now' is printed. 

**-> It is important to note that the values of the closest epoch & instantaneous speed to 'now' will change everytime you run your program, since your 'now' is defined as the time you execute your program.**
