install:
	pip install -r requirements.txt

limpeza:
	python src/limpeza.py

visualizacao:
	python src/visualizacao.py

mapa:
	python src/mapa.py

all: limpeza visualizacao mapa

run:
	python src/app.py

test:
	python3 -m unittest discover -s tests