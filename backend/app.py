import os
import schedule  
import time
from threading import Thread
from flask import Flask, send_from_directory
from flask_cors import CORS
from .auth import auth, setup_initial_user
from .db import create_tables
from .routes.speedtest import speedtest_bp
from .routes.schedule import schedule_bp
from .routes.results import results_bp

app = Flask(__name__, static_folder="../build")
CORS(app)

create_tables()
setup_initial_user()

app.register_blueprint(speedtest_bp)
app.register_blueprint(schedule_bp)
app.register_blueprint(results_bp)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_frontend(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    scheduler_thread = Thread(target=run_scheduler)
    scheduler_thread.start()
    app.run(host='0.0.0.0', port=80)
