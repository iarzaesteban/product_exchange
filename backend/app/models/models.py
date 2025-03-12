import uuid
from sqlalchemy import Column, String, ForeignKey, Float, DateTime, Integer
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hash_password = Column(String, nullable=False)
    wallet_address = Column(String, unique=True, nullable=False)
    reputation = Column(Float, default=0)
    registration_date = Column(DateTime, default=datetime.utcnow)

class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    category = Column(String)
    image_url = Column(String)
    barter_value = Column(Float)
    state = Column(String, default="Available")
    creation_date = Column(DateTime, default=datetime.utcnow)

    owner = relationship("User")

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    offering_user_id = Column(String, ForeignKey("users.id"), nullable=False)
    receiving_user_id = Column(String, ForeignKey("users.id"), nullable=False)
    offered_product_id = Column(String, ForeignKey("products.id"), nullable=False)
    received_product_id = Column(String, ForeignKey("products.id"), nullable=False)
    state = Column(String, default="Pending")
    transaction_hash = Column(String, unique=True)
    transaction_date = Column(DateTime, default=datetime.utcnow)

    offering_user = relationship("User", foreign_keys=[offering_user_id])
    receiving_user = relationship("User", foreign_keys=[receiving_user_id])
    offered_product = relationship("Product", foreign_keys=[offered_product_id])
    received_product = relationship("Product", foreign_keys=[received_product_id])

class Credit(Base):
    __tablename__ = "credits"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    amount = Column(Float, default=0)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User")

class Review(Base):
    __tablename__ = "reviews"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    evaluator_user_id = Column(String, ForeignKey("users.id"), nullable=False)
    evaluated_user_id = Column(String, ForeignKey("users.id"), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String)
    review_date = Column(DateTime, default=datetime.utcnow)

    evaluator = relationship("User", foreign_keys=[evaluator_user_id])
    evaluated = relationship("User", foreign_keys=[evaluated_user_id])
