from flask import Blueprint, jsonify, request
from ..models import Guest

guest_bp = Blueprint('guests', __name__)

@guest_bp.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([
        {'id': g.id, 'name': g.name, 'occupation': g.occupation}
        for g in guests
    ])

@guest_bp.route('/guests', methods=['POST'])
def create_guest():
    data = request.get_json()
    name = data.get('name')
    occupation = data.get('occupation')
    if not name or not occupation:
        return {"error": "Missing name or occupation"}, 400
    from ..models.guest import Guest, db
    guest = Guest(name=name, occupation=occupation)
    db.session.add(guest)
    db.session.commit()
    return {'id': guest.id, 'name': guest.name, 'occupation': guest.occupation}, 201
