https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/

# Gym Planner With docker file
Based on previous Gym-Planner web app developed for TUAS project. This version incorperates docker files usage to be able to run without the need to install Postgres locally. 

Additionally, the database will run on a docker network. 

Furthermore, plans to incorparate kubernetes technology. 

This project is an application that stores work out plans and allows registered users to create their own plans using the database of excersises. Users can customize their own plans and print out work out sheets to bring with them to the gym.

Guest users are also allowed to view workout published by members but can't customize, save or print workouts. 
