.PHONY: run 

default: run

run:
	@. .venv/bin/activate; python -m main.run

create-data:
	@. .venv/bin/activate; python -m main.util.data_processor
