from sqlalchemy import Column, Integer, String, Text, ForeignKey, Float, DateTime, Date
from sqlalchemy.orm import relationship
from database import Base

class Guest(Base):
    __tablename__ = "guests"

    guest_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(Text, unique=True, nullable=False)
    phone_number = Column(Integer)

    reservations = relationship("Reservation", back_populates="guest")
    payments = relationship("Payment", back_poulates="guest")

class Room(Base):
    __tablename__ = "rooms"

    room_id = Column(Integer, primary_key=True)
    room_number = Column(Integer, nullable=False)
    room_type = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    status = Column(String, nullable=False)

    reservations = relationship("Reservation", back_populates="room")

class Reservation(Base):
    __tablename__ = "reservations"

    reservation_id = Column(Integer, primary_key=True)
    guest_id = Column(Integer, ForeignKey("guests.guest_id"))
    room_id = Column(Integer, ForeignKey("rooms.room_id"))
    check_in_date = Column(DateTime)
    check_out_time = Column(DateTime)
    status = Column(Text)

    guest = relationship("Guest", back_populates="reservations")
    room = relationship("Room", back_populates="reservations")
    payment = relationship("Payment", back_populates="reservation", uselist=False)


class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True)
    reservation_id = Column(Integer, ForeignKey("reservations.reservation_id"))
    amount = Column(Float, nullable=False)
    payment_method = Column(Text, nullable=False)
    payment_date = Column(Date)

    reservation = relationship("Reservation", back_populates="payment")
    guest_id = Column(Integer, ForeignKey("guests.guest_id"))
    guest = relationship("Guest", back_populates="payments")