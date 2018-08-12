from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, Length
from wtforms import StringField, PasswordField, SubmitField, BooleanField


class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[
        DataRequired(),
        Email(),
        Length(3, 64)])

    password = PasswordField('Senha', validators=[
        DataRequired(),
        Length(3, 6)])

    remember_me = BooleanField('Lembrar')
    submit = SubmitField('Entrar')


class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[
        DataRequired(),
        Length(0, 10)])

    last_name = StringField('First Name', validators=[
        DataRequired(),
        Length(0, 10)])

    email = StringField('E-mail', validators=[
        DataRequired(),
        Email(),
        Length(3, 64)])

    password = PasswordField('Senha', validators=[
        DataRequired(),
        Length(3, 6)])

    submit = SubmitField('Solicitar')
