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

