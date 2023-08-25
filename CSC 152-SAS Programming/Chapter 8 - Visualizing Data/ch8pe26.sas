LIBNAME chap8 '~/sasuser.v94/Chapter8';
* a. create a scatter plot of year and magnitude for quakes in 2000+;
DATA quakes;
	SET chap8.earthquakes;
RUN;
DATA quakesCopy;
	SET chap8.earthquakes;
RUN;
PROC SQL;
	CREATE TABLE yearVmag AS
		SELECT Year, Magnitude
		FROM quakesCopy
		WHERE Year >= 2000;
QUIT;
PROC SGPLOT DATA = yearVmag;
	SCATTER X = Year Y = Magnitude;
	XAXIS VALUES = (2000 TO 2011 BY 1);
	TITLE 'Earthquake Magnitudes by Year, 2000-2011';
RUN;

* b. overlay a time series plot of mean magnitude for each year on the same graph as a, in red;
PROC SQL;
	CREATE TABLE meanMagByYear AS
		SELECT Year, Magnitude, MEAN(Magnitude) AS Mean FORMAT = comma12.2
		FROM yearVmag
		GROUP BY Year;
QUIT;
PROC SGPLOT DATA = meanMagByYear;
	SCATTER X = Year Y = Magnitude;
	SERIES X = Year Y = Mean / LINEATTRS = (COLOR = Red);
	XAXIS VALUES = (2000 TO 2011 BY 1);
	TITLE 'Earthquake Magnitudes by Year, 2000-2011';
RUN;

* c.include legend that labels timeseries plot as Mean. legend should be in bottom right and have no border;
PROC SGPLOT DATA = meanMagByYear;
	SCATTER X = Year Y = Magnitude;
	SERIES X = Year Y = Mean / LINEATTRS = (COLOR = Red);
	KEYLEGEND / LOCATION = INSIDE POSITION = BOTTOMRIGHT NOBORDER;
	XAXIS VALUES = (2000 TO 2011 BY 1);
	TITLE 'Earthquake Magnitudes by Year, 2000-2011';
RUN;

* d. overlay reference lines for light, moderate, strong, major, and great quakes. lines should be
	dashed, labeled, and have .5 transparency;
PROC SGPLOT DATA = meanMagByYear;
	SCATTER X = Year Y = Magnitude;
	SERIES X = Year Y = Mean / LINEATTRS = (COLOR = Red);
	REFLINE 4.0 5.0 6.0 7.0 8.0 / LABEL = ('Light' 'Moderate' 'Strong' 'Major' 'Great') TRANSPARENCY = .5;
	KEYLEGEND / LOCATION = INSIDE POSITION = BOTTOMRIGHT NOBORDER;
	XAXIS VALUES = (2000 TO 2011 BY 1);
	TITLE 'Earthquake Magnitudes by Year, 2000-2011';
RUN;
	
* e. make sure all years appear on x-axis;