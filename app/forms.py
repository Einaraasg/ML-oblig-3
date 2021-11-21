from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange


class DataForm(FlaskForm):
    #submit variabler

    budget = IntegerField('Budget of movie', validators=[DataRequired()])
    popularity = FloatField('Popularity of move', validators=[DataRequired()])
    runtime= FloatField('Runtime of movie in minuttes', validators=[DataRequired()])


    submit =SubmitField('Submit')