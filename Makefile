init:
	python -m venv venv

install:
	pip install -r requirements.txt

run:
	uvicorn app:app --reload --port 5000

clean:
	rm -rf venv

test:
	python test.py

freeze:
	pip freeze
