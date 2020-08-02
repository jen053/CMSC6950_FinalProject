# CMSC 6950 Open Science Project
## Windrose: Getting Started

Welcolme to Jacob Newman's CMSC 6950 final project. This project focuses on the Python based Windrose package which plots wind speed and directional data to generate polar (rose) diagrams for wind data.
This work flow takes a number of the elements of the Windrose package and applies them to user selected wind data from airports around Newfoundland and Labrador. Once a certain data set (see below) has 
been selected, a Makefile runs all the needed scripts to produce plots and to generate a report.

To begin the workflow implementation, clone the repository to a system capable of running a Makefile. To run this projects workflow, a number of instances have to be installed:
### Dependences:

(1). The windrose package should be installed via pip: pip install windrose
     addtional packages that are used in the backgroud of windrose are numpy
     and matplotlib. Alternativly, the windrose package files can be clone  
     from git via git clone https://github.com/python-windrose/windrose
     Additional information can be found at: https://pypi.org/project/windrose/

(2). Some type of LaTeX complier must be installed such that a .tex file can be called
     by a pdflatex.exe to generate a .pdf file. (https://www.tug.org/texlive/).

(3). As stated above, a Makefile must be able to be complied on the system.

### Data Access:

When running the Makefile a location variable needs to be passed. This location varible defines what dataset should be retrived from a wind data repository. All the availble locations are airports from 
around Newfoundland and Labrador including:

* Argentia_1953-1970 
* Buchans_1953-1965 
* Cartwright_2015-2018
* ChurchillFalls_2011-2019 
* DeerLake_1980-2012 
* Gander_1980-2012
* GooseBay_1990-2019 
* Makkovik_2015-2019 
* Mary'sHarbour_2013-2015
* Nain_1990-2015 
* Saglek_1991-1994 
* St.Anthony_2009-2012
* St.Johns_2012-2019 
* Stephenville_1980-2012 
* WabushLake_1985-2013
