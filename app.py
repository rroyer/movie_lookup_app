from flask import Flask
from flask_restplus import Api
import configparser
from external_api.themoviedb import TheMovieDBAPI

from api.search_movie import movie_search_api

# load configuration
config = configparser.ConfigParser()
config.read("config.ini")

if not config.has_section("API_KEYS"):
    raise Exception("API_KEYS missing from config.ini")

# initialize external APIs
TheMovieDBAPI.init(config["API_KEYS"].get("THEMOVIEDB_API_KEY"))

# initialize flask app
app = Flask("movie_lookup_app")

# initialize flask swagger
api = Api(app, version="0.1", title="Movie Lookup API", description="Wrapper API for external Movie API searches.")

# add movie search namespace
api.add_namespace(movie_search_api)

if __name__ == "__main__":
    app.run()
    