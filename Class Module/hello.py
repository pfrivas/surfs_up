# CREATE A NEW PYTHON FILE CALLED FLASK

# import dependency
from flask import Flask

# assign variable
app = Flask(__name__)

#defines starting point (root)
@app.route('/')
def hello_world():
    return 'Hello World'

# Access WSGI Server (Waitress)
#if __name__ == "__main__":
 # from waitress import serve
 # serve(hello_world, host="0.0.0.0", port=8080)

# Export App
    # export FLASK_APP=helloworld.py
    # flask run
