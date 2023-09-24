# USAGE

## Setup

```sh
$ poetry install     # install packages for project
Installing dependencies from lock file 
...

$ poetry shell       # start virtual environment
Spawning shell within D:\YourDirectory\flask-server\src\.venv
...
```

### OUTPUT

```text
(flask-server-py3.11) PS D:\Your\Directory\flask-server\src>
```

## Starting Server

```sh
$ poetry run start  # Recommended
 * Serving Flask app 'flask_server'
 ...
```

 OR

```sh
$ poetry run py -m flask_server
 * Serving Flask app 'flask_server'
 ...
```

 OR

- Windows

```sh
$ $env:FLASK_APP = 'flask_server'; flask run
...
```

- Unix

```sh
$ export FLASK_APP=flask_server && flask run
...
```

## Deactivate

```sh
$ deactivate
PS D:\Your\Directory\flask-server\src>
```

## Miscellaneous

- ### Install Poetry

```sh
$ pip install poetry
Collecting poetry
  Obtaining dependency information for poetry ...
```

- ### Install Packages in Poetry

```sh
$ poetry add <your-package-name>
Using version ^ver.sub-ver.sub-sub-ver for <package-name>

Updating dependencies
Resolving dependencies...
```

<!-- Add poetry.toml poetry config virtualenvs.in-project true --local -->
