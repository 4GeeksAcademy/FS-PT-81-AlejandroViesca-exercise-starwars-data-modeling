import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    pricing = Column(Float)
    weight = Column(Float)
    color = Column(String)

class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    address = Column(String)

class Shopping_Carts(Base):
    __tablename__ = 'shopping_carts'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    price = Column(Float)

    product_id = Column(Integer, ForeignKey('products.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    bill_id = Column(Integer, ForeignKey('bills.id'))

    product = relationship('Products', backref='shopping_carts')
    customer = relationship('Customers', backref='shopping_carts')
    bill = relationship('Bills', backref='shopping_carts')


class Bills(Base):
    __tablename__ = 'bills'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    total_price = Column(Float)
    status = Column(Enum("paid","pending","refunded", name="status_enum"))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
