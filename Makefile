# Default target
all: setup check

setup:
	@export PYTHONPATH="${PYTHONPATH}:$(pwd)/espia_jogos"

jogos:
	poetry run espia jogos $(JOGO)

amigos:
	poetry run espia usuario $(AMIGO)

grupo:
	poetry run espia extrai-grupo $(GRUPO)

# Target to run tests
check:
	poetry run python -m pytest

.PHONY: all check
