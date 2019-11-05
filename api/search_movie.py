from flask_restplus import Namespace, Resource, fields
from flask import request

from external_api.themoviedb import TheMovieDBAPI

movie_search_api = Namespace('search_movie', description='Searching Movie Titles')

@movie_search_api.route("/", endpoint="search_movie")
class SearchMovie(Resource):
    # search movie endpoint
    @movie_search_api.doc(params={
        "query_text": fields.String(description="Text to search movie title with", required=True),
        "page_num": fields.Integer(description="The page number to be requested from the API.", required=False),
        "include_adult": fields.Boolean(description="Whether to include mature rated titles", required=False),
        "year": fields.Integer(description="Year to search titles", required=False),
        "primary_release_year": fields.Integer(description="Primary release year to search titles", required=False),
    })
    def get(self):
        if "query_text" not in request.args:
            return "Missing required parameter: query_text", 400

        query_text = request.args.get("query_text")
        page_num = request.args.get("page_num")
        include_adult = request.args.get("include_adult")
        year = request.args.get("year")
        primary_release_year = request.args.get("primary_release_year")
    
        return TheMovieDBAPI.lookup_movie(query_text, page_num, include_adult, year, primary_release_year)