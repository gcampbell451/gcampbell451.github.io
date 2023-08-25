LIBNAME chap4 '~/sasuser.v94/Chapter4';
DATA crayons;
	SET chap4.crayons;
RUN;

* a. To view variable attributes in a data set, one can navigate to the
*    OUTPUT DATA tab and click on the variable name in the Columns pane.
*    This populates the values for the variables' properties in a table
*    below.

* b. The variable Color has a label of Crayon Name and a length of 26.;

* c. ;
DATA crayons;
	SET chap4.crayons;
	RETAIN issued1903 0 issued1949 0 issued1958 0 issued1972 0 issued1990 0 issued1993 0;
	IF Issued = 1903 THEN issued1903 + 1;
		ELSE IF Issued = 1949 THEN issued1949 + 1;
		ELSE IF Issued = 1958 THEN issued1958 + 1;
		ELSE IF Issued = 1972 THEN issued1972 + 1;
		ELSE IF Issued = 1990 THEN issued1990 + 1;
		ELSE issued1993 + 1;
RUN;

* The largest number of colors were issued in 1993, with 35.;

* d. ;

PROC SORT DATA = crayons OUT = sortedOnRGB SORTSEQ = LINGUISTIC (NUMERIC_COLLATION = ON);
	BY RGB;
	
* e. ;
PROC PRINT DATA = sortedOnRGB NOOBS;
	VAR Color RGB;
	TITLE 'Colors Sorted by RGB';
RUN;