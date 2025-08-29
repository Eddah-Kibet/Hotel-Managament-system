from models import Guest,Room,Reservation,Payment
from database import SessionLocal

db = SessionLocal()

def add_guest(first_name, last_name, email, phone_number):
    guest = Guest(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number)
    db.add(guest)
    db.commit()
    db.refresh(guest)
    return guest

def list_guests():
    return db.query(Guest).all()

def add_room(room_number, room_type, price, status = "Available"):
    room = Room(room_number=room_number, room_type=room_type, price=price, status=status)
    db.add(room)
    db.commit()
    db.refresh(room)
    return room

def list_rooms():
    return db.query(Room).all()

def create_reservation(guest_id,room_id,check_in_date, check_out_time, status= "Booked"):
    reservation = Reservation(
        guest_id=guest_id, room_id=room_id, check_in_date=check_in_date, check_out_time=check_out_time, status=status
    )
    db.add(reservation)
    db.commit()
    db.refresh(reservation)
    return reservation

def list_reservations():
    return db.query(Reservation).all()

def update_reservation(reservation_id, **kwargs):
    reservation = db.query(Reservation).filter(Reservation.reservation_id == reservation_id).first()
    if reservation:
        for key, value in kwargs.items():
            setattr(reservation, key, value)
        db.commit()
        db.refresh(reservation)
    return reservation

def create_payment(reservation_id, amount, payment_method, payment_date, guest_id):
    payment = Payment(
        reservation_id=reservation_id, amount=amount, payment_method=payment_method, payment_date=payment_date, guest_id=guest_id
    )
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment

def list_payments():
    return db.query(Payment).all()