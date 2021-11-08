from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import InputRequired


class Search(FlaskForm):
    search = StringField('Search', [validators.InputRequired()])
    submit_search = SubmitField('submit')


class City(FlaskForm):
    insee = StringField('Insee', [validators.InputRequired()])
    submit_city = SubmitField('submit')


class Around(FlaskForm):
    insee = StringField('Insee', [validators.InputRequired()])
    submit_around = SubmitField('submit')