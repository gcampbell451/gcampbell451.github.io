LIBNAME chap8 '~/sasuser.v94/Chapter8';
* a. examine data set, create histogram that includes a normal distribution overlay.
     limit plot to counties with 100 patents or more.;
DATA patents;
	SET chap8.patents;
RUN;
DATA patentsCopy;
	SET chap8.patents;
RUN;
PROC SQL;
	CREATE TABLE ge100patents AS
		SELECT Patents
		FROM patentsCopy
		WHERE Patents >= 100;
QUIT;
PROC SGPLOT DATA = ge100patents;
	HISTOGRAM Patents / SCALE = COUNT;
	DENSITY Patents / LINEATTRS = (COLOR = 'Red');	
	TITLE 'Patents per County, USA, Where Number of Patents is GE 100';
RUN;

* b. describe the shape of the histogram in a.
	 The histogram is skewed right.;
	 
* c. create a scatter plot of education versus patents in counties with 100 patents or more.;
PROC SQL;
	CREATE TABLE ge100patentsVeducation AS
		SELECT Patents, Education
		FROM patentsCopy
		WHERE Patents >= 100;
QUIT;
PROC SGPLOT DATA = ge100patentsVeducation;
	SCATTER X = Education Y = Patents;
	TITLE 'Education Versus Patents per County, USA, Where Number of Patents is GE 100';
RUN;

* d. id the county with the largest number of patent by including the name of the county
     as a label on the scatter plot from c.;
PROC SORT DATA = patentsCopy;
	BY DESCENDING Patents;
RUN;
DATA patentsCopy;
	SET patentsCopy;
	IF _n_ = 1 THEN 
		DO;
			maxCounty = 'Santa Clara County';
		END;
	ELSE
		DO;
			maxCounty = "";
			
		END;
RUN;
PROC SGPLOT DATA = patentsCopy;
	SCATTER X = Education Y = Patents / DATALABEL = maxCounty;
	TITLE 'Education Versus Patents per County, USA, Where Number of Patents is GE 100';
RUN;

* e. modify the markers from the plots in c and d to be filled circles with 50% transparency.;
PROC SGPLOT DATA = ge100patentsVeducation;
	SCATTER X = Education Y = Patents / MARKERATTRS = (SYMBOL = CIRCLEFILLED) TRANSPARENCY = .5;
	TITLE 'Education Versus Patents per County, USA, Where Number of Patents is GE 100';
RUN;
PROC SGPLOT DATA = patentsCopy;
	SCATTER X = Education Y = Patents / DATALABEL = maxCounty MARKERATTRS = (SYMBOL = CIRCLEFILLED) TRANSPARENCY = .5;
	TITLE 'Education Versus Patents per County, USA, Where Number of Patents is GE 100';
RUN;