from flask import Blueprint, jsonify, request
from ..models.episode import Episode
from ..models import db

episode_bp = Blueprint('episode', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def list_episodes():
    episodes = Episode.query.all()
    return jsonify([e.to_dict() for e in episodes]), 200

@episode_bp.route('/episodes', methods=['POST'])
def create_episode():
    data = request.get_json()
    title = data.get('title')
    air_date = data.get('air_date')
    if not title or not air_date:
        return {"error": "Missing title or air_date"}, 400
    episode = Episode(title=title, air_date=air_date)
    db.session.add(episode)
    db.session.commit()
    return episode.to_dict(), 201
