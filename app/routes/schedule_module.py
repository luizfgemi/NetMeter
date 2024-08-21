from flask import Blueprint, jsonify
from modules.auth import auth
from .speedtest_module import run_speedtest
import schedule

schedule_bp = Blueprint('schedule', __name__)

@schedule_bp.route('/schedule_test', methods=['POST'])
@auth.login_required
def schedule_test():
    schedule.every().hour.do(run_speedtest)
    return jsonify({"message": "Speedtest scheduled every hour."})

@schedule_bp.route('/schedule_test_custom/<int:minutes>', methods=['POST'])
@auth.login_required
def schedule_test_custom(minutes):
    schedule.every(minutes).minutes.do(run_speedtest)
    return jsonify({"message": f"Speedtest scheduled every {minutes} minutes."})
