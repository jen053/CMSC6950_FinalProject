main.pdf: main.tex bar.pdf box.pdf contour.pdf contourf.pdf
	latexmk -pdf

bar.pdf: data.csv plotbarWindrose.py
	python plotbarWindrose.py data.csv

box.pdf: data.csv plotboxWindrose.py
	python plotboxWindrose.py data.csv

contour.pdf: data.csv plotcontourWindrose.py
	python plotcontourWindrose.py data.csv

contourf.pdf: data.csv plotcontourfWindrose.py
	python plotcontourfWindrose.py data.csv

data.csv:
	wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=FILEID' -O FILENAME

.PHONY: clean almost_clean

clean: almost_clean
	rm main.pdf
	rm myWindrose.pdf

almost_clean:
	latexmk -c

