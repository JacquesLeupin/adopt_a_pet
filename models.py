from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    '''connect to database.'''
    db.app = app
    db.init_app(app)

class Pet(db.Model):

    __tablename__ = 'pets'

    id = db.Column(db.Integer,
        primary_key=True,
        autoincrement=True)
    
    name = db.Column(db.String(),
                    nullable=False)

    species = db.Column(db.String(),
                    nullable=False)
    
    photo_url = db.Column(db.String(),
                    nullable=True)
    
    age = db.Column(db.Integer(),
                    nullable=False)

    notes = db.Column(db.String(),
                    nullable=True)
    
    available = db.Column(db.Boolean(),
                    default=True,
                    nullable=False)
    
    def __repr__(self):
        return f'{self.name}'

