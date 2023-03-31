from flask import Flask, request, jsonify
from services.service import BookmarkService
from daos.bookmark_dao import BookmarkDAO
from src.barkylib.domain.models import Bookmark
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

engine = create_engine('sqlite:///bookmarks.db')
Session = sessionmaker(bind=engine)
session = Session()

bookmark_dao = BookmarkDAO()
bookmark_service = BookmarkService(bookmark_dao)

@app.route('/bookmarks', methods=['GET'])
def get_all_bookmarks():
    bookmarks = bookmark_service.get_all_bookmarks()
    return jsonify([bookmark.to_dict() for bookmark in bookmarks])

@app.route('/bookmarks/<int:bookmark_id>', methods=['GET'])
def get_bookmark_by_id(bookmark_id):
    bookmark = bookmark_service.get_bookmark_by_id(bookmark_id)
    if bookmark:
        return jsonify(bookmark.to_dict())
    else:
        return jsonify({'error': 'Bookmark not found'})

@app.route('/bookmarks', methods=['POST'])
def create_bookmark():
    name = request.json['name']
    url = request.json['url']
    new_bookmark = Bookmark(name=name, url=url)
    bookmark_id = bookmark_service.create_bookmark(new_bookmark)
    return jsonify({'id': bookmark_id})

@app.route('/bookmarks/<int:bookmark_id>', methods=['PUT'])
def update_bookmark(bookmark_id):
    name = request.json['name']
    url = request.json['url']
    bookmark = Bookmark(name=name, url=url)
    bookmark_service.update_bookmark(bookmark_id, bookmark)
    return jsonify({'success': True})

@app.route('/bookmarks/<int:bookmark_id>', methods=['DELETE'])
def delete_bookmark(bookmark_id):
    bookmark_service.delete_bookmark(bookmark_id)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run()
