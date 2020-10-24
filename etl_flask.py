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
engine = create_engine("postgres:///movies.sql")

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save reference to the table
movies = Base.classes.movies
wiki = Base.classes.wiki

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
def wiki():
    """Return a list of all movie names"""

    # Query all passengers
    session = Session(engine)
    results = session.query(wiki.film).all()

    # close the session to end the communication with the database
    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))
    print(all_names)
    return jsonify(all_names)


@app.route("/api/v1.0/movies")
def movies():
    """Return a list movies and where they are streaming"""

    # Open a communication session with the database
    session = Session(engine)

    # Query all passengers
    results = session.query(movies).all()

    # close the session to end the communication with the database
    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_movies = []
    for movie in results:
        movies_dict = {}
        movies_dict["Title"] = movies.title
        movies_dict["Streaming_Channel"] = movies.streaming_channel
        all_movies.append(movies_dict)

    return jsonify(all_movies)


if __name__ == '__main__':
    app.run(debug=True)
