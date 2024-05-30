from available_seats import seat_Picker
def main():
    running_movies = {
    "The Shawshank Redemption": {"year": 1994, "Genre": "action/Drama", "rating through imdb": "9/10"},  # using a nested dictionary(dict within a dict)
    "The Good, The Bad and The Ugly": {"year": 1994, "Genre": "action/Drama", "rating through imdb": "8.9/10"}
    }

    print("The currently running movies are: \n")
    for  i,(movie,details) in enumerate(running_movies.items()): # A simple feature in python that lets you print value with indexed values
        print(f"{i + 1}. {movie}")
        print(f"   Year: {details['year']}")
        print(f"   Genre: {details['Genre']}")
        print(f"   Rating through IMDb: {details['rating through imdb']}")

    user_Input = int(input("Enter the ranking of the movie you want to watch \n"))  #use choosing the movie
    try:
        if 1 <= user_Input <= len(running_movies):  # Check if the input is within the valid range
            selected_movie = list(running_movies.items())[user_Input - 1]  # Access the selected movie, user input is dec cause it was increased in above loop
                                                                        # we made it list so that the list()[user-1] this part can choose without indexing
            movie, details = selected_movie  # Unpack the tuple into movie name and details
            print(f"The movie have choosen is {movie}")
            print(f"   Year: {details['year']}")
            print(f"   Genre: {details['Genre']}")
            print(f"   Rating through IMDb: {details['rating through imdb']}")
        else:
            print("Invalid ranking. Please enter a valid ranking number.")  # Handle invalid ranking input
    except ValueError:
        print("Invalid input. Please enter a number.")  # Handle non-integer input
    
    seat_Picker()

