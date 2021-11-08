from hwapp import hwapp_obj
from hwapp.forms import TopCities
from flask import render_template, flash, redirect

from hwapp import db
from hwapp.models import User


@hwapp_obj.route('/',methods =['GET','POST'])
def cities():
    form=TopCities()
    name='Bianca'
    title= 'Top Cities'
    top_cities=User.query.all()
    if form.validate_on_submit():
        u = User(city_name=form.city_name.data,city_rank=form.city_rank.data)
        db.session.add(u)
        db.session.commit()
        return redirect('/')
    return render_template("home.html",form=form,top_cities=top_cities,name=name,title=title)


