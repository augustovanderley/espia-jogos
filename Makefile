# Default target
all: setup check

setup:
	@export PYTHONPATH="${PYTHONPATH}:$(pwd)/espia_jogos"

jogos:
	poetry run espia jogos $(JOGO)

amigos:
	poetry run espia usuario $(AMIGOS)

grupo:
	poetry run espia extrai-grupo $(GRUPO)

# Target to run tests
check:
	poetry run python -m pytest -vvv

check-ipdb:
	poetry run python -m pytest -s

streamlit:
	poetry run streamlit run espia_jogos/front.py

run-server:
	uvicorn espia_jogos.api:app --reload

.PHONY: all check
