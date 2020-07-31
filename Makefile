main.pdf: main.tex bar.pdf box.pdf contour.pdf contourf.pdf
	latexmk -pdf

data.txt: getData.py
	python getData.py location

bar.pdf: data.txt plotbarWindrose.py
	python plotbarWindrose.py data.txt

box.pdf: data.txt plotboxWindrose.py
	python plotboxWindrose.py data.txt

contour.pdf: data.txt plotcontourWindrose.py
	python plotcontourWindrose.py data.txt

contourf.pdf: data.txt plotcontourfWindrose.py
	python plotcontourfWindrose.py data.txt

.PHONY: clean almost_clean

clean: almost_clean
	rm *.pdf
	rm data.txt

almost_clean:
	latexmk -c

