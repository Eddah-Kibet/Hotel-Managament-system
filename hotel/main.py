import click
from crud import * 

while True:
    click.secho("-------Hotel Management System-------", fg="green")
    click.secho("1. Guests", fg="blue")
    click.secho("2. Reservations", fg="yellow")
    click.secho("3. Rooms", fg = "green")
    click.secho("4. Exit", fg = "red")

    user_input = click.prompt("Select an option", type = int)

