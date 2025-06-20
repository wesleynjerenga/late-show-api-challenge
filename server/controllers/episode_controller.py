from flask import Blueprint, jsonify
from ..models.episode import Episode
from ..models import db

episode_bp = Blueprint('episode', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def list_episodes():
    episodes = Episode.query.all()
    return jsonify([e.to_dict() for e in episodes]), 200
