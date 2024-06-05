from available_seats import seat_Picker
import sqlite3

def main():
    con = sqlite3.connect("movi")
    cur = con.cursor()
    title = cur.execute("SELECT Title FROM run_movies").fetchall() # this fetches all the data at once in a tuple
    year = cur.execute("SELECT Year FROM run_movies").fetchall()
    genre = cur.execute("SELECT Genre FROM run_movies").fetchall()
    rating = cur.execute("SELECT Rating FROM run_movies").fetchall()

    print("The currently running movies are: \n")
    for  i,(t,y,g,r) in enumerate(zip(title,year,genre,rating)): # A simple feature in python that lets you print value with indexed values
        print(f"{i + 1}. {t}")
        print(f"   Year: {y}")
        print(f"   Genre: {g}")
        print(f"   Rating_through_IMDb: {r}")

    user_Input = int(input("Enter the ranking of the movie you want to watch \n"))  #use choosing the movie
    try:
        if 1 <= user_Input <= len(title):  # Check if the input is within the valid range
            querry = "SELECT * FROM run_movies WHERE id = ?" #we can either call from id {} or using fetch like given below
            cur.execute(querry, (user_Input,))
            inp = cur.fetchone()      ## fetches the given row of db
            ##selected_movie = list(running_movies.items())[user_Input - 1]  # Access the selected movie, user input is dec cause it was increased in above loop
                                                                        # we made it list so that the list()[user-1] this part can choose without indexing
            ##movie, details = selected_movie  # Unpack the tuple into movie name and details
            print(f"The movie have choosen is {inp[1]}")
            print(f"   Year: {inp[2]}")
            print(f"   Genre: {inp[3]}")
            print(f"   Rating_through_IMDb: {inp[4]}")
        else:
            print("Invalid ranking. Please enter a valid ranking number.")  # Handle invalid ranking input
    except ValueError:
        print("Invalid input. Please enter a number.")  # Handle non-integer input
        con.close()
    
    seat_Picker()

