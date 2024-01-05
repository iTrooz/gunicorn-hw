PoC python project using gunicorn, pytest, and a vanilla python thread for background tasks

To install dependencies and get into the poetry venv:
```sh
poetry install
poetry shell
```

Then run the app with
```sh
gunicorn main:app
```

You can run the test with
```sh
python -m pytest
```

You can also take a look at the [CI script](./.github/workflows/build.yml)
