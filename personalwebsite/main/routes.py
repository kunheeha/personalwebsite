from flask import (
    Blueprint, render_template, current_app, request, jsonify, url_for
        )
from personalwebsite import db, mail
from personalwebsite.models import Myself, Contact, Skill, Project
from flask_mail import Message


main = Blueprint('main', __name__)


@main.route('/')
def index():
    myid = int(current_app.config['MYSELF_ID'])
    me = db.get_or_404(Myself, myid)
    return render_template('index.html', me=me)


@main.route('/about')
def about():
    myid = int(current_app.config['MYSELF_ID'])
    me = db.get_or_404(Myself, myid)
    contacts = db.session.execute(
            db.select(Contact).filter_by(me_id=myid)).scalars().all()
    email = db.session.execute(
            db.select(Contact).filter_by(
                me_id=myid, contact_type="email")).scalar()
    contacts = [contact for contact in contacts
                if contact.contact_type != "email"]
    profile_photo = url_for('static', filename='images/'+me.profile_photo)
    skills = db.session.execute(db.select(Skill)).scalars().all()
    projects = db.session.execute(db.select(Project).limit(4)).scalars().all()

    return render_template('about.html', me=me, email=email,
                           contacts=contacts, projects=projects, skills=skills,
                           profile_photo=profile_photo)


@main.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        # why is this so broken up? because pycodestyle
        sender_name = (
                f"{request.form.get('fname')} {request.form.get('lname')}"
                )
        sender_email = request.form.get('email')
        sender_message = request.form.get('message')
        to_receive = Message(subject='From Website',
                             sender='kunheeha@gmail.com',
                             recipients=['kunheeha@gmail.com'])
        to_send = Message(subject='Message Received',
                          sender='kunheeha@gmail.com',
                          recipients=[sender_email])
        to_receive.html = render_template('email_templates/to_me.html',
                                          sender_name=sender_name,
                                          sender_email=sender_email,
                                          sender_message=sender_message)
        to_send.html = render_template('email_templates/autoresponse.html',
                                       sender_name=sender_name)

        try:
            mail.send(to_receive)
            mail.send(to_send)
            return jsonify(status=True)
        except Exception:
            return jsonify(status=False)


@main.route('/projects')
def projects():
    projects = db.session.execute(db.select(Project)).scalars().all()
    return render_template('projects.html', projects=projects)


@main.route('/project/<int:project_id>')
def project_view(project_id):
    project = db.get_or_404(Project, project_id)
    return render_template('placeholder.html')
