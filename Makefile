main.pdf: main.tex myWindrose.pdf
	latexmk -pdf

myWindrose.pdf: data.txt plotWindrose.py
	python plotWindrose.py

data.txt: makedata.py
	python makedata.py

.PHONY: clean almost_clean

clean: almost_clean
	rm main.pdf
	rm myWindrose.pdf

almost_clean:
	latexmk -c

