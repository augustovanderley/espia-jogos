# Default target
all: setup check

setup:
	@export PYTHONPATH="${PYTHONPATH}:$(pwd)/espia_jogos"

jogos:
	poetry run espia jogos $(JOGO)

amigos:
	poetry run espia usuario $(AMIGO)

# Target to run tests
check:
	poetry run python -m pytest

.PHONY: all check
