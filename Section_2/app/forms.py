from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, DateField
from wtforms.validators import DataRequired,length,Regexp,NumberRange



class SignInForm(FlaskForm):
    Username = TextField(validators=[DataRequired(message="please enter a username "),length(min=0,max=15,message="username length must be between 4 and 15 characters")])
    Password = TextField(validators=[DataRequired(message="please enter a password"),length(min=0,max=20,message="password length must be between 8 and 20 characters")])

class ChosenProducts(FlaskForm):
    Ipad=IntegerField(validators=[NumberRange(min=0,message="Cannot have a negative number of products")]);
    thinkpad=IntegerField(validators=[NumberRange(min=0,message="Cannot have a negative number of products")]);
    thinkbook=IntegerField(validators=[NumberRange(min=0,message="Cannot have a negative number of products")]);
    samsung=IntegerField(validators=[NumberRange(min=0,message="Cannot have a negative number of products")]);
    macbook=IntegerField(validators=[NumberRange(min=0,message="Cannot have a negative number of products")]);
    mech_key=IntegerField(validators=[NumberRange(min=0,message="Cannot have a negative number of products")]);
    pro_12=IntegerField(validators=[NumberRange(min=0,message="Cannot have a negative number of products")]);
    Xiaomi=IntegerField(validators=[NumberRange(min=0,message="Cannot have a negative number of products")]);
    eye_mac=IntegerField(validators=[NumberRange(min=0,message="Cannot have a negative number of products")]);
    oneplus=IntegerField(validators=[NumberRange(min=0,message="Cannot have a negative number of products")]);
