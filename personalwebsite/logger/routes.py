from flask import Blueprint, current_app, request, jsonify, Response
from personalwebsite import db
from personalwebsite.models import VisitorInfo


logger = Blueprint('logger', __name__)


@logger.route('/log-visitor', methods=['POST'])
def log_visitor():
    info = request.get_json()
    if info['ipinfo'] == 'true':
        newVisitor = VisitorInfo(
                ip=info['ip'], browser=info['browser'],
                operating_system=info['operatingSystem'],
                device_type=info['deviceType'],
                country=info['country'],
                region=info['region'],
                city=info['city'],
                postal=info['postal'],
                timezone=info['timezone'],
                page=info['page']
                )
    else:
        newVisitor = VisitorInfo(
                browser=info['browser'],
                operating_system=info['operatingSystem'],
                device_type=info['deviceType'],
                page=info['page']
                )
    db.session.add(newVisitor)
    db.session.commit()

    return Response(status=204)
