main.pdf: main.tex bar.pdf box.pdf contour.pdf contourf.pdf
	latexmk -pdf

bar.pdf: data.txt plotbarWindrose.py
	python plotbarWindrose.py data.txt

box.pdf: data.txt plotboxWindrose.py
	python plotboxWindrose.py

contour.pdf: data.txt plotcontourWindrose.py
	python plotcontourWindrose.py

contourf.pdf: data.txt plotcontourfWindrose.py
	python plotcontourfWindrose.py

data.txt: makedata.py
	python makedata.py

.PHONY: clean almost_clean

clean: almost_clean
	rm main.pdf
	rm myWindrose.pdf

almost_clean:
	latexmk -c

