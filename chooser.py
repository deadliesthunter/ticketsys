from components import running_movies, upcoming_movies

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