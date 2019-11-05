from flask import Flask, request
import configparser

from external_api.themoviedb import TheMovieDBAPI

# load configuration and initialize app
config = configparser.ConfigParser()
config.read("config.ini")

#api_keys = config.get("API_KEYS", None)
if not config.has_section("API_KEYS"):
    raise Exception("API_KEYS missing from config.ini")

# initialize external APIs
TheMovieDBAPI.init(config["API_KEYS"].get("THEMOVIEDB_API_KEY"))

# initialize flask app
app = Flask("movie_lookup_app")

# search movie endpoint
@app.route("/search_movie")
def search_movie():
    if "query_text" not in request.args:
        return "Missing required parameter: query_text", 400

    query_text = request.args.get("query_text")
    page_num = request.args.get("page_num")
    include_adult = request.args.get("include_adult")
    year = request.args.get("year")
    primary_release_year = request.args.get("primary_release_year")
    
    return TheMovieDBAPI.lookup_movie(query_text, page_num, include_adult, year, primary_release_year)

if __name__ == "__main__":
    app.run()
    