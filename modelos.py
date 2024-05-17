from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length


class RegistroForm(FlaskForm):
    usuario = StringField("Usuario", validators=[DataRequired(), Length(min=4, max=32)])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("Registrarse")


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    submit = SubmitField("Inciar Sesión") 