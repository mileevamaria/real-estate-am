repl:
	uv run python3
install:
	uv sync
lint:
	uv run ruff check real_estate
devapp:
	uv run flask --debug --app real_estate:app run --port=5001
startapp:
	uv run gunicorn -w 5 -b 0.0.0.0:8000 real_estate:app
