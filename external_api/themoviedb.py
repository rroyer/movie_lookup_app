import requests
import urllib.parse

class TheMovieDBAPI:
    """
    Static class for wrapping requests to the Movie DB external API.
    Documentation for themoviedb api search endpoints can be found here:
    https://developers.themoviedb.org/3/search/search-movies
    
    Attributes:
    api_key (string): API key currently configured to use in the external API requests
    api_version (string): Version number of the API the requests should use.
    base_url (string): The base url of this external API.
    """
    api_key = None
    api_version = "4"
    base_url = "https://api.themoviedb.org/"

    @staticmethod
    def init(api_key):
        """
        Initializes the external api class with an api key configured by the application.
        
        Paramters:
        api_key (string): API key currently configured to use in the external API requests
        """
        if api_key is None or not len(api_key):
            raise Exception("Missing TheMovieDB API key")
        TheMovieDBAPI.api_key = api_key
    
    @staticmethod
    def lookup_movie(query_text, page_num=None, include_adult=None, year=None, primary_release_year=None):
        """
        Formats and sends a query to the Movie DB external API and returns the results. The primary query is text, but if
        any other search paramters are included, they will be passed on to the API.
        
        Paramters:
        query_text (string): Text of the query used to search.
        page_num (int): The page number to be requested from the API.
        include_adult (bool): Whether to include mature rated titles
        year (int): Year to search titles.
        primary_release_year (int): Primary release year to search titles
        
        Returns:
        Dictionary: JSON results returned from the external API.
        """
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
        """
        Formats and sends a request to the Movie DB external API on a given path and passes the paramters, including the api_key.
        
        Paramters:
        path (string): Path of the API to search.
        params (int): Any query string paramters to include.
        
        Returns:
        requests.models.Response: Object returned by the http request.
        """
        params["api_key"] = TheMovieDBAPI.api_key
        request_url = TheMovieDBAPI.base_url + TheMovieDBAPI.api_version + path
        params = urllib.parse.urlencode(params)
        
        return requests.get(url=request_url, params=params)
