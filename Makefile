.PHONY: run build tailwind migrate superuser clean format lint install

# Run Django development server
run:
	python manage.py runserver 0.0.0.0:8000

# Run Tailwind CSS build process
tailwind:
	python manage.py tailwind start

# Build Tailwind CSS for production
build:
	python manage.py tailwind build

# Run migrations
migrate:
	python manage.py makemigrations
	python manage.py migrate

# Lint code with Ruff
lint:
	uv run ruff check

# Install dependencies with UV
install:
	uv pip install -e .

# Clean Python cache files
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete