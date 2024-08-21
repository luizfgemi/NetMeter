# routes/results.py

from flask import Blueprint, jsonify
from modules.auth import auth
from modules.db import cursor

results_bp = Blueprint('results', __name__)

@results_bp.route('/results', methods=['GET'])
@auth.login_required
def get_results():
    cursor.execute('SELECT * FROM results ORDER BY timestamp DESC')
    results = cursor.fetchall()
    return jsonify({"results": results})
