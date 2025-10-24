install:
	uv sync

lint:
	uv run ruff check .

migrate:
	uv run python manage.py migrate --noinput

collectstatic:
	uv run python manage.py collectstatic --noinput

start:
	uv run python manage.py runserver 0.0.0.0:8000

render-start:
	gunicorn my_project.wsgi

build:
	./build.sh