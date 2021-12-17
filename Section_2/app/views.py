from flask import render_template, flash,session, url_for
from app import app
from app import models
from .forms import *
from app.models import *
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
import logging
app.logger.info('index route request')
@app.route('/',methods=['GET','POST'])
def HomePage():
    return render_template('InfoPage.html')
@app.route('/UserSignIn',methods=['GET','POST'])
def UserSignIn():
    app.logger.info('arrived at sign in page')
    sign_in= Sign_In
    form = SignInForm()
    if form.validate_on_submit():
        username=form.Username.data
        databases= sign_in.query.filter_by(Username=username).first()
        if databases:
            if check_password_hash(databases.Password,form.Password.data):
                login_user(databases)
                session['username']=username
                products=ChosenProducts()
                basket=databases.shopping
                numberone=basket[0].Ipad+basket[0].Lenovo_Thinkbook+basket[0].Samsung_OLED_TV+basket[0].Macbook+basket[0].One_Plus_9+basket[0].I_Mac+basket[0].Xiaomi_Laptop+basket[0].Iphone_12_pro
                numbertwo=basket[0].Lenovo_Thinkpad_Laptop+basket[0].Mechanical_Keyboard
                number=numberone+numbertwo
                if products.validate_on_submit:
                    if products.Ipad.data is None:
                        products.Ipad.data=0
                        print(products.Ipad.data)
                    if products.thinkbook.data is None:
                            products.thinkbook.data=0
                    if products.thinkpad.data is None:
                        products.thinkpad.data=0
                    if products.samsung.data is None:
                        products.samsung.data=0
                    if products.macbook.data is None:
                        products.macbook.data=0
                    if products.mech_key.data is None:
                        products.mech_key.data=0
                    if products.pro_12.data is None:
                        products.pro_12.data=0
                    if products.Xiaomi.data is None:
                        products.Xiaomi.data=0
                    if products.eye_mac.data is None:
                        products.eye_mac.data=0
                    if products.oneplus.data is None:
                        products.oneplus.data=0
                    basket[0].Ipad=basket[0].Ipad+products.Ipad.data
                    basket[0].Lenovo_Thinkbook=basket[0].Lenovo_Thinkbook+products.thinkbook.data
                    basket[0].Lenovo_Thinkpad_Laptop=basket[0].Lenovo_Thinkpad_Laptop+products.thinkpad.data
                    basket[0].Samsung_OLED_TV=basket[0].Samsung_OLED_TV+products.samsung.data
                    basket[0].Macbook=basket[0].Macbook+products.macbook.data
                    basket[0].Mechanical_Keyboard=basket[0].Mechanical_Keyboard+products.mech_key.data
                    basket[0].Iphone_12_pro=basket[0].Iphone_12_pro+products.pro_12.data
                    basket[0].Xiaomi_Laptop=basket[0].Xiaomi_Laptop+products.Xiaomi.data
                    basket[0].I_Mac=basket[0].I_Mac+products.eye_mac.data
                    basket[0].One_Plus_9=basket[0].One_Plus_9+products.oneplus.data
                    numberone=basket[0].Ipad+basket[0].Lenovo_Thinkbook+basket[0].Samsung_OLED_TV+basket[0].Macbook+basket[0].One_Plus_9+basket[0].I_Mac+basket[0].Xiaomi_Laptop+basket[0].Iphone_12_pro
                    numbertwo=basket[0].Lenovo_Thinkpad_Laptop+basket[0].Mechanical_Keyboard
                    number=numberone+numbertwo
                    return render_template('Shop_site.html',basket=basket,form=products,username=username,cart_size=number)
                else:
                    app.logger.warning('flask validator not working')
                return render_template('Shop_site.html',basket=basket,form=products,username=username,cart_size=number)
        flash("Incorrect password/username")
    return render_template('UserSignIn.html',sign=sign_in,form=form)
@app.route('/Register',methods=['GET','POST'])
def Register():
        sign_in=Sign_In
        form = SignInForm()
        if form.validate_on_submit():
            username=form.Username.data
            databases= sign_in.query.filter_by(Username=username).first()
            if not databases:
                    p=Sign_In(Username=username,Password=generate_password_hash(form.Password.data, method="sha256"))
                    bask=Shopping_Basket(Ipad=0,Lenovo_Thinkpad_Laptop=0,Samsung_OLED_TV=0,Macbook=0,One_Plus_9=0,I_Mac=0,Xiaomi_Laptop=0,Iphone_12_pro=0,Lenovo_Thinkbook=0,Mechanical_Keyboard=0)
                    db.session.add(p)
                    db.session.add(bask)
                    db.session.commit()
                    p.shopping.append(bask)
                    db.session.commit()
                    flash("User has been registered")
            flash("User already exists")
        return render_template('Register.html',sign=sign_in,form=form)
@app.route('/Shop_site', methods=['GET','POST'])
@login_required
def Shop_site():
    user_username=session['username']
    app.logger.warning('flask validator not working')
    sign_in=Sign_In
    user=sign_in.query.filter_by(Username=user_username).first()
    products=ChosenProducts()
    basket=user.shopping
    numberone=basket[0].Ipad+basket[0].Lenovo_Thinkbook+basket[0].Samsung_OLED_TV+basket[0].Macbook+basket[0].One_Plus_9+basket[0].I_Mac+basket[0].Xiaomi_Laptop+basket[0].Iphone_12_pro
    numbertwo=basket[0].Lenovo_Thinkpad_Laptop+basket[0].Mechanical_Keyboard
    number=numberone+numbertwo
    if products.Ipad.data is None:
        products.Ipad.data=0
    if products.thinkbook.data is None:
            products.thinkbook.data=0
    if products.thinkpad.data is None:
        products.thinkpad.data=0
    if products.samsung.data is None:
        products.samsung.data=0
    if products.macbook.data is None:
        products.macbook.data=0
    if products.mech_key.data is None:
        products.mech_key.data=0
    if products.pro_12.data is None:
        products.pro_12.data=0
    if products.Xiaomi.data is None:
        products.Xiaomi.data=0
    if products.eye_mac.data is None:
        products.eye_mac.data=0
    if products.oneplus.data is None:
        products.oneplus.data=0
    if products.validate_on_submit():
        if products.Ipad.data is None:
            products.Ipad.data=0
        if products.thinkbook.data is None:
                products.thinkbook.data=0
        if products.thinkpad.data is None:
            products.thinkpad.data=0
        if products.samsung.data is None:
            products.samsung.data=0
        if products.macbook.data is None:
            products.macbook.data=0
        if products.mech_key.data is None:
            products.mech_key.data=0
        if products.pro_12.data is None:
            products.pro_12.data=0
        if products.Xiaomi.data is None:
            products.Xiaomi.data=0
        if products.eye_mac.data is None:
            products.eye_mac.data=0
        if products.oneplus.data is None:
            products.oneplus.data=0
        basket[0].Ipad=basket[0].Ipad+products.Ipad.data
        basket[0].Lenovo_Thinkbook=basket[0].Lenovo_Thinkbook+products.thinkbook.data
        basket[0].Lenovo_Thinkpad_Laptop=basket[0].Lenovo_Thinkpad_Laptop+products.thinkpad.data
        basket[0].Samsung_OLED_TV=basket[0].Samsung_OLED_TV+products.samsung.data
        basket[0].Macbook=basket[0].Macbook+products.macbook.data
        basket[0].Mechanical_Keyboard=basket[0].Mechanical_Keyboard+products.mech_key.data
        basket[0].Iphone_12_pro=basket[0].Iphone_12_pro+products.pro_12.data
        basket[0].Xiaomi_Laptop=basket[0].Xiaomi_Laptop+products.Xiaomi.data
        basket[0].I_Mac=basket[0].I_Mac+products.eye_mac.data
        basket[0].One_Plus_9=basket[0].One_Plus_9+products.oneplus.data
        numberone=basket[0].Ipad+basket[0].Lenovo_Thinkbook+basket[0].Samsung_OLED_TV+basket[0].Macbook+basket[0].One_Plus_9+basket[0].I_Mac+basket[0].Xiaomi_Laptop+basket[0].Iphone_12_pro
        numbertwo=basket[0].Lenovo_Thinkpad_Laptop+basket[0].Mechanical_Keyboard
        number=numberone+numbertwo
        db.session.commit()
        return render_template('Shop_site.html',basket=basket,form=products,username=user_username,cart_size=number)
    return render_template('Shop_site.html',basket=basket,form=products,username=user_username,cart_size=number)
@app.route('/Laptop',methods=['GET','POST'])
@login_required
def Laptop():
    sign_in=Sign_In
    username=session['username']
    products=ChosenProducts()
    databases=sign_in.query.filter_by(Username=username).first()
    basket=databases.shopping
    numberone=basket[0].Ipad+basket[0].Lenovo_Thinkbook+basket[0].Samsung_OLED_TV+basket[0].Macbook+basket[0].One_Plus_9+basket[0].I_Mac+basket[0].Xiaomi_Laptop+basket[0].Iphone_12_pro
    numbertwo=basket[0].Lenovo_Thinkpad_Laptop+basket[0].Mechanical_Keyboard
    number=numberone+numbertwo
    if products.validate_on_submit:
        print("hello")
        if products.thinkbook.data is None:
                products.thinkbook.data=0
        if products.thinkpad.data is None:
            products.thinkpad.data=0
        if products.macbook.data is None:
            products.macbook.data=0
        if products.Xiaomi.data is None:
            products.Xiaomi.data=0
        if products.eye_mac.data is None:
            products.eye_mac.data=0
        basket[0].Lenovo_Thinkbook=basket[0].Lenovo_Thinkbook+products.thinkbook.data
        basket[0].Lenovo_Thinkpad_Laptop=basket[0].Lenovo_Thinkpad_Laptop+products.thinkpad.data
        basket[0].Macbook=basket[0].Macbook+products.macbook.data
        basket[0].Xiaomi_Laptop=basket[0].Xiaomi_Laptop+products.Xiaomi.data
        basket[0].I_Mac=basket[0].I_Mac+products.eye_mac.data
        numberone=basket[0].Lenovo_Thinkbook+basket[0].Macbook+basket[0].I_Mac+basket[0].Xiaomi_Laptop
        numbertwo=basket[0].Lenovo_Thinkpad_Laptop
        db.session.commit()
    else:
        print("hellos")
        app.logger.info('here')
    return render_template('Laptop.html',basket=basket,form=products,username=username,cart_size=number)
@app.route('/Apple',methods=['GET','POST'])
@login_required
def Apple():
    user_username=session['username']
    sign_in=Sign_In
    user=sign_in.query.filter_by(Username=user_username).first()
    products=ChosenProducts()
    basket=user.shopping
    print("hello")
    numberone=basket[0].Ipad+basket[0].Lenovo_Thinkbook+basket[0].Samsung_OLED_TV+basket[0].Macbook+basket[0].One_Plus_9+basket[0].I_Mac+basket[0].Xiaomi_Laptop+basket[0].Iphone_12_pro
    numbertwo=basket[0].Lenovo_Thinkpad_Laptop+basket[0].Mechanical_Keyboard
    number=numberone+numbertwo
    print("hellos")
    if products.Ipad.data is None:
        products.Ipad.data=0
    if products.thinkbook.data is None:
            products.thinkbook.data=0
    if products.thinkpad.data is None:
        products.thinkpad.data=0
    if products.samsung.data is None:
        products.samsung.data=0
    if products.macbook.data is None:
        products.macbook.data=0
    if products.mech_key.data is None:
        products.mech_key.data=0
    if products.pro_12.data is None:
        products.pro_12.data=0
    if products.Xiaomi.data is None:
        products.Xiaomi.data=0
    if products.eye_mac.data is None:
        products.eye_mac.data=0
    if products.oneplus.data is None:
        products.oneplus.data=0
    if products.validate_on_submit():
        print("hello")
        basket[0].Ipad=basket[0].Ipad+products.Ipad.data
        basket[0].Macbook=basket[0].Macbook+products.macbook.data
        basket[0].Iphone_12_pro=basket[0].Iphone_12_pro+products.pro_12.data
        basket[0].I_Mac=basket[0].I_Mac+products.eye_mac.data
        numberone=basket[0].Ipad+basket[0].Macbook+basket[0].I_Mac+basket[0].Iphone_12_pro
        db.session.commit()
        return render_template('Apple.html',basket=basket,form=products,username=user_username,cart_size=number)
    return render_template('Apple.html',basket=basket,form=products,username=user_username,cart_size=number)
@app.route('/ChangePassword',methods=['GET','POST'])
@login_required
def ChangePassword():
    sign_in=Sign_In
    form= SignInForm()
    if form.validate_on_submit():
        username=form.Username.data
        databases= sign_in.query.filter_by(Username=username).first()
        print(databases.Password)
        if databases:
            password=form.Password.data
            databases.Password=password
            print(databases.Password)
            db.session.commit()
            print(databases.Password)
            return render_template('UserSignIn.html',sign=sign_in,form=form)
    return render_template('Changepassword.html',form=form)
@app.route('/Sign_Out')
@login_required
def Sign_Out():
    logout_user()
    session.pop('username',None)
    return render_template('InfoPage.html')
@app.route('/tv_keyboard',methods=['GET','POST'])
@login_required
def tv_keyboard():
    user_username=session['username']
    sign_in=Sign_In
    user=sign_in.query.filter_by(Username=user_username).first()
    products=ChosenProducts()
    basket=user.shopping
    numberone=basket[0].Ipad+basket[0].Lenovo_Thinkbook+basket[0].Samsung_OLED_TV+basket[0].Macbook+basket[0].One_Plus_9+basket[0].I_Mac+basket[0].Xiaomi_Laptop+basket[0].Iphone_12_pro
    numbertwo=basket[0].Lenovo_Thinkpad_Laptop+basket[0].Mechanical_Keyboard
    number=numberone+numbertwo
    if products.Ipad.data is None:
        products.Ipad.data=0
    if products.thinkbook.data is None:
            products.thinkbook.data=0
    if products.thinkpad.data is None:
        products.thinkpad.data=0
    if products.samsung.data is None:
        products.samsung.data=0
    if products.macbook.data is None:
        products.macbook.data=0
    if products.mech_key.data is None:
        products.mech_key.data=0
    if products.pro_12.data is None:
        products.pro_12.data=0
    if products.Xiaomi.data is None:
        products.Xiaomi.data=0
    if products.eye_mac.data is None:
        products.eye_mac.data=0
    if products.oneplus.data is None:
        products.oneplus.data=0
    if products.validate_on_submit():
        if products.samsung.data is None:
            products.samsung.data=0
        if products.mech_key.data is None:
            products.mech_key.data=0
        basket[0].Samsung_OLED_TV=basket[0].Samsung_OLED_TV+products.samsung.data
        basket[0].Mechanical_Keyboard=basket[0].Mechanical_Keyboard+products.mech_key.data
        numberone=basket[0].Samsung_OLED_TV
        numbertwo=basket[0].Mechanical_Keyboard
        db.session.commit()
        return render_template('Tvs-Keyboards.html',basket=basket,form=products,username=user_username,cart_size=number)
    return render_template('Tvs-Keyboards.html',basket=basket,form=products,username=user_username,cart_size=number)
@app.route('/Shopping_cart',methods=['GET','POST'])
@login_required
def Shopping_cart():
    user_username=session['username']
    sign_in=Sign_In
    user=sign_in.query.filter_by(Username=user_username).first()
    basket=user.shopping
    costone=(basket[0].Ipad*320)+(basket[0].Lenovo_Thinkbook*700)+(basket[0].Samsung_OLED_TV*2099)+(basket[0].Macbook*1300)+(basket[0].One_Plus_9*600)
    costtwo=(basket[0].Lenovo_Thinkpad_Laptop*900)+(basket[0].Mechanical_Keyboard*30)+(basket[0].I_Mac*1250)+(basket[0].Xiaomi_Laptop*750)+(basket[0].Iphone_12_pro*600)
    cost=costone+costtwo
    return render_template('basket.html',basket=basket,username=user_username,cost=cost)
