import os
import time
from threading import Thread
import schedule  
from flask import Flask, send_from_directory
from flask_cors import CORS
from routes import results_bp, schedule_bp, speedtest_bp
from modules import setup_initial_user, create_tables

# Configura a aplicação Flask
app = Flask(__name__, static_folder="static")

CORS(app)

create_tables()
setup_initial_user()

app.register_blueprint(speedtest_bp)
app.register_blueprint(schedule_bp)
app.register_blueprint(results_bp)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_frontend(path):
    return send_from_directory(app.root_path, 'index.html')

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    scheduler_thread = Thread(target=run_scheduler)
    scheduler_thread.start()
    app.run(host='0.0.0.0', port=5000)
