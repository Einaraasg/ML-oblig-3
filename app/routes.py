from app import app
from flask import render_template, session, redirect, url_for
import pickle

from app.predict import predict
from app.forms import DataForm

app.config['SECRET_KEY'] = 'DAT158'

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods =['GET','POST'])

def index():

    form = DataForm()

    if form.validate_on_submit():

        for fieldname,value in form.data.items():
            session[fieldname] = value

        pred = predict(session)
        session['pred'] = pred

        return redirect(url_for('index'))
    return render_template('index.html', form=form)

