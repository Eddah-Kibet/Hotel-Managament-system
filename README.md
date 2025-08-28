# Hotel Management System

A simple command-line Hotel Management System built with Python, SQLAlchemy, and Alembic for database migrations.

## Features

- Manage Guests: Add and list hotel guests.
- Manage Rooms: Add and list rooms.
- Manage Reservations: Add and list reservations.
- Manage Payments: Add and list payments.

## Project Structure

```
hotel/
    create_tables.py      # Script to create database tables
    crud.py               # CRUD operations for all models
    database.py           # Database connection and Base class
    hotel.db              # SQLite database file
    main.py               # Main CLI application
    models.py             # SQLAlchemy ORM models
migrations/
    env.py                # Alembic migration environment
    script.py.mako        # Alembic migration script template
    versions/             # Alembic migration scripts
alembic.ini               # Alembic configuration file
README.md                 # Project documentation
```

## Setup

1. **Clone the repository**

    ```sh
    git clone <your-repo-url>
    cd Hotel-Managament-system
    ```

2. **Create a virtual environment and activate it**

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**

    ```sh
    pip install sqlalchemy alembic click
    ```

4. **Initialize the database**

    ```sh
    cd hotel
    python create_tables.py
    ```

5. **Run the application**

    ```sh
    python main.py
    ```

## Database Migrations

This project uses [Alembic](https://alembic.sqlalchemy.org/) for database migrations.

- To create a new migration after modifying models:

    ```sh
    alembic revision --autogenerate -m "Your migration message"
    ```

- To apply migrations:

    ```sh
    alembic upgrade head
    ```

## Notes

- The database is stored in `hotel/hotel.db`.
- All models are defined in [`hotel/models.py`](hotel/models.py).
- CRUD operations are in [`hotel/crud.py`](hotel/crud.py).
- The CLI application is in [`hotel/main.py`](hotel/main.py).
