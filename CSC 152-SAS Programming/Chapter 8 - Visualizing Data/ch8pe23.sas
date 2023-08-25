LIBNAME chap8 '~/sasuser.v94/Chapter8';
* a. examine data set, create histogram of most recent population estimates for all countries combined;
DATA population;
	SET chap8.population;
RUN;
DATA populationCopy;
	SET chap8.population;
RUN;
PROC SGPLOT DATA = populationCopy;
	HISTOGRAM Y4 / SCALE = COUNT;
	TITLE 'World Population Estimates, All Countries';
RUN;

* b. create separate histograms of the most recent population estimates for each continent;
PROC FORMAT;
	VALUE $continentName
		'AF' = 'Africa'
		'AS' = 'Asia'
		'AU' = 'Australia'
		'EU' = 'Europe'
		'NA' = 'North America'
		'OC' = 'Oceania'
		'SA' = 'South America';
PROC SGPANEL DATA = populationCopy;
	PANELBY Continent / NOVARNAME SPACING=5;
	HISTOGRAM Y4 / SCALE = COUNT;
	TITLE 'Population By Continent';
	FORMAT Continent $continentName.;
RUN;

* c. create a single graph with box plots of the most recent population estimeates per continent;
PROC SGPANEL DATA = populationCopy;
	PANELBY Continent / NOVARNAME SPACING=5;
	VBOX Y4;
	TITLE 'Population By Continent';
	FORMAT Continent $continentName.;
RUN;
	

* d. describe the main differences between the statistical information from b and c;
* In part b, the only information given by the histogram is what number of countries fell in a given bin.
  The box plots in part c show the Q1, Median, Mean, Q3, Min and Max, and Outliers, giving much greater
  information than merely the histogram.  