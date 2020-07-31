main.pdf: main.tex bar.pdf box.pdf contour.pdf contourf.pdf
	pdflatex main.tex

data.txt: getData.py
	python3 Code/getData.py location

bar.pdf: data.txt plotbarWindrose.py
	python3 Code/plotbarWindrose.py data.txt

box.pdf: data.txt plotboxWindrose.py
	python3 Code/plotboxWindrose.py data.txt

contour.pdf: data.txt plotcontourWindrose.py
	python3 Code/plotcontourWindrose.py data.txt

contourf.pdf: data.txt plotcontourfWindrose.py
	python3 Code/plotcontourfWindrose.py data.txt

.PHONY: clean almost_clean

clean: almost_clean
	rm *.pdf
	rm data.txt
	
almost_clean:
	rm main.log
	rm main.aux

