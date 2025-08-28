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
            first_name = click.prompt("First name")
            last_name = click.prompt("Last name")
            email = click.prompt("Email")
            phone_number = click.prompt("Phone number")
            click.secho(f"{Guest} added successfully", fg = "green")

        if guest_option == 2:
            click.secho("List guests", fg = "blue")
            list_guests()

# ------------Reservations--------------
    if user_input == 2:
        click.secho("Reservation options", fg="green")
        click.secho("1. Add new reservation", fg = "yellow")
        click.secho("2. List reservations", fg = "yellow")

        reservation_option = click.prompt("Select an option", type = int)

        if reservation_option == 1:
            click.secho("Add new reservation", fg = "yellow")
            create_reservation(
                guest_id=click.prompt("Guest ID"),              
                room_id=click.prompt("Room ID"),                
                check_in_date=click.prompt("Check out time"), 
                check_out_time=click.prompt("Check out time"),
            )
            click.secho("Reservation added successfully", fg = "green")

        if reservation_option == 2:
            click.secho("List reservations", fg = "yellow")
            total_reservations = list_reservations()
            click.secho(f"Total reservations: {total_reservations}", fg = "yellow") 

# ------------Rooms--------------
    if user_input == 3:
        click.secho("Room options", fg = "green")
        click.secho("1. Add new room", fg = "white")
        click.secho("2. List rooms", fg = "white")

        rooms_option = click.prompt("Select an option", type = int)

        if rooms_option == 1:
            click.secho("Add new room", fg = "white")
            room_number = input("Enter room number: ")
            room_type = input("Enter room type: ")
            price = float(input("Enter price: ")) 
            status = input("Enter status: ")
            add_room(room_number, room_type, price, status)
            click.secho("Room added successfully", fg = "green")

        if rooms_option == 2:
            click.secho("List rooms", fg = "white")
            list_rooms()

# ------------Exit--------------
    if user_input == 4:
        click.secho("Goodbye", fg = "red")
        break
