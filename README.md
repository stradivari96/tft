# tft

https://api.tft.xiang.es/docs

## Development
1. Create a virtualenv with Python3.9 (eg: `python3.9 -m venv venv`)
2. Activate the virtualenv (eg: `source venv/bin/activate`)
3. Install the dependencies: `pip install -r requirements-dev.txt`
4. Setup pre-commit hooks: `pre-commit install`
5. Copy the `.env.example` file to `.env` and fill in the values
6. Run the server: `uvicorn tft.main:app --reload`
7. Go to http://localhost:8000/docs

## Updating dependencies
Add to `requirements.in` or `requirements-dev.in` and run:
```
pip-compile requirements.in
pip-compile requirements-dev.in
```