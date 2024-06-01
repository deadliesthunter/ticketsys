def seat_Picker():
    seats = {}
    for i in range(20):
        seats_a = "a" + str(i+1)
        seats_b = "b" + str(i+1)
        seats_c = "c" + str(i+1)
        seats[seats_a] = "available"
        seats[seats_b] = "available"
        seats[seats_c] = "available"

    if "available" in seats.values():
        print(f"the availabel seats are {seats}")

    ask_User =input("Enter the seat you want to reserve \n").lower()
    
    if ask_User in seats:
        if seats[ask_User] == "available":
            confirmation = input("Your seat is currently available. Please press Y/N to reserve the seat \n").upper()
            if confirmation == "Y":
                seats[ask_User] = "reserved"
                print("Your seat is successfully reserved. Please arrive within 30 mins of the show to access your reservation.")
            elif confirmation == "N":
                print("Reservation cancelled. Thank you for your cooperation.")
            else:
                print("Error 101: Incorrect input. Please try again.")
        else:
            print("Sorry, this seat is already reserved. Please try again.")
    else:
        print("Error: The selected seat is not available.")



