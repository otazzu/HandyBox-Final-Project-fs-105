# This file was created to run the application on heroku using gunicorn.
# Read more about it here: https://devcenter.heroku.com/articles/python-gunicorn

from app import app as application, socketio
import os


if __name__ == "__main__":
    application.run()
    PORT = int(os.environ.get('PORT', 3001))
    socketio.run(application, host='0.0.0.0', port=PORT, debug=True)