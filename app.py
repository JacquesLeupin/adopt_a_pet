from flask import Flask, request, redirect, render_template, flash
# from flask_wtf import FlaskForm
# from wtforms import StringField
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm
from flask_debugtoolbar import DebugToolbarExtension
from pat_finder import show_response

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecrethehe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)
connect_db(app)
db.create_all()



@app.route('/')
def index():
    print("HELLO WE ARE RUNNING REPONSE:" * 10)
    first_animal = show_response()
    animal = Pet(**first_animal) # **first_animal just means that you make keyword arguments: like (name=name1, species)
    db.session.add(animal)
    db.session.commit()
    pets = Pet.query.all()
    return render_template('base.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def pet_adder():

    pets = Pet.query.all()
    form = AddPetForm()

    if form.validate_on_submit():
        name1 = form.pet_name.data
        species1 = form.species.data
        photo_url1 = form.photo_url.data
        age1 = form.age.data
        notes1 = form.notes.data
        add_pet = Pet(name = name1, species = species1, photo_url = photo_url1, age = age1, notes = notes1)
        db.session.add(add_pet)
        db.session.commit()
        return redirect('/')
    
    else:
        return render_template('add_pet.html', form=form)

@app.route('/<int:petid>', methods=["GET", "POST"])
def pet_info(petid):

    pet = Pet.query.get_or_404(petid)
    form = EditPetForm()

    if form.validate_on_submit():

        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        return redirect('/')

    else:
        return render_template('pet_info.html', pet=pet, form=form)





