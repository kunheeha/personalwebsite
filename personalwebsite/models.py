from personalwebsite import db


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
