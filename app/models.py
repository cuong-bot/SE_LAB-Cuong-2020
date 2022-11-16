""" Define database Models """
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    

class Category(BaseModel):
    """ Product category """
    __tablename__ = 'category'
    name = Column(String(20), nullable=False)
    product = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name

class Product(BaseModel):
    """ Manage product info """
    __tablename__ = 'product'
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(200))
    price = Column(Float, default=0)
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.now())
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name

if __name__ == '__main__':
    db.create_all()
