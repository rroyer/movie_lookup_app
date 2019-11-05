import requests
import urllib.parse

class TheMovieDBAPI:
    api_version = "4"
    base_url = "https://api.themoviedb.org/"

    @staticmethod
    def init(api_key):
        if api_key is None or not len(api_key):
            raise Exception("Missing TheMovieDB API key")
        TheMovieDBAPI.api_key = api_key
    
    @staticmethod
    def lookup_movie(query_text, page_num=None, include_adult=None, year=None, primary_release_year=None):
        path = "/search/movie"
        params = {"query": query_text}
        if page_num is not None:
            params["page"] = page_num
        if include_adult is not None:
            params["include_adult"] = include_adult
        if year is not None:
            params["year"] = year
        if primary_release_year is not None:
            params["primary_release_year"] = primary_release_year
        
        response = TheMovieDBAPI.send_request(path, params)

        if response.status_code != 200:
            raise Exception('Did not get a valid response from the external API: (' + str(response.status_code) + ') ' + response.reason)
        
        return response.json()
    
    @staticmethod
    def send_request(path, params):
        params["api_key"] = TheMovieDBAPI.api_key
        request_url = TheMovieDBAPI.base_url + TheMovieDBAPI.api_version + path
        params = urllib.parse.urlencode(params)
        
        return requests.get(url=request_url, params=params)
