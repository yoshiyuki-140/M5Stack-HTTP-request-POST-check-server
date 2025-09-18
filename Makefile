.PHONY: venv run
venv:
	echo "source ./.venv/bin/activate" | clip.exe

run:
	python main.py
