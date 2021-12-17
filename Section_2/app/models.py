from app import db
from flask_login import UserMixin
Baskets = db.Table('Baskets',
             db.Column('technology',db.Integer,db.ForeignKey('basket.id')),
             db.Column('sign_id',db.Integer,db.ForeignKey('sign.id')))

class Sign_In(db.Model,UserMixin):
     __tablename__ = 'sign'
     id=db.Column(db.Integer,primary_key=True)
     Username =db.Column(db.String(500), index=True, unique=True)
     Password =db.Column(db.String(500),index=True, unique=False)


class Shopping_Basket(db.Model):
    __tablename__ = 'basket'
    id=db.Column(db.Integer,primary_key=True)
    Ipad=db.Column(db.Integer)
    Lenovo_Thinkpad_Laptop=db.Column(db.Integer)
    Samsung_OLED_TV=db.Column(db.Integer)
    Macbook= db.Column(db.Integer)
    One_Plus_9= db.Column(db.Integer)
    I_Mac=db.Column(db.Integer)
    Xiaomi_Laptop=db.Column(db.Integer)
    Iphone_12_pro= db.Column(db.Integer)
    Lenovo_Thinkbook= db.Column(db.Integer)
    Mechanical_Keyboard= db.Column(db.Integer)
    user_basket=db.relationship('Sign_In',secondary=Baskets,backref=db.backref('shopping',lazy='dynamic'))
