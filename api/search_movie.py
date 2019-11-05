from flask_restplus import Namespace, Resource, fields
from flask import request

from external_api.themoviedb import TheMovieDBAPI

# namespace for these endpoints
movie_search_api = Namespace("search_movie", description="Searching Movie Titles")

# results model defined by themoviedbapi
api_results_model = movie_search_api.model("themoviedb Results", {
    "page": fields.String(),
    "results": fields.List(fields.Raw()),
    "total_results": fields.Integer(),
    "total_pages": fields.Integer()
})

@movie_search_api.route("/", endpoint="search_movie")
class SearchMovie(Resource):
    @movie_search_api.doc(params={
        "query_text": "Text to search movie title with",
        "page_num": "The page number to be requested from the API.",
        "include_adult": "Whether to include mature rated titles",
        "year": "Year to search titles",
        "primary_release_year": "Primary release year to search titles",
    })
    @movie_search_api.marshal_with(api_results_model)
    def get(self):
        if "query_text" not in request.args:
            return "Missing required parameter: query_text", 400

        query_text = request.args.get("query_text")
        page_num = request.args.get("page_num")
        include_adult = request.args.get("include_adult")
        year = request.args.get("year")
        primary_release_year = request.args.get("primary_release_year")
    
        return TheMovieDBAPI.lookup_movie(query_text, page_num, include_adult, year, primary_release_year)