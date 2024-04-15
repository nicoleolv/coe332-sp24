# HGNC App

## Purpose
This repository contains a full flask application with redis to analyze data abot genes from the HGNC. This data is useful and important to gather accurate information about old and newly discovered. Overall, this project is used to gain familiarity with flask web applications, redis database, and jobs functionality, while also analyzing important gene data.


## Summary of Contents
* `api.py`: Flask web application with redis database
* `worker.py`: Handles all jobs processed from the redis queue
* `jobs.py`: Contains functions for creating, retrieving, and updating jobs in the redis queue 
* `requirements.txt`: Lists all of the necessary Python depenedencies to run our app
* `Dockerfile`: Contains instructions to build our docker image
* `docker-compose.yml`: Configuration file that allows for a simplified `docker run` command

## Data
The HGNC data is available to the public and can be downloaded from their website; https://www.genenames.org/download/archive/ . This data contains a lot of specifications for each gene. For a better understanding of what the data yields, I recommend reading the paragraphs provided (on the website) and taking a look at the data itself. 

## Instructions
### Running the Containers
We need to launch two containers, one for Flask and one for Redis. For this reason, we have a docker-compose.yml file. This file allows us to containerize both services at once.

To build our docker image, run this command:
```python
docker-compose build 
```
To launch both services run this command:
```python
docker-compose up -d
```
Make sure it is running with this command:
```python
docker ps -a 
```
You should see something like this: 
```python
CONTAINER ID   IMAGE                             COMMAND                  CREATED              STATUS                     PORTS                                       NAMES
619fe36d3cf9   nicoleolv/gene-app:1.0            "python3 api.py"         About a minute ago   Up About a minute          0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   homework07_flask-api_1
3bba4811e28c   nicoleolv/gene-app:1.0            "python3 worker.py"      About a minute ago   Up About a minute                                                      homework07_worker_1
f71dfd5f4101   redis:7                           "docker-entrypoint.s…"   About a minute ago   Up About a minute          0.0.0.0:6379->6379/tcp, :::6379->6379/tcp   homework07_redis-db_1
```
**p.s. : to stop the services, run: `docker-compose down`**

### Accessing the Routes 
To interact with the Flask API, use `curl` commmands as shown below:
* To put the data into Redis:
  ```python
  curl -X POST localhost:5000/data
  ```
* To get all the data from Redis:
  ```python
  curl localhost:5000/data
  ```
  * To delete the data from Redis:
  ```python
  curl -X DELETE localhost:5000/data
  ```
  * To get a list of all hgnc_ids:
  ```python
  curl localhost:5000/genes
  ```
   * To get all the data associated with a specific hgnc_id:
  ```python
  curl localhost:5000/genes/<hgnc_id>
  ```
  * To create a job:
   ```python
  curl localhost:5000/jobs -X POST -d '{"gene_id":<HGNC:5>, "gene_status":<Approved>}' -H "Content-Type: application/json"
  ```
  * To list all jobs on the queue:
   ```python
   curl localhost:5000/jobs
   ```
  * To get job status:
    ```python
    curl localhost:5000/jobs/<jobid>
    ```

## Interpreting the Output 
* `/data` (GET) route returns a list of the whole data
* `/genes` route returns a list of all the hgnc_ids
* `/genes/<hgnc_id>` route returns a list of all the data associated with a specific hgnc, including its location, symbol, status, name, and much more
* `/jobs` (GET) route returns all exisiting job ids
          (POST) route creates a new job with a unique identifier 
* `/jobs/<jobid>` returns the job information for a given job ID including its status (if it has been completed) 

## Overview
Overall, this Flask Web Application and use of the Redis Database provides an easy way to analyze this large set of data. The whole data may be returned & may be deleted, or only the data associated with hgnc_ids of one OR all. It returns all this data fast and efficiently with the help of Redis and Flask!  
