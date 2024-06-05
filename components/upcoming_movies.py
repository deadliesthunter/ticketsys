import sqlite3

def pr_Movies(title,year,genre):
    title = title
    year = year
    genre = genre
    print("The currently upcoming movies are: \n")
    for i, (t, y, g) in enumerate(zip(title, year, genre)):     
        print(f"{i + 1}. Title {t}")
        print(f"year: {y}")
        print(f"genre: {g}")

def up_mov():
    con = sqlite3.connect("movi")
    cur = con.cursor()
    title = cur.execute("SELECT Title FROM up_movies").fetchall() # this fetches all the data at once in a tuple
    year = cur.execute("SELECT Year FROM up_movies").fetchall()
    genre = cur.execute("SELECT Genre FROM up_movies").fetchall()
    pr_Movies(title,year,genre)
    con.close()

