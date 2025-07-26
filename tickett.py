total_seats = 30
seats = [False] * total_seats  

while True:
    print("\n1) Book Ticket")
    print("2) Show Seats")
    print("3) Cancel Booking")
    print("4) Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        seat_number = input("Enter seat number to book: ")
        if seat_number.isdigit():
            seat_number = int(seat_number)
            if 1 <= seat_number <= total_seats:
                if not seats[seat_number - 1]:
                    seats[seat_number - 1] = True
                    print(f"Seat {seat_number} booked successfully!")
                else:
                    print(f"Seat {seat_number} is already booked.")
            else:
                print("Invalid seat number. Please enter a number between 1 and 30.")
        else:
            print("Invalid input! Please enter a valid seat number.")

    elif choice == '2':
        print("\nSeats:")
        seat_display = [str(i+1) if not seats[i] else 'B' for i in range(total_seats)]
        print(" ".join(seat_display))

    elif choice == '3':
        seat_number = input("Enter seat number to cancel: ")
        if seat_number.isdigit():
            seat_number = int(seat_number)
            if 1 <= seat_number <= total_seats:
                if seats[seat_number - 1]:
                    seats[seat_number - 1] = False
                    print(f"Booking for seat {seat_number} cancelled successfully!")
                else:
                    print(f"Seat {seat_number} was not booked.")
            else:
                print("Invalid seat number. Please enter a number between 1 and 30.")
        else:
            print("Invalid input! Please enter a valid seat number.")

    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
