from flask import Blueprint, jsonify, request
from ..models.appearance import Appearance, db

appearance_bp = Blueprint('appearance', __name__)

@appearance_bp.route('/appearances', methods=['GET'])
def list_appearances():
    appearances = Appearance.query.all()
    return jsonify([
        {
            'id': a.id,
            'rating': a.rating,
            'guest_id': a.guest_id,
            'episode_id': a.episode_id
        } for a in appearances
    ]), 200

@appearance_bp.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    guest_id = data.get('guest_id')
    episode_id = data.get('episode_id')
    if not all([rating, guest_id, episode_id]):
        return {"error": "Missing rating, guest_id, or episode_id"}, 400
    try:
        appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
        db.session.add(appearance)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400
    return {
        'id': appearance.id,
        'rating': appearance.rating,
        'guest_id': appearance.guest_id,
        'episode_id': appearance.episode_id
    }, 201
