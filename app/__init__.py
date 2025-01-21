from flask import Flask, render_template, redirect, url_for, request
import os
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from .routes.items import items_bp
    from .routes.teleport import teleport_bp
    from .routes.fetch_items import fetch_items_bp

    app.register_blueprint(items_bp, url_prefix='/items')
    app.register_blueprint(teleport_bp, url_prefix='/teleport')
    app.register_blueprint(fetch_items_bp, url_prefix='/fetch_items')


    # Add a route for the root URL
    @app.route('/')
    def index():
      # Get the referer (previous page)
      referer = request.referrer
      # If the referer exists and it’s not the root or a non-matching URL, use it
      if referer and referer != url_for('index'):
        return redirect(referer)
      else:
        return redirect(url_for('items.manage_items'))

    # Enable flash messages
    app.secret_key = os.urandom(24)

    return app
