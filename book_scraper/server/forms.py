#Third part
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    send = SubmitField("Log In")


class BookForm(FlaskForm):
    book_url = StringField("book_url", validators=[DataRequired()])
    number_of_pages = IntegerField("number_of_pages", validators=[DataRequired()])
    cookie = StringField("cookie", validators=[DataRequired()])
    refer = StringField("refer", validators=[DataRequired()])
    send = SubmitField("Submit")
    logout = SubmitField("logout")


class AfterSubmit(FlaskForm):
    download = SubmitField("download")
    previous_page = SubmitField("return")
