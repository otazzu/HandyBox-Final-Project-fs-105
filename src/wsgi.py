# This file was created to run the application on heroku using gunicorn.
# Read more about it here: https://devcenter.heroku.com/articles/python-gunicorn

from app import app
import os
from extensions import socketio as application


application.init_app(app)

if __name__ == "__main__":
    import eventlet
    import eventlet.wsgi
    PORT = int(os.environ.get('PORT', 3001))
    application.run(app, host='0.0.0.0', port=PORT, debug=True)