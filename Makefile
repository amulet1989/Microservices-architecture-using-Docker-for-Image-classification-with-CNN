

test:
	pytest tests/

format:
	black .
	isort . --recursive --profile black