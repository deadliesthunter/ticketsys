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
    
    try:
        if ask_User in seats.values() and "available" in ask_User:
            confirmation = input("Your seat is currently available. Please press Y/N to reserve the seat \n").upper
            try:
                if "Y" in  confirmation:
                    seats.values = "Reserved"
                    print("Your seat is sucessfully reserved. Please arrive within 30 mins of the show to acess you reservation")
                elif "N" in confirmation:
                    print("N pressed. Reservation Cancelled. Thank you for co-operation")
            except ValueError:
                print("Error 101: Incorrect input. Please try again")
        elif ask_User in seats.values() and "Reserved" not in ask_User:
            print("Sorry, it is already reserved please try again")
                #need goto not availabe in python need structured code
    except ValueError:
        print("Error: The following seat is not present")



