from datetime import datetime
from flask import Blueprint, jsonify
import speedtest
from modules.auth import auth
from modules.db import cursor, conn

speedtest_bp = Blueprint('speedtest', __name__)

def run_speedtest():
    s = speedtest.Speedtest()
    s.download()
    s.upload()
    results = s.results.dict()

    cursor.execute('''
    INSERT INTO results (timestamp, download_speed, upload_speed, ping)
    VALUES (?, ?, ?, ?)
    ''', (datetime.now(), results['download'] / 1e6, results['upload'] / 1e6, results['ping']))

    conn.commit()

@speedtest_bp.route('/speedtest', methods=['GET'])
@auth.login_required
def speedtest_endpoint():
    run_speedtest()
    return jsonify({"message": "Speedtest completed and results stored."})
