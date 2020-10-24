# Docs on session basics
# https://docs.sqlalchemy.org/en/13/orm/session_basics.html

import numpy as np
import os

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
pg_user = 'postgres'
pg_password = 'postgres'
db_name = 'ETL Project'

connection_string = f"{pg_user}:Jennifer11@localhost:5432/{db_name}"
engine = create_engine(f'postgresql://{connection_string}')


# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save reference to the table
movies = Base.classes.movies
wiki = Base.classes.wiki
# table = Base.classes.wiki_movie

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/movies<br/>"
        f"/api/v1.0/wiki"
    )


@app.route("/api/v1.0/wiki")
def wiki_():
    """Return a list of all movie names"""

    # Query all movies
    session = Session(engine)
    results = session.query(wiki.film).all()

    # close the session to end the communication with the database
    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))
    print(all_names)
    return jsonify(all_names)


@app.route("/api/v1.0/movies")
def movies_():
    """Return a list movies and where they are streaming"""

    # Query all movies
    session = Session(engine)
    results = session.query(movies.title).all()

    # close the session to end the communication with the database
    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))
    print(all_names)
    return jsonify(all_names)



if __name__ == '__main__':
    app.run(debug=True)
