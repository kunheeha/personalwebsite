from personalwebsite import db
from flask import current_app

class Myself(db.Model):
    __tablename__ = "me"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False, default="Kunhee")
    last_name = db.Column(db.String, nullable=False, default="Ha")
    about = db.Column(db.String, nullable=False, default="Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat.")
    email = db.Column(db.String, nullable=False, default="kunheeha@gmail.com")
    profile_photo = db.Column(db.String, default="default_profile_photo.jpg")
    cv_file = db.Column(db.String)


class Skill(db.Model):
    __tablename__ = "skills"
    id = db.Column(db.Integer, primary_key=True)
    skill = db.Column(db.String, nullable=False, default="Arch btw")
