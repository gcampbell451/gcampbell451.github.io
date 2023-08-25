PROC IMPORT DATAFILE = "~/sasuser.v94/Chapter3/RoseBowl.xlsx" OUT = rosebowl
	DBMS = XLSX REPLACE;
RUN;

DATA rosebowl;
	SET rosebowl;
	PointDiff = WinPts - LosePts;
	RETAIN TotalGames 0 TotalPoints 0;
	TotalGames + 1;
	TotalPoints + WinPts + LosePts;
RUN;

PROC PRINT DATA = rosebowl;
	FORMAT GameDate WEEKDATE29.;
	TITLE 'Rose Bowl Winners with Selected Formats and Variables';
RUN;