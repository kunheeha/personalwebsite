from flask import Blueprint, render_template
from personalwebsite import db


blog = Blueprint('blog', __name__)


@blog.route('/blog')
def blog():
    return render_template('placeholder.html')
