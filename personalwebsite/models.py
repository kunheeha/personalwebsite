from personalwebsite import db
from datetime import datetime


class Myself(db.Model):
    __tablename__ = "me"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False, default="Kunhee")
    last_name = db.Column(db.String, nullable=False, default="Ha")
    about = db.Column(db.String, nullable=False, default=(
        "Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint"
        " cillum sint consectetur cupidatat."
        ))
    profile_photo = db.Column(db.String, default="default_profile_photo.jpg")
    cv_file = db.Column(db.String)
    contacts = db.relationship("Contact", backref="me")


class Contact(db.Model):
    __tablename__ = "contacts"
    id = db.Column(db.Integer, primary_key=True)
    contact_type = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False)
    me_id = db.Column(db.Integer, db.ForeignKey("me.id"))


class Skill(db.Model):
    __tablename__ = "skills"
    id = db.Column(db.Integer, primary_key=True)
    skill = db.Column(db.String, nullable=False, default="Arch btw")


class Project(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    source_code_link = db.Column(db.String, nullable=False)
    webapp = db.Column(db.Boolean, nullable=False, default=False)
    deployed = db.Column(db.Boolean, nullable=False, default=False)
    live_link = db.Column(db.String)
    brief = db.Column(db.String, nullable=False,
                      server_default="a plan for world domination",
                      default="a plan for world domination")
    show_on_main = db.Column(db.Boolean, default=False, server_default="false")


class VisitorInfo(db.Model):
    __tablename__ = "visitors"
    id = db.Column(db.Integer, primary_key=True)
    date_visited = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    ip = db.Column(db.String)
    browser = db.Column(db.String(20))
    operating_system = db.Column(db.String(10))
    device_type = db.Column(db.String(10))
    country = db.Column(db.String(5))
    region = db.Column(db.String(50))
    city = db.Column(db.String(50))
    postal = db.Column(db.String(10))
    timezone = db.Column(db.String(20))
    page = db.Column(db.String(10))
