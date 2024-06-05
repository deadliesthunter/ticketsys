import sqlite3

def run_movies():
    con = sqlite3.connect("movi")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS run_movies(id INTEGER PRIMARY KEY AUTOINCREMENT,Title TEXT, Year INTEGER, Genre TEXT, Rating REAL)") #Real is float of sqlite
    running_movies = {
    "The Shawshank Redemption": {"Year": 1994, "Genre": "action/Drama", "rating_through_imdb": "9"},  # using a nested dictionary(dict within a dict)
    "The Good, The Bad and The Ugly": {"Year": 1994, "Genre": "action/Drama", "rating_through_imdb": "8.9"}
    }
    for title, details in running_movies.items():
            year = details['Year']
            genre = details['Genre']
            rating = float(details['rating_through_imdb'])
            cur.execute("INSERT INTO run_movies VALUES(NULL,? ,? ,? ,?)",(title,year,genre,rating)) # should pass the values as tuple

    con.commit()
    con.close()

def upcomming_movies():
      con = sqlite3.connect("movi")
      cur = con.cursor()
      cur.execute("CREATE TABLE IF NOT EXISTS up_movies(id INTEGER PRIMARY KEY AUTOINCREMENT, Title TEXT, Year INTEGER, Genre TEXT)")
      upcoming_movies = {
        "The Shawshank Redemption": {"Year": 1994, "Genre": "action/Drama"},
        "The Good, The Bad and The Ugly": {"Year": 1994, "Genre": "action/Drama"}
    }
      for title, details in upcoming_movies.items():
            year = details['Year']
            genre = details['Genre']
            
            cur.execute("INSERT INTO up_movies VALUES(NULL,? ,? ,? )",(title,year,genre)) # should pass the values as tuple

      con.commit()
      con.close()

def available_seats():
      con = sqlite3.connect("movi")
      cur = con.cursor()
      cur.execute("CREATE TABLE IF NOT EXISTS av_seat(id INTEGER PRIMARY KEY AUTOINCREMENT,Seat_num TEXT, Availability TEXT)")
      seats = {}        # dict created to make store seates with availability
      for i in range(20):
        seats_a = "a" + str(i+1)       #creating total of 60 seats with id a1,b1.c1.....
        seats_b = "b" + str(i+1)
        seats_c = "c" + str(i+1)
        seats[seats_a] = "available"           #it declares the dic like "a1" : avilable
        seats[seats_b] = "available"
        seats[seats_c] = "available"
    
      for seat,availability in seats.items():
           cur.execute("INSERT INTO av_seat VALUES(NULL,? ,?)",(seat,availability))

      con.commit()
      con.close()
        
run_movies()
upcomming_movies()
available_seats()
