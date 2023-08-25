LIBNAME chap5 '~/sasuser.v94/Chapter5';
DATA earthquakes;
	SET chap5.earthquakes;
RUN;

* a.;
PROC FORMAT;
	VALUE size
		  LOW -< 7.0 = 'Normal'
		  7.0 - HIGH = 'Major to Great';
RUN;

PROC TABULATE DATA = chap5.earthquakes;
	CLASS State Magnitude Year; 
	TABLE Magnitude State;
	FORMAT Magnitude size.;
RUN;

* there were 70 earthquakes GE magnitude 7.0;

* b.;
ODS TRACE ON;
PROC TABULATE DATA = chap5.earthquakes;
	CLASS State Magnitude Year; 
	TABLE Year * Magnitude  * State;
	FORMAT Magnitude size.;
ODS OUTPUT Table = tabout;
RUN;
ODS TRACE OFF;

* c.;
ODS PDF FILE = '~/sasuser.v94/Chapter5/Quakes.pdf' STYLE = ANALYSIS;
ODS NOPROCTITLE;

PROC SQL;
	CREATE TABLE manyBigQuakes AS
		SELECT state, COUNT(N)
		FROM tabout
		WHERE magnitude > 6.9
		GROUP BY state
		HAVING COUNT(N) > 1;
QUIT;

PROC PRINT DATA = manyBigQuakes NOOBS LABEL;
	VAR State _TEMG001;
	LABEL _TEMG001 = "Quakes >= 7.0";
	TITLE 'Earthquakes with Magnitude GE 7.0 by State';
RUN;

ODS PDF CLOSE;

* d.;
ODS PDF FILE = '~/sasuser.v94/Chapter5/Quakes2.pdf' STYLE = ANALYSIS STARTPAGE = NO;
ODS NOPROCTITLE;

PROC SQL;
	CREATE TABLE manyBigQuakes AS
		SELECT state, COUNT(N)
		FROM tabout
		WHERE magnitude > 6.9
		GROUP BY state
		HAVING COUNT(N) > 1;
QUIT;

PROC SQL;
	CREATE TABLE bigAfter2000 AS
		SELECT state, magnitude, year
		FROM tabout
		WHERE magnitude > 6.9 AND year >= 2000;
QUIT;

PROC PRINT DATA = manyBigQuakes NOOBS LABEL;
	VAR State _TEMG001;
	LABEL _TEMG001 = "Quakes >= 7.0";
	TITLE 'Earthquakes with Magnitude GE 7.0 by State';
RUN;

PROC PRINT DATA = bigAfter2000 NOOBS;
	VAR state magnitude year;
	TITLE 'Major to Great Events Since 2000';
RUN;
ODS PDF CLOSE;



