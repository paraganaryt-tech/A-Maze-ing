run:
	python3 a_maze_ing.py config.txt || true

install:
	pip install --upgrade pip
	pip install build flake8 mypy
	pip install -e .

debug:
	python3 -m pdb a_maze_ing.py config.txt

clean:
	rm -rf __pycache__
	rm -rf mazegen/__pycache__
	rm -rf .mypy_cache
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist
	rm -f output_maze.txt

lint:
	python3 -m flake8 .
	python3 -m mypy .

build:
	python3 -m build