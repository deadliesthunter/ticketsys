import sys
import os

# Get the current directory and components path
current_dir = os.path.dirname(__file__)
components_path = os.path.join(current_dir, 'components')

# Add the components directory to sys.path
sys.path.append(components_path)

# Import the modules from the components directory
import running_movies
import upcoming_movies

def up_Run():
    a = input("""Please Enter To Select:  
              1. Running Movies
              2. Upcoming Movies
              """)
    if (a == "1"):
        running_movies.main()

    elif(a == "2"):
        upcoming_movies.up_mov()
    
    else:
        print("Sorry, No such options available !!!")
    

up_Run()