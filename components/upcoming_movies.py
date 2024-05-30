def pr_Movies(upm):
    print("The currently upcoming movies are: \n")
    for i, (movie, details) in enumerate(upm.items()):
        print(f"{i + 1}. {movie}")
        print(f"   Year: {details['year']}")
        print(f"   Genre: {details['Genre']}")

def up_mov():
    upcoming_movies = {
        "The Shawshank Redemption": {"year": 1994, "Genre": "action/Drama", "rating through imdb": "9/10"},
        "The Good, The Bad and The Ugly": {"year": 1994, "Genre": "action/Drama", "rating through imdb": "8.9/10"}
    }
    pr_Movies(upcoming_movies)
