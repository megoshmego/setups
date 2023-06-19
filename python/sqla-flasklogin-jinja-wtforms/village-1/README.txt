# ---------------
# Quick Guide for Dummies
# ---------------

# If you don't have a virtual environment setup yet, create one using virtualenv
# Ensure you're in the project directory then run the following commands

python3 -m venv flaskenv

# Activate the virtual environment (assuming you're using virtualenv and its name is flaskenv)
source flaskenv/bin/activate

# Install the requirements
pip install -r requirements.txt

# For setting up the PostgreSQL database
# Enter the PostgreSQL command line
psql postgres

# In the PostgreSQL command line, create the database
CREATE DATABASE mydatabase;

# Exit the PostgreSQL command line
\q

# Make sure you have your DATABASE_URL environment variable set in your activated virtual environment
# It should look like this:
# export DATABASE_URL=postgresql://<username>:<password>@localhost:5432/mydatabase

# run

python run.py

TO CLONE THIS REPO IF YOU HAVENT DONE THAT BEFORE
*********************
create an empty repo 

clone my repo

open a terminal

in terminal 

    > rm -rf .git

    > git init

    > git add .

    > git commit -m "Initial commit"

    > git remote add origin https://github.com/yourusername/newrepository.git

    > git push -u origin main

