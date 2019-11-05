# Movie Lookup App
API for searching movies on public APIs

## Getting Started
Clone the repo and install the prerequisites below.

### Prerequisites
Python 3.6+, pip

### Installing

```
pip install -r requirements.txt
```

## To Run

Obtain an API key from themoviedb: https://developers.themoviedb.org
Replace [INSERT KEY HERE] in `config.ini` with your API key

Run:
```
python app.py
```

### Swagger documentation:
Navigate your browser to `http://localhost:5000/`

### Example query:
HTTP GET `http://localhost:5000/search_movie?query_text=taxi&page_num=2`
