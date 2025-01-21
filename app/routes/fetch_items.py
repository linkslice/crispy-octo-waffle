import os
import requests
from flask import Blueprint, jsonify, send_file

fetch_items_bp = Blueprint('fetch_items', __name__)

ITEMS_URL = "https://raw.githubusercontent.com/PrismarineJS/minecraft-data/master/data/bedrock/1.20.0/items.json"
CACHE_FILE = "/app/minecraft_items.json"

@fetch_items_bp.route('/', methods=['GET'])
def fetch_items():
    """Fetches and caches the Minecraft items list on the server."""
    if not os.path.exists(CACHE_FILE):
        try:
            response = requests.get(ITEMS_URL)
            response.raise_for_status()
            with open(CACHE_FILE, 'w') as file:
                file.write(response.text)
        except requests.RequestException as e:
            return jsonify({"error": "Failed to fetch items", "details": str(e)}), 500

    return send_file(CACHE_FILE)
