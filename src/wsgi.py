# This file was created to run the application on heroku using gunicorn.
# Read more about it here: https://devcenter.heroku.com/articles/python-gunicorn

from app import app, socketio  # asegúrate de que estos estén definidos en app.py
import os

if __name__ == "__main__":
    # Exporta lo que Gunicorn necesita
    application = app  # Gunicorn buscará esto
    socketio.run(application, host='0.0.0.0', port=int(os.environ.get('PORT', 3001)), debug=True)