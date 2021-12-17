import os
import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app, db, models, views
from flask_login import LoginManager
import logging

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config.from_object('config')
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        #the basedir lines could be added like the original db
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.create_all()
        login_manager= LoginManager()
        login_manager.login_view="UserSignIn"
        login_manager.init_app(app)

        @login_manager.user_loader
        def load_user(id):
            return Sign_In.query.get(int(id))

        pass


    def tearDown(self):
        db.session.remove()
        db.drop_all()
    def test_addtaskroute(self):
        response = self.app.get('/UserSignIn',
                               follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("hello")
    def populate_db(self):
        p=Sign_In(Username=username,Password=generate_password_hash(form.Password.data, method="sha256"))
        bask=Shopping_Basket(Ipad=0,Lenovo_Thinkpad_Laptop=0,Samsung_OLED_TV=0,Macbook=0,One_Plus_9=0,I_Mac=0,Xiaomi_Laptop=0,Iphone_12_pro=0,Lenovo_Thinkbook=0,Mechanical_Keyboard=0)
        db.session.add(p)
        db.session.add(bask)
        db.session.commit()
        p.shopping.append(bask)
        db.session.commit()

    def login(self):
        self.client.post('/auth/login', data={
            'username': 'susan',
            'password': 'foo',
        })
