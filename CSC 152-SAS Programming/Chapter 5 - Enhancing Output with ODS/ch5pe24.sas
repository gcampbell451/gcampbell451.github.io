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
ODS PDF FILE = 'C:\Desktop\Quakes.pdf' STYLE = ANALYSIS;
ODS NOPROCTITLE;

DATA tabout;
	IF Magnitude < 7.0 THEN DELETE;
RUN;

PROC PRINT DATA = tabout;
	SUM N;
	VAR State N;
	TITLE 'Earthquakes with Magnitude GE 7.0 by State';
RUN;



