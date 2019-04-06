Sandbox project for experimenting with python database access.


Install:

1.  Install Pip
+ sudo apt install python3-pip


Goals:

Hello Points Problem
1.  Run a prepared container that runs the hello_points program
+ Prepare a container.
+ Copy the source director to the container.
+ Run the install command
+ Execute the binary

Hello Points Solution
+ Created the Dockerfile.build file
+ The Dockerfile.build is executed via the command: 
  docker build -t python-points -f docker/Dockerfile.build  .
+ The image created from the previous command can be used to execute the hello_point by running: 
  docker run python-points hello_points
  
  
  
JSON interface AND Test Functionality
+ Create a function to_json
+ the to_json function calls to_json on the object passed in.
+ The Point and the PointSet object should implement a to_json function that turns their data into json
+ Write functions to create Point and PointSet from json data
+ Use the python unit testing framework to unit test the json input, output functions

Hook up python to postgres problem
+ Docker container exists and is called postgres-points
+ to build a new image: 
  docker run -d -p 5432:5432 --name postgres-points -e POSTGRES_PASSWORD=fart postgres
+ to start the container from the image:
  docker start postgres-points
  
+ Install SQL Alchemy: pip3 install sqlalchemy
  + Note that this installed sqlalchemy 1.3.1
  + Work done on branch ADD_SQL_ALCHEMY
+ Install psycopg2: pip3 install psycopg2
  + installed version psycopg2-2.7.7
+ Built a basic dao using the raw pscopg2 driver. 
  + docker run python-points hello_postgres
  
New Problem: Connecting the python container to the postgres container
+ To get the ip address of the postgres container run: 
docker network inspect bridge
+ To run the stub program 
docker run \
-e "PGPORT=5432" \
-e "PGHOST=172.17.0.2" \
-e "PGUSER=postgres" \
-e "PGPASSWORD=fart" \
-e "PGDATABASE=points" \
python-points  hello_postgres



