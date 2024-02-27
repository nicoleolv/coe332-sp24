# ISS Trajectory Data Flask Web Application 

## Purpose
This repository contains a main script and a testing script that analyze and test the ISS trajectory data, as well as a Dockerfile used to build an image. The goal is to make a full flask application web and prints out a few informative statistics, including all the epochs, part of the epochs specified by the user, state vectors from one specific epoch, the instantaneous speed and state vectors nearest in time, and the full epoch closest to when the program was executed. This data is useful and important to gather accurate information about space and ensure the ISS is safe and not colliding with other objects in space. Overall, this project is used to gain familiarity with flask web applications and routes, while also analyzing important ISS data.

## Description of Scripts
* `iss_tracker.py`: Flask web application
* `test_iss_tracker.py`: Unit tests for iss_tracker.py 
* `Dockerfile`: Contains instructions to build our docker image
* diagram.png : An overview of the components of this project 
 
## Instructions 
1. Make a Docker account (if you don't have one already)
2. Ensure `pytest`, `python3`, and `flask` are installed in your system
3. Clone this repository or download the files to your local machine
4.  View the ISS trajectory data [here](https://spotthestation.nasa.gov/trajectory_data.cfm), I recommend reading the paragraphs provided to get a sense of what the data provides and taking a look at the data itself (XML file is easier to read) 
5. Run this command to start the web application:
   ```python
   python3 iss_tracker.py
   ```
   And to interact with it, use curl commands (on another window) as shown:
   **your web application has to be running to be able to interact with it**
   * Returns all epochs
   ```python
   curl http://129.114.37.110:5000/epochs
   ```
   * Returns a modified list of epochs with a specified limit (amount of epochs returned) and 
    offset (# starting epoch) 
    ```python
   curl http://129.114.37.110:5000/epochs?limit=20&offset=5
   ```
   * Returns a specific epoch 
   ```python
   curl http://129.114.37.110:5000/epochs/2024-052T12:16.00.000Z
   ```
   * Returns instantaneous speed of a specific epoch
  ```python
   curl http://129.114.37.110:5000/epochs/2024-052T12:16.00.000Z/speed 
   ```
   * Returns state vectors and intsantaneous speed closest to now (time when the program was 
    executed)
   ```python
   curl http://129.114.37.110:5000/now 
   ```
7. (Optional) If you would like to edit any of the functions, `test_iss_tracker.py` allows you to, and ensures the functions are still working as intended. You may run it with this command: 
   ```python
   pytest
   ```
8. Now you want to build an image using our Dockerfile, so run this command:
9.  ```python
   docker build -t <dockerhubusername>/<code>:<version> . 
   ```
   To build my image I would execute:
   ```python
   docker build -t nicoleolv/flask-iss_tracker.py . 
   ```
   **DO NOT FORGET THE DOT . AT THE END & MAKE SURE YOU'RE IN THE DIRECTORY (homework04) THAT CONTAINS ALL YOUR FILES**
9. Ensure your image has been built by executing this command:
   ```python
   docker images
   ```
   You should see something like this:
   ```python
     REPOSITORY                      TAG       IMAGE ID       CREATED          SIZE
     nicoleolv/flask-iss_tracker     1.0       f217fbc625b7   11 seconds ago   1.01GB
   ```
10. Then, to test/run the containerized code, execute this:
   ```python
     docker run --name "flask-iss_tracker-app" -d -p 5000:5000 nicoleolv/flask-iss_tracker:1.0
   ```
   And you should get something like this:
   ```python
   1f0d016b4c618e68c3068ee6d6217487fc4b5f4396687a5ac9ea5e7019700b76
  ```
    To test/run the containerized tests.
   ```python
   docker run iss_tracker pytest
   ```
## Interpreting the Output 
* `/epochs` : returns entire data set
* `/epochs?limit=int&offset=int` : returns a modified list of epochs given query parameters
* `/epochs/<epoch>` : returns state vectors for a specififc epoch from data set
* `/epochs/<epoch>/speed` : returns instantaneous speed for a specific epoch in the data set
* `/now` : returns state vectors and instantaneous speed for the epoch closest to now 

## Overview
Overall, my docker image illustrates a flask web application that returns ummary statistics on ISS trajectory data. The interactive `iss_tracker.py` script provide a series of statistics that help the user gain clarity on the ISS trajectory data. The whole data may be returned, a modified list of the data, instantaneous speed of a specific epoch, state vectors and instantaneous speed of the epoch closest to now may be returne. All is based on user interactive user input. Please note that 'diagram.png' provides a visual overview of this project.  

**-> It is important to note that the values of the closest epoch & instantaneous speed to 'now' will change everytime you run your program, since your 'now' is defined as the time you execute your program.**
