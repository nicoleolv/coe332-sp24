# HGNC Redis in Flask App

## Purpose


## Summary of Contents
* `api.py`: Flask web application with redis database
* `worker.py`:
* `jobs.py`:
* `requirements.txt`: 
* `Dockerfile`: Contains instructions to build our docker image
* `docker-compose.yml`: Configuration file that allows for a simplified `docker run` command

## Data
The HGNC data is available to the public and can be downloaded from their website; https://www.genenames.org/download/archive/ . This data contains a lot of specifications for each gene. For a better understanding of what the data yields, I recommend reading the paragraphs provided (on the website) and taking a look at the data itself. 

## Instructions
### Running the Containers
We need to launch two containers, one for Flask and one for Redis. For this reason, we have a docker-compose.yml file. This file allows us to containerize both services at once.

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
CONTAINER ID   IMAGE                              COMMAND                  CREATED          STATUS                     PORTS
           NAMES
efc2c9dcc38b   nicoleolv/gene_api_flask_app:1.0   "python3 /gene_api/g…"   33 minutes ago   Up 33 minutes              0.0.0.0:5001->5001/tcp, :::5001->5001/tcp   homework06_flask-app_1
9cde92899c31   redis:7                            "docker-entrypoint.s…"   33 minutes ago   Up 33 minutes              0.0.0.0:6379->6379/tcp, :::6379->6379/tcp   homework06_redis-db_1
```
**p.s. : to stop the services, run: `docker-compose down`**

### Accessing the Routes 
To interact with the Flask API, use `curl` commmands as shown below:
* To put the data into Redis:
  ```python
  curl -X POST localhost:5001/data
  ```
* To get all the data from Redis:
  ```python
  curl localhost:5001/data
  ```
  * To delete the data from Redis:
  ```python
  curl -X DELETE localhost:5001/data
  ```
  * To get a list of all hgnc_ids:
  ```python
  curl localhost:5001/genes
  ```
   * To get all the data associated with a specific hgnc_id:
  ```python
  curl localhost:5001/genes/<hgnc_id>
  ```

## Interpreting the Output 
* `/data` (GET) route returns a list of the whole data
* `/genes` route returns a list of all the hgnc_ids
* `/genes/<hgnc_id>` route returns a list of all the data associated with a specific hgnc, including its location, symbol, status, name, and much more

## Overview
Overall, this Flask Web Application and use of the Redis Database provides an easy way to analyze this large set of data. The whole data may be returned & may be deleted, or only the data associated with hgnc_ids of one OR all. It returns all this data fast and efficiently with the help of Redis and Flask!  
