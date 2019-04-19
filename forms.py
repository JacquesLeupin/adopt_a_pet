from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, AnyOf, URL

class AddPetForm(FlaskForm):
    pet_name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(), AnyOf(values=['cat', 'dog', 'porcupine'], message="Can only choose cat, dog, or porcupine")])
    photo_url = StringField("Photo URL", validators=[InputRequired(), URL(message="Please enter valid URL")])
    age = IntegerField('Age', validators=[InputRequired(), NumberRange(min=0, max=30, message="Please enter number between 0-30")])
    notes = StringField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL", validators=[InputRequired(), URL(message="Please enter valid URL")])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField('available')