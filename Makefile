main.pdf: main.tex bar.pdf box.pdf contour.pdf contourf.pdf
	pdflatex main.tex

data.txt: Code/getData.py
	python3 Code/getData.py $(location)

bar.pdf: data.txt Code/plotbarWindrose.py
	python3 Code/plotbarWindrose.py data.txt $(location)

box.pdf: data.txt Code/plotboxWindrose.py
	python3 Code/plotboxWindrose.py data.txt $(location)

contour.pdf: data.txt Code/plotcontourWindrose.py
	python3 Code/plotcontourWindrose.py data.txt $(location)

contourf.pdf: data.txt Code/plotcontourfWindrose.py
	python3 Code/plotcontourfWindrose.py data.txt $(location)

.PHONY: clean almost_clean

clean:
	rm *.pdf
	rm data.txt

almost_clean:
	rm main.log
	rm main.aux

