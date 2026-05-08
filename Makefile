install:
	pip install -r requirements.txt

run:
	uvicorn app.main:app --reload

ingest:
	python scripts/ingest.py ./sample_repo

eval:
	python scripts/eval.py