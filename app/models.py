""" Define database Models """
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app import db, app

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
    image = Column(String(200), default=True)
    created_date = Column(DateTime, default=datetime.now())
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name

if __name__ == '__main__':
    
    product = [{
         "id": 1,
         "name": "iPhone 14 Pro",
         "description": "Apple, 128GB, RAM: 6GB, iOS16",
         "price": 29490000,
         "image":
         "https://res.cloudinary.com/dis95mx4d/image/upload/v1668644313/aditya-chinchure-CCqfZOeu8Oo-unsplash_nruqc9.jpg",
         "category_id": 1
        }, {
         "id": 2,
         "name": "iPad Pro 2020",
         "description": "Apple, 128GB, RAM: 6GB",
         "price": 37000000,
         "image":
         "https://res.cloudinary.com/dis95mx4d/image/upload/c_scale,h_6000,w_4000/v1668646108/ipad-pro-12-9-inch-wifi-128gb-2020-xam-400x460-1-400x460_dobr44.png",
         "category_id": 2
        }, {
         "id": 3,
         "name": "Laptop ASUS VivoBook Flip 14",
        "description": "ASUS, 512GB, RAM: 8GB",
         "price": 10990000,
         "image":
        "https://res.cloudinary.com/dis95mx4d/image/upload/c_scale,h_6000,w_4000/v1668645943/vivobook_14_whbn67.jpg",
         "category_id": 3
        },
        {
         "id": 4,
         "name": "MSI modern 14 b11",
        "description": "Samsung, 64GB, RAML: 6GB",
         "price": 11390000,
         "image":
        "https://res.cloudinary.com/dis95mx4d/image/upload/c_scale,h_6000,w_4000/v1668699264/msi_modern_b11_nzcbic.jpg",
         "category_id": 3
        },
        {
         "id": 5,
         "name": "Samsung Galaxy Z Flip4",
        "description": "Samsung, 128GB, RAM: 8GB",
         "price": 20990000,
         "image":
        "https://res.cloudinary.com/dis95mx4d/image/upload/c_scale,h_6000,w_4000,x_0/v1668702494/samsung-galaxy-z-flip4-tim-128gb-1_ul8jwl.jpg",
         "category_id": 1
        }]
        
    # c1 = Category(name='Phone')
    # c2 = Category(name='Tablet')
    # c3 = Category(name='Laptop')
    with app.app_context():
        for p in product:
            pro = Product(name=p['name'], description=p['description'],
             price=p['price'], image=p['image'], category_id=p['category_id'])
            db.session.add(pro)
        db.session.commit()
        # db.create_all()
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.add(c3)

    
