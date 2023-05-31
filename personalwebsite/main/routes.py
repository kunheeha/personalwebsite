from flask import Blueprint, render_template, current_app
from personalwebsite import db
from personalwebsite.models import Myself, Contact


main = Blueprint('main', __name__)


@main.route('/')
def index():
    myid = int(current_app.config['MYSELF_ID'])
    me = db.get_or_404(Myself, myid)
    contacts = db.session.execute(
            db.select(Contact).filter_by(me_id=myid)).scalars().all()
    email = db.session.execute(
            db.select(Contact).filter_by(
                me_id=myid, contact_type="email")).scalar()
    contacts = [contact for contact in contacts
                if contact.contact_type != "email"]

    return render_template('index.html', me=me, email=email, contacts=contacts)
