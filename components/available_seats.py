import sqlite3

def seat_Picker():
    con = sqlite3.connect("movi")
    cur = con.cursor()
    seat_no = cur.execute("SELECT seat_num FROM av_seat").fetchall()
    avaialbility= cur.execute("SELECT Availability FROM av_seat").fetchall()
    available_seats = cur.execute("SELECT seat_num FROM av_seat WHERE Availability = 'available'").fetchall()
    available_seats = [seat[0] for seat in available_seats]  # Convert list of tuples to list of strings
    if available_seats:
        print(f"The available seats are: {', '.join(available_seats)}")
    else:
        print("No available seats.")
        return

    ask_User =input("Enter the seat you want to reserve \n").lower()
    
    if ask_User in available_seats:
            confirmation = input("Your seat is currently available. Please press Y/N to reserve the seat \n").upper()
            if confirmation == "Y":
                cur.execute("UPDATE av_seat SET Availability = 'reserved' WHERE seat_num = ?", (ask_User,))
                con.commit() 
                print("Your seat is successfully reserved. Please arrive within 30 mins of the show to access your reservation.")
            elif confirmation == "N":
                print("Reservation cancelled. Thank you for your cooperation.")
            else:
                print("Error 101: Incorrect input. Please try again.")
    else:
        print("Sorry, this seat is already reserved. Please try again.")
    con.close()

