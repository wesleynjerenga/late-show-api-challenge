from flask import Blueprint, jsonify, request
from ..models.episode import Episode
from ..models import db
from flask_jwt_extended import jwt_required

episode_bp = Blueprint('episode', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def list_episodes():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    title_filter = request.args.get('title')
    query = Episode.query
    if title_filter:
        query = query.filter(Episode.title.ilike(f"%{title_filter}%"))
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    episodes = [e.to_dict() for e in pagination.items]
    return jsonify({
        'episodes': episodes,
        'total': pagination.total,
        'page': pagination.page,
        'pages': pagination.pages
    }), 200

@episode_bp.route('/episodes', methods=['POST'])
@jwt_required()
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
