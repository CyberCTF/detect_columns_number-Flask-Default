from flask import Flask, render_template, jsonify
import json
import os
import mysql.connector
from flask import request

app = Flask(__name__, template_folder='templates', static_folder='static')

def load_metadata():
    """Charge les métadonnées depuis le fichier JSON dans deploy"""
    metadata_path = os.path.join(os.path.dirname(__file__), '..', 'deploy', 'metadata.json')
    try:
        with open(metadata_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "site": {"name": "CyberCTF Library", "description": "A Capture The Flag platform"},
            "navigation": {"main": [], "auth": []},
            "footer": {"links": [], "social": []},
            "challenge": {"title": "Challenge", "description": "Description", "skills": [], "points": 0},
            "cta": {"label": "Start", "link": "/"}
        }

# MySQL connection utility
def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get('MYSQL_HOST', 'db'),
        user=os.environ.get('MYSQL_USER', 'acme'),
        password=os.environ.get('MYSQL_PASSWORD', 'acmepass'),
        database=os.environ.get('MYSQL_DATABASE', 'acme_research'),
    )

@app.route('/')
def home():
    metadata = load_metadata()
    return render_template('home.html', metadata=metadata)

@app.route('/api/metadata')
def api_metadata():
    return jsonify(load_metadata())

@app.route('/lab', methods=['GET', 'POST'])
def lab():
    metadata = load_metadata()
    results = None
    error = None
    query = None
    if request.method == 'POST':
        project_id = request.form.get('project_id', '')
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            # Vulnerable query: direct string formatting
            query = f"SELECT * FROM projects WHERE id = {project_id}"
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            conn.close()
        except Exception as e:
            error = str(e)
    return render_template('lab.html', metadata=metadata, results=results, error=error, query=query)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 