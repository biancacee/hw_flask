from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired 

from hwapp import hwapp_obj
from flask import render_template, flash, redirect

class TopCities(FlaskForm):
    city_name= StringField('City Name', validators=[DataRequired()])
    city_rank= IntegerField('City Rank',validators=[DataRequired()])
    is_visited= BooleanField('Visited')
    submit=SubmitField('Submit')


