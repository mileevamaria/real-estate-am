repl:
	uv run python3
install:
	uv sync
lint:
	uv run ruff check real_estate

build:
	./build.sh
dev:
	uv run flask --debug --app real_estate:app run --port=5001
start:
	gunicorn -w 5 -b 0.0.0.0:8000 real_estate:app
