import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# create the variable basedir pointing to the directory the program is running in
basedir = os.path.abspath(os.path.dirname(__file__))

# Create the connexion application instance
# This uses the basedir variable to create the Connexion app instance and give it the path to the swagger.yml file
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
# Create a variable app, which is the Flask instance initialized by Connexion
app = connex_app.app

# Configure the SqlAlchemy part of the app instance
# This line enables the SQLAlchemy echo, which
# prints all the generated SQL statements to the console
app.config["SQLALCHEMY_ECHO"] = True

# This line configures the SQLAlchemy database URI
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "people.db")

# This line configures the SQLAlchemy to track modifications of objects and emit signals
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create the SqlAlchemy db instance
# Create the db variable by calling SQLAlchemy(app).
# This initializes SQLAlchemy by passing the app configuration information that was just set
db = SQLAlchemy(app)

# Initialize Marshmallow
# Create the ma variable by calling Marshmallow(app).
# This initializes Marshmallow and allows it to introspect the SQLAlchemy components 
# attached to the app. This is why Marshmallow is initialized after SQLAlchemy
ma = Marshmallow(app)