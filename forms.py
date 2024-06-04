from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, URL, Email, Length, ValidationError, InputRequired

class RateMovieForm(FlaskForm):
    rating = StringField(label="Votre evaluation sur 10 e.g 7.5", validators=[DataRequired()])
    review = TextAreaField(label="Votre Review", validators=[DataRequired()])
    submit = SubmitField(label="Entrer")

class FindMovieForm(FlaskForm):
    title = StringField(label="Nom Du Film",validators=[DataRequired(message="Veillez entrer un nom de film")])
    submit = SubmitField(label="Ajouter")