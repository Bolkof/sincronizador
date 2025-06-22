from flask import Flask, send_from_directory
import os
from sync_logic import FILES_DIR, SYNC_DIR

app = Flask(__name__)

@app.route('/files/<path:filename>')
def serve_file(filename):
    return send_from_directory(FILES_DIR, filename)

@app.route('/Sync/metadata.csv')
def serve_metadata():
    return send_from_directory(SYNC_DIR, 'metadata.csv')

# Nota: Eliminado el app.run() para que sea controlado desde main.py