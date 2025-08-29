import click
from datetime import datetime
from crud import * 

while True:
    click.secho("-------Hotel Management System-------", fg="green")
    click.secho("1. Guests", fg="blue")
    click.secho("2. Reservations", fg="yellow")
    click.secho("3. Rooms", fg = "white")
    click.secho("4. Exit", fg = "red")

    user_input = click.prompt("Select an option", type = int)

# ------------Guests--------------
    if user_input == 1:
        click.secho("Guests options", fg = "green")
        click.secho("1. Add new guest", fg = "blue" )
        click.secho("2. List guests", fg = "blue")

        guest_option = click.prompt("Select an option", type = int)

        if guest_option == 1:
            click.secho("Add new guest", fg = "blue")
            add_guest(
                first_name = click.prompt("First name"),
                last_name = click.prompt("Last name"),
                email = click.prompt("Email"),
                phone_number = click.prompt("Phone number")
            )
            click.secho(f"Guest added successfully", fg = "green")

        if guest_option == 2:
            click.secho("List guests", fg = "blue")
            for g in list_guests():
                print(g)

# ------------Reservations--------------
    if user_input == 2:
        click.secho("Reservation options", fg="green")
        click.secho("1. Add new reservation", fg = "yellow")
        click.secho("2. List reservations", fg = "yellow")
        click.secho("3. Update reservation", fg = "yellow")

        reservation_option = click.prompt("Select an option", type = int)

        if reservation_option == 1:
            click.secho("Add new reservation", fg = "yellow")
            create_reservation(
                guest_id=click.prompt("Guest ID"),
                room_id=click.prompt("Room ID"),
                check_in_date=click.prompt("Check in date"),
                check_out_date=click.prompt("Check out date"),
            )
            click.secho("Reservation added successfully", fg = "green")

        if reservation_option == 2:
            click.secho("List reservations", fg = "yellow")
            for r in list_reservations():
                print(r)

        if reservation_option == 3:
            click.secho("Update reservation", fg = "yellow")
            update_reservation(
                reservation_id=click.prompt("Reservation ID"),
                **{
                    "guest_id": click.prompt("Guest ID", default=None),
                    "room_id": click.prompt("Room ID", default=None),
                    "check_in_date": click.prompt("Check in date", default=None),
                    "check_out_date": click.prompt("Check out date" , default=None),
                    "status": click.prompt("Status", default=None)
                }
            )
            click.secho("Reservation updated successfully", fg = "green")

# ------------Rooms--------------
    if user_input == 3:
        click.secho("Room options", fg = "green")
        click.secho("1. Add new room", fg = "white")
        click.secho("2. List rooms", fg = "white")

        rooms_option = click.prompt("Select an option", type = int)

        if rooms_option == 1:
            click.secho("Add new room", fg = "white")
            room_number = input("Enter room number: ")
            click.secho("Types of rooms include: executive, deluxe, standard", fg = "blue")
            room_type = input("Enter room type: ")
            price = float(input("Enter price: ")) 
            click.secho("Status of room can be: Available, Booked, Unavailable", fg = "blue")
            status = input("Enter status: ")
            add_room(room_number, room_type, price, status)
            click.secho("Room added successfully", fg = "green")

        if rooms_option == 2:
            click.secho("List rooms", fg = "white")
            for r in list_rooms():
                print(r)


# ------------Exit--------------
    if user_input == 4:
        click.secho("Goodbye and welcome again", fg = "yellow")
        break
