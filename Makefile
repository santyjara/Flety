format:
	#autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place . --ignore-init-module-imports --exclude venv
	isort .
	black .

ut:
	pytest tests/unit --asyncio-mode=strict

it:
	pytest tests/integration --asyncio-mode=strict

ft:
	pytest tests/functional --asyncio-mode=strict

test:
	make ut
	make it
	make ft