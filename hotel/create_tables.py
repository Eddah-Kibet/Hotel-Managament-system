from database import Base, engine
from models import Guest, Room, Reservation, Payment

print(" Creating tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")