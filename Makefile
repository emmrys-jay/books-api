SHELL := /bin/zsh

.PHONY: deactivate dev run

env:
	python3 -m venv env

install:
	pip install -r requirements.txt

dev:
	fastapi dev main.py

run: 
	fastapi run main.py