SHELL := /bin/zsh

.PHONY: deactivate dev run

env:
	python3 -m venv env

install:
	pip install -r requirements.txt

dev:
	fastapi dev src/

run: 
	fastapi run src/