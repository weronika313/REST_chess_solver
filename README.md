# REST-chess-solver

A flask-driven restful API for checking the moves of chess pieces 


## Technologies used
* **[Python3](https://www.python.org/downloads/)** - A programming language
* **[Flask](https://flask.pocoo.org)** - A microframework for Python based on Werkzeug, Jinja 2 and good intentions
* **[Virtualenv](https://virtualenv.pypa.io/en/stable/)** - A tool to create isolated virtual environments
* **[Pytest](https://pypi.org/project/pytest/)** – A framework that makes building simple and scalable tests easy. 


## Running 

Start flask server

## Usage
### Users endpoint

#### TO GET AVAILABLE MOVES LIST:
    [GET] /api/v1/{chess-figure}/{current-field}

EXAMPLE:

    REQUEST

        curl http://127.0.0.1:5000/api/v1/rook/h2

    RESPONSE
```json
{
    "availableMoves":["H1","H3","H4","H5","H6","H7","H8","A2","B2","C2","D2","E2","F2","G2"],
    "current_field":"h2",
    "error":null,
    "figure":"rook"}
```

#### TO CHECK MOVE:
    [GET] /api/v1/{chess-figure}/{current-field}/{dest-field}

EXAMPLE:

    REQUEST
        curl http://127.0.0.1:5000/api/v1/rook/h2/h5

    RESPONSE
```json
{
    "current_field":"h2",
    "destField":"h5",
    "error":null,
    "figure":"rook",
    "move":"valid"}
```


