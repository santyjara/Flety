format:
	isort .
	black .

ut:
	pytest tests/unit

it:
	pytest tests/integration

ft:
	pytest tests/functional

test:
	make ut
	make it
	make ft