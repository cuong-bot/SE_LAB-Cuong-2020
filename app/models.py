from sqlalchemy import Column, Integer, String
from . import db


class Category(db.Model):
    """ Product category """
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)

class Product(db.Model):
    """ Manage product info """
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)

