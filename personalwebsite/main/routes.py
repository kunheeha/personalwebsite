from flask import Blueprint, render_template, current_app
from personalwebsite import db
from personalwebsite.models import Myself, Skill


main = Blueprint('main', __name__)


@main.route('/')
def index():
    myid = int(current_app.config['MYSELF_ID'])
    me = db.get_or_404(Myself, myid)

    return render_template('index.html', me=me)
