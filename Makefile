maint:
	pre-commit autoupdate
	pip-compile -U requirements/ci.in
	pip-compile -U requirements/dev.in

upload:
	flit publish

install:
	pip install -e .

start:
	jump_and_run_game
